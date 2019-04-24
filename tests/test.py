from docsumo import Docsumo
from loguru import logger

# r = Docsumo(apikey="Trt7Rukb9BZ5rFsO1s7zlGFlVPJRDZCJr0cByjfiK8jqjSLyQjpgd4ze2jOI")
r = Docsumo(
    url="https://app.docsumo.com/",
    apikey="7x0Ntk0eu4AHobsBVlmT14tprikLTThdyTVqrG9h2JlhUFsqlw9ZJ8CIFOSZ",
)

# logger.info(r.user_detail_credit_limit())
# logger.info(r.documents_list())
# logger.info(r.documents_list())
# logger.info(r.documents_summary())
# logger.info(
#     r.upload_file(
#         "/Users/bikramdahal/Downloads/drip capital/Invoice_2009.pdf",
#         "invoice_financing",
#     )
# )
logger.info(r.extracted_data("c511ba245484442fb097901548c126c6"))
