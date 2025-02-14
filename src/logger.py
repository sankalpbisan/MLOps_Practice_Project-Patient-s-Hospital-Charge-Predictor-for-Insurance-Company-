import os
import logging
from datetime import datetime
from src.utils import root_dir

log_file_name=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(root_dir,'logs')
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path,log_file_name)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
