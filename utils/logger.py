import logging
import datetime

log_file = "report/LOG_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".log"
log_file_level = "INFO"
log_file_format = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
log_file_date_format = "%H:%M:%S %d-%m-%Y"

logging.basicConfig(filename=log_file, level=log_file_level, format=log_file_format, datefmt=log_file_date_format)
LOGGER = logging.getLogger(__name__)
