import sys
import re
import os

subject_regex = re.compile(r"^>\s>\sSubject:\s(.*)$",flags=re.MULTILINE)
from_regex = re.compile(r"^>\s>\sFrom:\s(\w+),", flags=re.MULTILINE)#arnold, john
from_regex2 = re.compile(r"^>\s>\sFrom:\s\w+\s(\w+)", flags=re.MULTILINE)#john arnold
to_regex = re.compile(r"^>\s>\sTo:\s(\w+),", flags=re.MULTILINE) #arnold, john
to_regex2 = re.compile(r"^>\s>\sTo:\s\w+\s(\w+)", flags=re.MULTILINE) #john arnold

root = sys.argv[1]
for dirname, _, files in os.walk(root):
    for filename in files:
        path = os.path.join(dirname, filename)
        try:
            with open(path, 'r') as f:
                string = f.read()

                subject_regex_match = subject_regex.search(string)
                if subject_regex_match:
                    print(subject_regex_match.group(1))

                from_regex_match = from_regex.search(string)
                from_regex2_match = from_regex2.search(string)

                if from_regex_match:
                    from1 = from_regex_match.group(1)
                    print(filename)
                    print("From:"+from1)

                elif from_regex2_match:
                    from1 = from_regex2_match.group(1)
                    print("From:"+from1)

                to_regex_match = to_regex.search(string)
                to_regex2_match = to_regex2.search(string)

                if to_regex_match:
                    to1 = to_regex_match.group(1)
                    print(filename)
                    print("To:"+to1)

                elif to_regex2_match:
                    to1 = to_regex2_match.group(1)
                    print("To:"+to1)

        except Exception as e:
            print(e)
