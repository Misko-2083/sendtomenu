#!/usr/bin/env python3

from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject
import os
import sys
import shutil
import errno
import threading
import time



def app_main():
    win = Gtk.Window()

    win.set_name("Send To")
    win.set_border_width(10)
    win.set_title('Send To')

    vbox = Gtk.Box()

    progressbar = Gtk.ProgressBar()
    vbox.add(progressbar)

    button = Gtk.Button("Cancel")
    button.connect("clicked", Gtk.main_quit)
    vbox.add(button)
    win.connect("delete-event", Gtk.main_quit)
    win.add(vbox)

    def get_input():
        src = ""
        path = ""
        list = ""

        INPUT = sys.stdin
        print("Waiting for input...")
        line_num = 1
        for line in INPUT:
            if line_num == 1:
               src = line.rstrip('\n')
            elif line_num == 2:
               path = line.rstrip('\n')
            elif line_num == 3:
               list = line.rstrip('\n')
            else:
               print("Too many arguments passed. Exiting...")
               Gtk.main_quit()
            line_num += 1
        if src == "":
            print("Source argument is missing. Exiting...")
            Gtk.main_quit()
        if path == "":
            print("Destination argument is missing. Exiting...")
            Gtk.main_quit()
        if list == "":
            print("List file is argument is missing. Exiting...")
            Gtk.main_quit()
        return src, path, list

    def read_file(file):
        f = open(file)
        content = [x.strip() for x in f.readlines()]
        f.close()
        return content

    def rename(file, path, num=1):
        (file_prefix, exstension) = os.path.splitext(file)
        renamed = "%s(%d)%s" % (file_prefix, num, exstension)
        if os.path.exists(path + renamed):
            renamed = "%s(%d)%s" % (file_prefix, num + 1, exstension)
            return renamed
        else:
            return renamed

    def update_progress(text):
        progressbar.pulse()
        progressbar.set_text(text)
        progressbar.set_show_text(True)
        return False

    def copy_files():
        (src, path, list) = get_input()
        list = read_file(list)
        GLib.idle_add(win.show_all)
        for files in list:
            src_file_path = src + files
            dst_file_path = path + files
            if os.path.exists(dst_file_path):
                new_file_name =  rename(files, path)
                dst_file_path = path + new_file_name
            text = "Copying: " + dst_file_path
            GLib.idle_add(update_progress, text)
            time.sleep(0.2)
            try:
                shutil.copytree(src_file_path,dst_file_path,
                                symlinks=False, ignore=None, copy_function=shutil.copy2,
                                ignore_dangling_symlinks=False)
            except OSError as e:
                if e.errno == errno.ENOTDIR:
                    shutil.copy2(src_file_path,dst_file_path,follow_symlinks=True)
                else:
                    print('Directory not copied. Error: %s' % e)

    thread = threading.Thread(target=copy_files)
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
     GObject.threads_init()

     app_main()
     Gtk.main()