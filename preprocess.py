#!/usr/bin/python3

import sys
import os
import re

MEGADIR = "megadir"

def main():
    regex = re.compile(r"^Message-ID:.*$", flags=re.MULTILINE)
    regex2 = re.compile(r"^X-Folder:.*$", flags=re.MULTILINE)
    regex3 = re.compile(r"^X-FileName:.*$", flags=re.MULTILINE)
    regex4 = re.compile(r"^X-Origin:.*$", flags=re.MULTILINE)

    root = sys.argv[1]
    for dirname, _, files in os.walk(root):
        for path in [os.path.join(dirname, filename) for filename in files]:
            string = ""
            try:
                with open(path, 'r') as f:
                    string = f.read()
                    string = regex.sub("", string)
                    string = regex2.sub("", string)
                    string = regex3.sub("", string)
                    string = regex4.sub("", string)

                new_path = os.path.join(MEGADIR, path.replace('/', '-'))
                with open(new_path, 'w') as f:
                    f.write(string)
            except:
                print(path)

if __name__ == "__main__":
    main()
