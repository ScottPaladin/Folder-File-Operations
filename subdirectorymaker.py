import os, shutil

WORKDIR = "pathname"
DESTDIR = "pathname"

def make_subdirectories(PATH):
    print("Working on directory: %s" % PATH)
    list = os.listdir(PATH)
    print("Path Listed")
    for FILE in list:
          temp_string = os.path.splitext(os.path.basename(FILE))[0]
          print("Filename: %s" % temp_string)
          temp_list = temp_string.split('-', 1)
          first_seg = temp_list[0]
          first_seg = first_seg.rstrip()
          print(first_seg)
          seglength = len(first_seg)
          print(seglength)
          if seglength > 50:
              print("Trimming")
              first_seg = first_seg[:50]
              first_seg = first_seg.rstrip()
              print(first_seg)
          temp_dir = os.path.join(DESTDIR, first_seg)
          print("Target Directory: %s" % temp_dir)
          if os.path.exists(temp_dir):
              print("yes")
          else:
            os.makedirs(temp_dir)
          if os.path.exists(temp_dir):
              print(FILE)
              src = os.path.join(WORKDIR, FILE)
              print(src)
              dst = os.path.join(temp_dir, FILE)
              print(len(dst))
              print(dst)
              shutil.move(src, dst)
              



make_subdirectories(WORKDIR)
