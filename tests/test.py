from docsumo import Docsumo
from loguru import logger

# r = Docsumo(apikey="Trt7Rukb9BZ5rFsO1s7zlGFlVPJRDZCJr0cByjfiK8jqjSLyQjpgd4ze2jOI")
r = Docsumo(
    url="https://apptesting.docsumo.com/",
    apikey="BUxTWOgrcn0t4qEAC3R90sPoJ60H58gcZIo3zxrOH8HnQQJTYWsir6komyrW",
)

logger.info(r.user_detail_credit_limit())
logger.info(r.documents_list())
logger.info(r.documents_list(created_date_less_than="2019-04-31"))
logger.info(r.documents_summary())
logger.info(
    r.upload_file(
        "/Users/bikramdahal/Downloads/268ef58b74f144b48e34ffdeae8e0f9b_image.jpg",
        "invoice_financing",
    )
)
logger.info(r.extracted_data("baac29ccec774679825373b09051e8c2"))
