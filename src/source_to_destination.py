import os 
import shutil
source = "/Users/kazikgarstecki/Desktop/workspace/github.com/kazgar/static_site_generator/static"
destination = "/Users/kazikgarstecki/Desktop/workspace/github.com/kazgar/static_site_generator/public2"


def copy_src_to_destination(source, destination):
    if not os.path.exists(source) or not os.path.exists(destination):
        raise ValueError("Invalid source or destination path")
    
    shutil.rmtree(destination)


    
copy_src_to_destination(source, destination)
