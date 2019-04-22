from docsumo import Docsumo
from loguru import logger
# r = Docsumo(apikey="Trt7Rukb9BZ5rFsO1s7zlGFlVPJRDZCJr0cByjfiK8jqjSLyQjpgd4ze2jOI")
r = Docsumo()

logger.info(r.limit())
logger.info(r.documents_list())
logger.info(r.documents_summary())
logger.info(r.upload_file('/Users/bikramdahal/Downloads/268ef58b74f144b48e34ffdeae8e0f9b_image.jpg', 'invoice'))
logger.info(r.document_data('0f120dfc790248558a22fe7a1e0d9c25'))