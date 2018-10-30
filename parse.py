#!/usr/bin/python3

import codecs
import os
import pickle
import re
import sys


def main():
    if len(sys.argv) != 3:
        print('Usage: parse.py maildir megadir')
        exit(1)

    root = sys.argv[1]
    megadir = sys.argv[2]
    os.makedirs(megadir, exist_ok=True)

    head_body_regex = re.compile(r"^(.*?\r\n\r\n)(.*)", flags=re.S)
    key_val_regex = re.compile(r"(^|(?<=\r\n))(\S.*?): (.*)\r\n")

    for dirname, _, files in os.walk(root):
        for filename in files:
            path = os.path.join(dirname, filename)
            try:
                with codecs.open(path, 'r', 'cp1252') as f:
                    string = f.read()

                head_body_match = head_body_regex.match(string)
                head_string = head_body_match.group(1)
                body_string = head_body_match.group(2).replace('\r', '')

                data_dict = {k: v for _, k, v in key_val_regex.findall(head_string)}
                if not data_dict:
                    print(f"Error in {path}: couldn't parse metadata")

                data_dict['Body'] = body_string
                del data_dict['Message-ID']
                del data_dict['X-Folder']
                del data_dict['X-FileName']
                del data_dict['X-Origin']

                new_path = os.path.join(megadir, path.replace('/', '-'))
                with open(new_path, 'wb') as f:
                    pickle.dump(data_dict, f)
            except Exception as e:
                print(f'Error in {path}: {str(e)}')


if __name__ == "__main__":
    main()
