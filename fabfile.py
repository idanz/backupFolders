from fabric.api import *
from folders import folders
import os

@task
def sync(default = True):
    for folder in folders:
        sync_folder(folder)
    
def sync_folder(path):
    name = os.path.basename(path)
    # Sync the folder
    local(r'python c:\Python27\Scripts\s3cmd -c s3.cfg sync "{path}/" "s3://idan-backups/{name}/"'.format(**locals()))
    # and delete old files in the folder
    with settings(warn_only = True): # This fails if we have nothing to delete
        local(r'forfiles -p "{path}" -s -m *.* -d -2 -c "cmd /c del @path"'.format(**locals()), )
    