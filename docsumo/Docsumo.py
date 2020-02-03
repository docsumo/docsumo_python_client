"""Docsumo class to upload document and get extracted data"""
import os

import requests

from .error import NoAPIKey, UnsupportedDocumentType, LengthNotMatched
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
        self.doc_titles = None

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

               {'data': {'invoice': {'date': {'model': '',
                            'orig_value': '',
                            'position': [1993, 474, 2086, 495],
                            'value': '5/15/2018'},
                        'number': {'model': '',
                            'orig_value': '',
                            'position': [1920, 424, 2087, 448],
                            'value': '19'},
                        'total_amount_ex': {'model': '',
                            'orig_value': '',
                            'position': [1817, 888, 1862, 905],
                            'value': '284'},
                        'total_btw': {'model': '',
                            'orig_value': '',
                            'position': [1922, 889, 1958, 903],
                            'value': '56'}},
                        'transactions': [{'amount': {'orig_value': '', 'position': '', 'value': ''},
                            'date': {'orig_value': '', 'position': '', 'value': ''},
                            'product': {'orig_value': '', 'position': '', 'value': ''},
                            'qty': {'orig_value': '', 'position': '', 'value': ''},
                            'vat': {'orig_value': '', 'position': '', 'value': ''}}]},
                        'error': '',
                        'error_code': '',
                        'message': '',
                        'meta_data': {'status': 'reviewing',
                        'title': '9cdacd30524bcb7b60fa92ac953f216b.pdf',
                        'user_id': '5e299e55033461d41704b284'},
                        'status': 'success',
                        'status_code': 200}
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

    def upload_file(self, file_path, doc_title, user_doc_id=None):
        """
        Uploads valid documents for processing.
        Args:
            file_path:``str``
                Path of document to be uploaded.
            doc_title:``str``
                Document title. You can get title using ``user_detail_credit_limit``.
            user_doc_id: ``str``
                document id given by user
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
        doc_type = doc_title

        if not self.doc_titles:
            user_detail = self.user_detail_credit_limit()["data"]
            doc_titles = user_detail.get("document_types", None)

            if not doc_titles:
                return {
                    "error": "no key document_types in method user_detail_credit_limit"
                }
            else:
                self.doc_titles = {i["title"]: i["value"] for i in doc_titles}

        if not doc_type in self.doc_titles:
            raise UnsupportedDocumentType(
                "{} document type is not supported. Supported types: {}".format(
                    doc_type, list(self.doc_titles.values())
                )
            )
        else:
            doc_type = self.doc_titles[doc_type]

        url = "{}/api/{}/eevee/apikey/upload/".format(self.url, self.version)
        headers = {"apikey": self.apikey}

        filename = os.path.basename(file_path)

        multipart_form_data = {
            "files": (filename, open(file_path, "rb")),
            "type": (None, doc_type),
            "uploaded_from": (None, "api"),
        }
        if user_doc_id:
            multipart_form_data["user_doc_id"]: (None, user_doc_id)

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

    def extracted_ocr(self, doc_id):
        """
        Returns ocr detail for document
        Args:
            doc_id:``str``
                Valid Document Id of the document whose detail is required. 
        Returns:
            Document ocr details : ``dict`` 
        """

        url = "{}/api/{}/eevee/apikey/ocr/{}/".format(self.url, self.version, doc_id)
        response = requests.request("GET", url, headers=self.headers)
        original_response = response.json()
        return original_response

    def _update_item(self, doc_id, item_id, value, position):
        """
        update value and position of item
        Args:
            doc_id:``str``
                Valid Document Id of the document whose detail is required. 
            item_id: ``int ``
                Item id to update
            value: ``str``
                new value of filed
            position: ``list``
                list of position as ``[x, y, x1, y1]
        Returns:
            responses : ``dict`` 
        """
        data = {"value": value, "position": position}
        url = "{}/api/{}/eevee/apikey/update/item/{}/{}/".format(
            self.url, self.version, doc_id, item_id
        )
        response = requests.request("POST", url, headers=self.headers, json=data)
        original_response = response.json()
        return original_response

    def _add_item(self, doc_id, item_dict):
        """
        add new item to list
        Args:
            doc_id:``str``
                Valid Document Id of the document whose detail is required. 
            item_dict: ``dict``
                complete dict of item
                    ..code-block :: json
                        {
                            "content": {
                            "is_valid_format": True, 
                            "orig_value": "test", 
                            "page": 1, 
                            "position": [], 
                            "validation_source": "human", 
                            "value": "test"
                            }, 
                            "doc_id": "8cb8ad65d6684165b32eed755a416138", 
                            "filters": {}, 
                            "format": "%s", 
                            "format_message": "value should be string", 
                            "id": 1001005, 
                            "ignore": False, 
                            "label": "new label", 
                            "low_confidence": False, 
                            "no_items_row": 1, 
                            "p_title": "Basic Information", 
                            "p_type": "basic_info", 
                            "parent_id": 1001, 
                            "time_spent": 4, 
                            "type": "string", 
                            "user_id": "5d4122f07c38c76c74073af7", 
                            "validation_source": "human"
                        }
        Returns:
            Responses : ``dict`` 
        """

        data = item_dict
        url = "{}/api/{}/eevee/apikey/add/item/{}/".format(
            self.url, self.version, doc_id
        )
        response = requests.request("POST", url, headers=self.headers, json=data)
        original_response = response.json()
        return original_response

    def upload_files(self, file_paths, doc_title, user_doc_ids=None):
        """
        Uploads valid document lists for processing.

        Args:
            file_paths:``list``
                List of document paths to be uploaded.
            doc_type:``str``
                Document type. Currently supported: (Invoice, Invoice_drip, bank_statements)`` 
            user_doc_ids: ``list``
                List of Document Id to be uploaded. Optional
        Returns:
            Document upload details for successful uploads : ``dict``                          
        
            .. code-block:: json
            
                {
                    'files_uploaded': [{
                                            'data': {
                                                'created_at': 'Fri, 08 Nov 2019 07:18:29 GMT',
                                                'doc_id': 'd96cf1528e214ba595541eefc71f6145',
                                                'email': 'saugat.adhikari@docsumo.com',
                                                'status': 'new',
                                                'title': 'invoice_1.png',
                                                'type': 'invoice',
                                                'url_original': 'https://s3.ap-south-1.amazonaws.com/testing-docsumo-documents/5dbfad7b14ffdef4ccea0840/16167/d96cf1528e214ba595541eefc71f6145.png',
                                                'user_doc_id': 'd96cf1528e214ba595541eefc71f6145',
                                                'user_id': '5dbfad7b14ffdef4ccea0840'
                                            },
                                            'error': '',
                                            'error_code': '',
                                            'message': '',
                                            'status': 'success',
                                            'status_code': 200
                                        }],
                    'files_not_uploaded': [{
                                            'metadata': {
                                                'user_doc_id': '7',
                                                'title': 'invoice_1.png'
                                                },
                                                'error': 'Duplicated user_id ',
                                                'message': '',
                                                'status': 'fail',
                                                'status_code': 409
                                            },
                                            {
                                            'metadata': {
                                                'user_doc_id': '333', 
                                                'title': 'invoice_2.jpg'
                                                },
                                                'error': 'Duplicated user_id ',
                                                'message': '',
                                                'status': 'fail',
                                                'status_code': 409
                                            }
                                        ]}
        """
        doc_type = doc_title
        doc_type = doc_type.lower()

        url = "{}/api/{}/eevee/apikey/upload/".format(self.url, self.version)
        headers = {"apikey": self.apikey}

        correct_response = []
        error_response = []
        error_codes = [400, 401, 409]

        if user_doc_ids:
            if not len(file_paths) == len(user_doc_ids):
                raise LengthNotMatched(
                    "Length of File Path and Length of User Doc Id not Equal."
                )
        else:
            user_doc_id = ["" for i in range(len(file_paths))]

        for i in range(len(file_paths)):

            filename = os.path.basename(file_paths[i])

            multipart_form_data = {
                "files": (filename, open(file_paths[i], "rb")),
                "type": (None, doc_type),
                "user_doc_id": (None, user_doc_id[i]),
                "uploaded_from": (None, "api"),
            }

            response = requests.post(url, files=multipart_form_data, headers=headers)

            if response.status_code != 200:

                if response.status_code in error_codes:
                    original_response = response.json()
                    error = {
                        "metadata": {"user_doc_id": user_doc_ids[i], "title": filename},
                        "error": original_response["error"],
                        "message": original_response["message"],
                        "status": "fail",
                        "status_code": original_response["status_code"],
                    }
                    error_response.append(error)

                else:
                    error = {
                        "metadata": {"user_doc_id": user_doc_ids[i], "title": filename},
                        "status": "fail",
                        "status_code": response.status_code,
                    }

            else:
                original_response = response.json()
                correct_response.append(original_response)

        final_response = {
            "files_uploaded": correct_response,
            "files_not_uploaded": error_response,
        }

        return final_response

    def __str__(self):
        return "Docsumo API"

    def __repr__(self):
        return "Docsumo API"
