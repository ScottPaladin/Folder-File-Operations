import os, shutil

WORKDIR = "pathname"
DESTDIR = "pathname"

def flatten_subdirectories(PATH):
    print("Working on directory: %s" % PATH)
    list = os.listdir(PATH)
    print("Path Listed")
    for DIRCAN in list:
          temp_string = os.path.join(WORKDIR, DIRCAN)
          print(": %s" % temp_string)
          if os.path.isdir(temp_string):
              print("Getting Filecount: %s" % temp_string)
              filelist = os.listdir(temp_string)
              for file in filelist:     
                  if file.endswith(".txt"):
                      filelist.remove(file)
                  if file.endswith(".php"):
                      filelist.remove(file)
              filecount = len(filelist)
              print(filecount)
              if filecount < 3:
                  for FILE in filelist:
                      src = os.path.join(WORKDIR, DIRCAN, FILE)
                      print("SRC: %s" % src)
                      afile = DIRCAN+FILE
                      dst = os.path.join(DESTDIR, afile)
                      print("DST: %s" % dst)
                      shutil.move(src, dst)
##              if filecount == 0:
##                  os.remove(temp_string)
              
flatten_subdirectories(WORKDIR)
