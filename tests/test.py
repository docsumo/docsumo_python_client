from docsumo import Docsumo
from loguru import logger
# r = Docsumo(apikey="Trt7Rukb9BZ5rFsO1s7zlGFlVPJRDZCJr0cByjfiK8jqjSLyQjpgd4ze2jOI")

r = Docsumo(apikey="enmYrHxKhAu3EttfofbE6xnYOKRRL18W9OrfRucXQXNJowRn6bmL9jzTFTJ8",url='https://apptesting.docsumo.com')
# r = Docsumo()

logger.info(r.limit())
logger.info(r.documents_list())
logger.info(r.documents_summary())
logger.info(r.upload_file('/home/saugat/Documents/invoice.png', 'Invoice', '32232'))
logger.info(r.upload_files(['/home/saugat/Documents/files/invoice.png',
                            '/home/saugat/Documents/files/invoice_1.png',
                            '/home/saugat/Documents/files/invoice_2.jpg'],
                            'Invoice'),
                            ['123', '345', '456'])
logger.info(r.document_data('0f120dfc790248558a22fe7a1e0d9c25'))