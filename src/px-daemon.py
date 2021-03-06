#!/usr/bin/python

from __init__ import *
from settings import *
from os import mkdir

def check_dirs():
  for d in [etc_folder, bin_folder, backup_folder, providers_folder]:
    if not path.isdir(d):
      logging.info('made directory: '+str(d))
      mkdir(d)

if __name__ == '__main__':
  check_dirs()
  pxf = ProxyFrame(settings.database, settings.threads)
  try:
    pxf.start()
  except KeyboardInterrupt:
    pxf.shutdown()
  
    