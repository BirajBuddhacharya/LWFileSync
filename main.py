import logging
from rich.logging import RichHandler
import config
from concurrent.futures import ThreadPoolExecutor
from utils import mount_device, src_dicts, dist_dicts, sync_loop, test

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])

def main(): 
   # mounting device 
   mount_device()
   
   # syncing file 
   with ThreadPoolExecutor(max_workers=10) as executor: 
       executor.map(sync_loop, src_dicts, dist_dicts)

if __name__ == '__main__': 
    logging.info(config.device)
    test()
    logging.info(config.device)
    