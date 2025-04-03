import psutil
import subprocess
import logging 
from rich.logging import RichHandler
from concurrent.futures import ThreadPoolExecutor
import time
import config

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])

def find_mount_point(device):
    """Check if a device is already mounted and return its mount point."""
    for partition in psutil.disk_partitions():
        if partition.device == device: return partition.mountpoint
    return None

def bidirectional_sync(src: str, dest: str) -> None:
    """Sync src → dest using rsync"""
    subprocess.run(['unison', src, dest, '-auto', '-batch'], check = True)

def sync_loop(src, dest):
    while True: 
        bidirectional_sync(src, dest)
        time.sleep(config.refresh_period)
        
def mount_device(): 
     # Check if the device is already mounted
    mounted_at = find_mount_point(config.device)

    if mounted_at:
        logging.info(f"✅ {config.device} is already mounted at {mounted_at}")
    else:
        logging.info(f"🔄 {config.device} is not mounted. Mounting now...")
        # Create mount point if it doesn't exist
        subprocess.run(["sudo", "mkdir", "-p", config.mount_point], check=True)

        # Mount the device
        subprocess.run(["sudo", "mount", config.device, config.mount_point], check=True)
        print(f"{config.device} mounted at {config.mount_point}")

def preprocess_path(): 
    config.src_dicts = list(config.dict_sync_mapper.keys())
    config.dist_dicts = [value for _, value in config.dict_sync_mapper.values()]

def test(): 
    config.device = 'test'
    
if __name__ == '__main__': 
    import os
    logging.info(os.getlogin())