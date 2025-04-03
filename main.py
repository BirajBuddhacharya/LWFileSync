import logging
from rich.logging import RichHandler
import config
from concurrent.futures import ThreadPoolExecutor
from utils import mount_device, sync_loop, preprocess_path

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])

def main(): 
   # mounting device 
   mount_device()
   
   # preprocessing dict path
   preprocess_path()
   
   # syncing file 
   with ThreadPoolExecutor(max_workers=10) as executor: 
       executor.map(sync_loop, config.src_dicts, config.dist_dicts)

if __name__ == '__main__': 
    pass
    