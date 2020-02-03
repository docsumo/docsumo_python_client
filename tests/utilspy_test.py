import os
import unittest

from docsumo import Docsumo


class Testutils(unittest.TestCase):
    def test_upload_file(self):
        r = Docsumo(apikey="")

        file_path = "/home/saugat/Documents/invoice.png"
        user_doc_id = "11001"
        res_1 = r.upload_file(file_path, "Invoice", user_doc_id)

        # get the uploaded file title
        uploaded_file_title = os.path.basename(file_path)

        # assert that we get the response
        self.assertTrue(res_1)

        # test different cases for 'success' and 'fail' status
        if res_1["status"] == "success":
            # assert the length of keys in response
            self.assertEqual(len(res_1.keys()), 6)

            # assert the user_doc_id in response
            self.assertEqual(res_1["data"]["user_doc_id"], user_doc_id)

            # assert the title of document uploaded in response
            self.assertEqual(res_1["data"]["title"], uploaded_file_title)
        else:
            # assert the length of keys in response
            self.assertEqual(len(res_1.keys()), 4)

        # test for the case when user does not provide 'user_doc_id'
        res_2 = r.upload_file("/home/saugat/Documents/invoice.png", "Invoice")

        # assert that we get the response
        self.assertTrue(res_2)

        # test whether the 'doc_id' and 'user_doc_id' are same or not in response when user does not provide 'user_doc_id'
        self.assertEqual(res_2["data"]["doc_id"], res_2["data"]["user_doc_id"])

    def test_upload_files(self):
        r = Docsumo(apikey="")
        file_path = [
            "/home/saugat/Documents/files/invoice.png",
            "/home/saugat/Documents/files/invoice_1.png",
            "/home/saugat/Documents/files/invoice_2.jpg",
        ]
        user_doc_id = ["000000001", "000000002", "0003"]

        # response when user provides the 'user_doc_id'
        res_1 = r.upload_files(file_path, "Invoice", user_doc_id)

        # assert that we get the response
        self.assertTrue(res_1)

        # assert the length of keys in response
        self.assertEqual(len(res_1.keys()), 2)

        uploaded_filetitle = []
        response_filetitle = []

        for i in range(len(file_path)):
            # get the title of every uploaded files
            uploaded_filetitle.append(os.path.basename(file_path[i]))

        # execute only if "files_uploaded" in not empty
        if res_1["files_uploaded"]:
            for i in range(len(res_1["files_uploaded"])):
                # assert the length of keys for 'files_uploaded' key in response
                self.assertEqual(len(res_1["files_uploaded"][i].keys()), 6)

                # get the title of files uploaded, from response
                response_filetitle.append(res_1["files_uploaded"][i]["data"]["title"])

        # execute only if "files_not_uploaded" is not empty
        if res_1["files_not_uploaded"]:
            for i in range(len(res_1["files_not_uploaded"])):
                # assert the length of keys for 'files_not_uploaded' key in response
                self.assertEqual(len(res_1["files_not_uploaded"][i].keys()), 5)

                # get the title of files not uploaded, from response
                response_filetitle.append(
                    res_1["files_not_uploaded"][i]["metadata"]["title"]
                )

        # assert that the response files title are same as the uploaded files title
        self.assertEqual(response_filetitle, uploaded_filetitle)

        # response when user does not provide the 'user_doc_id'
        res_2 = r.upload_files(file_path, "Invoice")

        # assert that we get the response
        self.assertTrue(res_2)

        # assert the length of keys in response
        self.assertEqual(len(res_2.keys()), 2)

        # execute only if "files_uploaded" is not empty
        if res_2["files_uploaded"]:
            for i in range(len(res_2["files_uploaded"])):
                doc_id = res_2["files_uploaded"][i]["data"]["doc_id"]
                user_doc_id = res_2["files_uploaded"][i]["data"]["user_doc_id"]

                # assert that the 'doc_id' and 'user_doc_id' are same when user does not provide 'user_doc_id'
                self.assertEqual(doc_id, user_doc_id)

    def test_limit(self):
        r = Docsumo(apikey="")

        res = r.limit()

        # assert that we get the response
        self.assertTrue(res)

        # assert the length of keys in response
        self.assertEqual(len(res.keys()), 6)

        # assert the length of keys in data key
        self.assertEqual(len(res["data"].keys()), 6)

        for i in range(len(res["data"]["document_types"])):
            # assert that the each elements in document_types list has length 2
            self.assertEqual(len(res["data"]["document_types"][i].keys()), 2)

    def test_documents_list(self):
        r = Docsumo(apikey="")

        res = r.documents_list()

        # assert that we get the response
        self.assertTrue(res)

        # assert the length of keys in response
        self.assertEqual(len(res.keys()), 6)

        # assert the length of keys in data key
        self.assertEqual(len(res["data"].keys()), 4)

        for i in range(len(res["data"]["documents"])):
            # assert that the each elements in document list has length 4
            self.assertEqual(len(res["data"]["documents"][i].keys()), 5)

    def test_documents_summary(self):
        r = Docsumo(apikey="")

        res = r.documents_summary()

        # assert that we get the response
        self.assertTrue(res)

        # assert the length of keys in response
        self.assertEqual(len(res.keys()), 6)

        # assert the length of keys in data key in response
        self.assertEqual(len(res["data"].keys()), 4)

    def test_document_data(self):
        r = Docsumo(apikey="")

        res = r.document_data("10d909859ef047d0bbe0de2e279486fc")

        # assert that we get the response
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
