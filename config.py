device = "/dev/nvme0n1p3"  # Change this to your partition
mount_point = "/mnt/WindowsDrive"  # Preferred mount point
refresh_period = 5 # time before each sync
dict_sync_mapper = {
    '/home/otakugod/Desktop': '/Users/admin',
}
src_dicts = None # will be configured in run time
dist_dicts = None # will be configured in run time 