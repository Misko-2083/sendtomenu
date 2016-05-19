## Send To
A Stand-alone Send To Gtk3 menu for the Thunar Custom Action    
  Setting thunar custom action:    
  Name: Send to    
  Description : Copy file(s) and folder(s) to...    
  Command: ```tempfile=$(mktemp /tmp/XXXXX); for file in %F; do echo "${file##*/}" >> $tempfile; done; python3 /usr/local/bin/menu.py %d/ $tempfile | python3 /usr/local/bin/docp.py; rm -f $tempfile```   
  File Pattern: *    
  Appearance: *    

## Author
* Miloš Pavlović

## Depends
* python3-gi dh-python

## Testing
* To test this in a terminal, create a test file with a list of files to be copied and use this command
```python3 /usr/local/bin/menu.py /working/dir/ /working/dir/list_file | python3 /usr/local/bin/docp.py```

## License ![License](https://img.shields.io/badge/license-GPLv3-green.svg)

This project is under the GPLv3 license. Unless otherwise stated in individual files