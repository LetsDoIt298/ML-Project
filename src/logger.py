# Logger file is used to keep track of what all excetion has happend

import logging
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Current working directory + "logs" + LOG_File
logs_path= os.path.join(os.getcwd(), "logs",LOG_FILE)
#Keep on appendting data when exist_ok=True
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
    
)

if __name__=="__main__":
    logging.info("Logging has started")