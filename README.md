## Send To
A Stand-alone Send To Gtk3 menu for the Thunar Custom Action    
  Setting thunar custom action:    
  Name: Send to    
  Description : Copy file(s) and folder(s) to...    
  Command: ```tempfile=$(mktemp /tmp/XXXXX); for file in %F; do echo "${file##*/}" >> $tempfile; done; python3 /usr/local/bin/menu.py %d/ $tempfile```   
  File Pattern: *    
  Appearance: *    

## Author
* Miloš Pavlović

## Depends
* python3-gi

## License ![License](https://img.shields.io/badge/license-GPLv3-green.svg)

This project is under the GPLv3 license. Unless otherwise stated in individual files