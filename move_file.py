import os

src_path = os.path.dirname("./001/hw6/")
dst_path = os.path.dirname("./001/HW/")

for filename in os.listdir(src_path):
    elems = filename.split("_")
    newname = '_'.join([elems[-2], elems[-1]])
    newpath = dst_path + "/" + elems[0] + "/"
    try:
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.rename(src_path + "/" + filename, newpath + newname)
    except OSError:
        print('Error: Creating directory. ' + directory)
