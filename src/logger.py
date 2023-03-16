import logging 
import os 
from datetime import datetime



LOG_File=f"{datetime.now().strftime('%m_%d_Y_%H_%M_%S')}.log"


logs_path=os.path.join(os.getcwd(),"logs",LOG_File)


os.makedirs(logs_path,exist_ok=True) 

lOG_FILE_PATH=os.path.join(logs_path,LOG_File)
logging.basicConfig(

filename=lOG_FILE_PATH,

format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,

)
if __name__=="__main__":
    logging.info("logging startted")

    