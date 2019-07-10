"""Documo class to upload document and get extracted data"""
import os

import requests

from .error import NoAPIKey, UnsupportedDocumentType
from .config import allowed_file_types


class Docsumo:
    """
    Initializes an object of Docsumo class.

    Args:
        apiKey:``str``
            API key provided to user.
        url:``str``    
            Url of docsumo api
        version:``str``
            API version.
    Returns:
        Docsumo class object.            
    """

    def __init__(self, apikey=None, url=None, version="v1"):

        if apikey:
            self.apikey = apikey
        else:
            self.apikey = os.getenv("DOCSUMO_API_KEY", None)
            if not self.apikey:
                raise NoAPIKey("Either pass apikey or set env `DOCSUMO_API_KEY`")

        if url:
            self.url = url
        else:
            self.url = "https://app.docsumo.com/"

        self.version = version
        self.headers = {"apikey": self.apikey}

    @staticmethod
    def _validate_date(date):
        """validate date has format of YYYY-MM-DD"""
        date_list = date.split("-")
        if len(date_list) == 3:
            if len(date_list[0]) == 4:
                if len(date_list[1]) == 2 and len(date_list[2]) == 2:
                    return True

        raise Exception("format should be 'YYYY-MM-DD'")

    def user_detail_credit_limit(self):
        """
        Provides credit limit information for user.
        Provides the information on the number of documents
        that the user can upload and the number of documents the user has already uploaded.

        Returns:
            Limit Information : ``dict``

            .. code-block:: json

                {
                    'error': '',
                    'error_code': '',
                    'message': '',
                    'status': 'success',
                    'status_code': 200,
                    'data': {
                        'email': 'bkrm.dahal@gmail.com',
                        'full_name': 'Bikram Dahal',
                        'monthly_doc_current': 10,
                        'monthly_doc_limit': 300,
                        'user_id': '5cbcb201a79f0f1d983a34ea'
                    }
                }

        """

        url = "{}/api/{}/eevee/apikey/limit/".format(self.url, self.version)
        response = requests.request("GET", url, headers=self.headers)
        original_response = response.json()
        return original_response

    def documents_list(
        self,
        offset=0,
        limit=20,
        status="",
        created_date_greater_than="",
        created_date_less_than="",
    ):
        """
        Returns basic details of all the documents uploaded by the user.

        Args:
            offset:``int``
                Index from where to fetch the list of documents.
            limit:``int``
                Number of documents whose details are to be fetched.
            status:``list``
                The status of the documents ``processed`` ``new`` ``review_required`` 
                ``review_skipped``.
            created_date_greater_than: ``str``
                format ``YYYY-MM-DD``
            created_date_less_than: ``str``
                format ``YYYY-MM-DD`` 

        Returns:
            Document list with details : ``dict``

            .. code-block:: json
            
                {
                    'data': {
                        'documents': [{
                                'doc_id': '1c37c1b0dc42416e91c7fa6a324f99a2',
                                'status': 'new',
                                'title': '6ca2bbf358ba4c8e9be7751b91aba3e5.pdf',
                                'type': 'invoice'
                            },
                            {
                                'doc_id': '9ec5b02a3caf423eb08e740c5696082b',
                                'status': 'new',
                                'title': '6ca2bbf358ba4c8e9be7751b91aba3e5.pdf',
                                'type': 'invoice'
                            },
                            {
                                'doc_id': 'f362e1fff99b4f329b5cfe79fe813cc9',
                                'status': 'review_required',
                                'title': 'c05440f11dda4cfba70a856114e12a50.jpg',
                                'type': 'invoice'
                            },
                            {
                                'doc_id': '5a031d2f4e224c069f9bd5016f941074',
                                'status': 'review_required',
                                'title': 'c05440f11dda4cfba70a856114e12a50.jpg',
                                'type': 'invoice'
                            },
                            {
                                'doc_id': '1644a07973fd4f919a298c7792469700',
                                'status': 'review_required',
                                'title': 'c05440f11dda4cfba70a856114e12a50.jpg',
                                'type': 'invoice'
                            }
                        ],
                        'limit': 5,
                        'offset': 0,
                        'total': 11
                    },
                    'error': '',
                    'error_code': '',
                    'message': '',
                    'status': 'success',
                    'status_code': 200
                }
        """
        url = "{}/api/{}/eevee/apikey/documents/".format(self.url, self.version)

        # make query string
        querystring = {"offset": offset, "limit": limit, "sort_by": "created_date.desc"}

        # if status add the status
        if status:
            querystring.update({"status": status})

        # if date
        date = []
        if created_date_greater_than:
            _ = self._validate_date(created_date_greater_than)
            date.append("gte:{}".format(created_date_greater_than))

        if created_date_less_than:
            _ = self._validate_date(created_date_less_than)
            date.append("lte:{}".format(created_date_less_than))

        # added date to query string
        if date:
            querystring.update({"created_date": date})

        response = requests.request(
            "GET", url, headers=self.headers, params=querystring
        )
        return response.json()

    def extracted_data(self, doc_id):
        """
        Returns details of a document whose valid document id is provided in doc_id agrument.

        Args:
            doc_id:``str``
                Valid Document Id of the document whose detail is required. 

        Returns:
            Document details : ``dict`` 

            .. code-block:: json

                {
                    'data': {
                                'Basic Information': {
                                    'Invoice Number': '307538597',
                                    'Issue Date': '06/16/2014',
                                    'Terms': ''
                                },
                                'Buyer Detail': {
                                    'Address': 'Ticket Buyer '
                                    'Company Street 1 '
                                    'Adelaide, 55555 '
                                    'Australia',
                                    'GST/ VAT Number': '',
                                    'Name': 'Ticket Buyer Company '
                                    'Name'
                                },
                                'GST & Amount': {
                                    'Subtotal': '',
                                    'Tax Rate': '15 %',
                                    'Tax Total': '',
                                    'Total Due': 7.04
                                },
                                'Line Items': [{
                                        'Description': 'Item '
                                        'Description',
                                        'HSN': '',
                                        'Quantity': 'Quantity',
                                        'Subtotal Line': 'Sub-Total '
                                        '(net)',
                                        'Tax Rate Line': 'GST',
                                        'Unit Price': 'Unit Price '
                                        '(net)'
                                    },
                                    {
                                        'Description': 'Adult Plates',
                                        'HSN': '',
                                        'Quantity': '',
                                        'Subtotal Line': '$5.00',
                                        'Tax Rate Line': '15 %',
                                        'Unit Price': '$5.00'
                                    },
                                    {
                                        'Description': '> Eventbrite '
                                        'Service & '
                                        'Payment Fees',
                                        'HSN': '',
                                        'Quantity': '',
                                        'Subtotal Line': '$1.29',
                                        'Tax Rate Line': '0%',
                                        'Unit Price': ''
                                    },
                                    {
                                        'Description': 'Children',
                                        'HSN': '',
                                        'Quantity': '',
                                        'Subtotal Line': '$0.00',
                                        'Tax Rate Line': '0%',
                                        'Unit Price': '$0.00'
                                    },
                                    {
                                        'Description': '> Eventbrite '
                                        'Service & '
                                        'Payment Fees',
                                        'HSN': '',
                                        'Quantity': '',
                                        'Subtotal Line': '$0.00',
                                        'Tax Rate Line': '0%',
                                        'Unit Price': ''
                                    }
                                ],
                                'Seller Detail': {
                                    'Address': 'Adelaide, 55555 '
                                    'Australia',
                                    'GST/ VAT Number': '',
                                    'Name': 'Organizer Company '
                                    'Name'
                                }
                            }
                    'error': '',
                    'error_code': '',
                    'message': '',
                    'status': 'success',
                    'status_code': 200
                }
        """

        url = "{}/api/{}/eevee/apikey/data/{}/".format(self.url, self.version, doc_id)
        response = requests.request("GET", url, headers=self.headers)
        original_response = response.json()
        return original_response

    def documents_summary(self):
        """
        Summary of all document status

        Returns:
            Limit Information : ``dict``

            .. code-block:: json

                {
                    'error': '',
                    'error_code': '',
                    'message': '',
                    'status': 'success',
                    'status_code': 200,
                    'data': {
                        "processed":1,
                        "new":1
                    }
                }
        """

        url = "{}/api/{}/eevee/apikey/documents/summary/".format(self.url, self.version)
        response = requests.request("GET", url, headers=self.headers)
        original_response = response.json()
        return original_response

    def upload_file(self, file_path, doc_type):
        """
        Uploads valid documents for processing.

        Args:
            file_path:``str``
                Path of document to be uploaded.
            doc_type:``str``
                Document type. Currently supported: ``invoice``, ``invoice_financing``, ``bank_statements`` 
        Returns:
            Document upload details for successful uploads : ``dict``                          
        
            .. code-block:: json
            
                {
                    'data': {
                            'created_at': 'Mon, 22 Apr 2019 11:56:53 GMT',
                            'doc_id': '16474639f3da47beb87788c875503009',
                            'email': 'bkrm.dahal@gmail.com',
                            'status': 'new',
                            'title': 'c05440f11dda4cfba70a856114e12a50.jpg',
                            'type': 'invoice',
                            'url_original': 'https://test.png',
                            'user_id': '5cbcb201a79f0f1d983a34ea'
                    },
                    'error': '',
                    'error_code': '',
                    'message': '',
                    'status': 'success',
                    'status_code': 200
                }
        """
        doc_type = doc_type.lower()

        if not doc_type in allowed_file_types:
            raise UnsupportedDocumentType(
                "{} document type is not supported. Supported types: {}".format(
                    doc_type, allowed_file_types
                )
            )

        url = "{}/api/{}/eevee/apikey/upload/".format(self.url, self.version)
        headers = {"apikey": self.apikey}

        filename = os.path.basename(file_path)

        multipart_form_data = {
            "files": (filename, open(file_path, "rb")),
            "type": (None, doc_type),
            "uploaded_from": (None, "api"),
        }

        response = requests.post(url, files=multipart_form_data, headers=headers)
        original_response = response.json()
        return original_response

    def delete_documents(self, doc_ids):
        """
        delete document
        Args:
            doc_ids:``list``
                list of doc_ids 

        Returns: 
            Doc_ids Detail: `json`

                .. code-block:: json
            
                    {
                        'deleted_doc': [],
                        'not_deleted_doc': [{'doc_id': 'ghsd',
                                            'err_message': 'files doesnt exist'}, ..]
                    }
        """

        if isinstance(doc_ids, list):
            if doc_ids:
                for doc_id in doc_ids:
                    url = "{}/api/{}/eevee/apikey/delete/{}/".format(
                        self.url, self.version, doc_id
                    )
                    response = requests.request(
                        "POST", url, headers={"apikey": self.apikey}
                    )
                    _ = response.json()
                return {"deleted_doc": doc_ids, "not_deleted_doc": []}
            else:
                raise ValueError("doc_ids should have have atleast one doc_id")
        else:
            raise TypeError("doc_ids should be list")

    def delete_documents_all(self):
        """
        Delete all documents

        Returns:
            Deleted Doc list : ``list``

        """
        docs = self.documents_list(limit=10000)
        doc_ids = [i["doc_id"] for i in docs["data"]["documents"]]
        if doc_ids:
            for doc_id in doc_ids:
                url = "{}/api/{}/eevee/apikey/delete/{}/".format(
                    self.url, self.version, doc_id
                )
                _ = requests.request("POST", url, headers={"apikey": self.apikey})
            return doc_ids
        else:
            return []

    def __str__(self):
        return "Docsumo API"

    def __repr__(self):
        return "Docsumo API"
