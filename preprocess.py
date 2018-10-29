#!/usr/bin/python3

import codecs
import os
import pickle
import re
import sys

MEGADIR = "megadir"


def main():
    os.makedirs(MEGADIR, exist_ok=True)

    head_body_regex = re.compile(r"^(.*?\r\n\r\n)(.*)", flags=re.S)
    key_val_regex = re.compile(r"^(.*?): (.*)$", flags=re.MULTILINE)

    root = sys.argv[1]
    for dirname, _, files in os.walk(root):
        for filename in files:
            path = os.path.join(dirname, filename)
            try:
                with codecs.open(path, 'r', 'cp1252') as f:
                    string = f.read()
                    head_body_match = head_body_regex.match(string)
                    head_string = head_body_match.group(1).replace('\r', '')
                    body_string = head_body_match.group(2).replace('\r', '')

                    data_dict = dict(key_val_regex.findall(head_string))
                    data_dict['Body'] = body_string
                    del data_dict['Message-ID']
                    del data_dict['X-Folder']
                    del data_dict['X-FileName']
                    del data_dict['X-Origin']

                new_path = os.path.join(MEGADIR, path.replace('/', '-'))
                with open(new_path, 'wb') as f:
                    pickle.dump(data_dict, f)
            except Exception as e:
                print(f'Error in {path}: {str(e)}')


if __name__ == "__main__":
    main()
