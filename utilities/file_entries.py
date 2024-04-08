# %%
from utilities.common import * 
# dirname = "D:/data/eroi"
from datetime import datetime 

def fetch_file_entries(dirname): 

  glob = fullpath(dirname).glob("*.*")
  files = [x for x in glob]

  def get_entries(file):
    d = dotdict()
    d.name = file.name 
    d.parent = file.parent 
    d.extname = file.suffix
    d.is_dir = file.is_dir()
    stat = file.stat()
    d.size = stat.st_size
    d.mtime = datetime.fromtimestamp(stat.st_mtime)
    d.ctime = datetime.fromtimestamp(stat.st_ctime)
    d.atime = datetime.fromtimestamp(stat.st_atime)
    return d
  entries = sorted([get_entries(x) for x in files], key=lambda x: x.mtime, reverse=True)
  return entries


