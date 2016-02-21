import os
import sys
import shutil
import errno

def rename(file_name, path, num=1):
    (file_prefix, exstension) = os.path.splitext(file_name)
    renamed = "%s(%d)%s" % (file_prefix, num, exstension)
    if os.path.exists(path + renamed):
        renamed = "%s(%d)%s" % (file_prefix, num + 1, exstension)
        return renamed
    else:
        return renamed

def copy_files(src, path, file_with_list):
    for files in file_with_list:
        src_file_path = src + files
        dst_file_path = path + files
        if os.path.exists(dst_file_path):
            new_file_name =  rename(files, path)
            dst_file_path = path + new_file_name

        print("Copying: " + dst_file_path)
        try:
            shutil.copytree(src_file_path,dst_file_path)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copyfile(src_file_path,dst_file_path)
            else:
                print('Directory not copied. Error: %s' % e)
 

def read_file(file_name):
    f = open(file_name)
    #reads each line of file (f), strips out extra whitespace and 
    #returns list with each line of the file being an element of the list
    content = [x.strip() for x in f.readlines()]
    f.close()
    return content

src = sys.argv[1]
path = sys.argv[2]
file_with_list = sys.argv[3]

copy_files(src,path,read_file(file_with_list))

os.remove(file_with_list)