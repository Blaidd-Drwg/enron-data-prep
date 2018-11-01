import sys
import re
import os
import codecs
import glob
import pickle

subject_regex = re.compile(r"^>\sSubject:\s+(.*)$(.*)$",flags=re.MULTILINE)

from_regex = re.compile(r"^>\sFrom:.*?(\w+)@", flags=re.MULTILINE)
from_regex2 = re.compile(r"^>\sFrom:\s\w+\s(\w+)", flags=re.MULTILINE)
from_regex3 = re.compile(r"^>\sFrom:\s(\w+),?", flags=re.MULTILINE)

to_regex = re.compile(r"^>\sTo:.*?(\w+)@", flags=re.MULTILINE)
to_regex2 = re.compile(r"^>\sTo:\s\w+\s(\w+)", flags=re.MULTILINE)
to_regex3 = re.compile(r"^>\sTo:\s(\w+),?", flags=re.MULTILINE)

reply_body_regex = re.compile(r".*?>\n>(.*?)\n\n", flags=re.MULTILINE|re.S)

root = sys.argv[1]
for dirname, _, files in os.walk(root):
    print(dirname)
    for filename in files:
        path = os.path.join(dirname, filename)
        try:
            with codecs.open(path, 'r',"cp1252") as f:
                string = f.read()
                dictionary_actual = pickle.load(f)

                potential_mail_places = list()

                subject_regex_match = subject_regex.search(string)
                if subject_regex_match:
                    print(filename)
                    if subject_regex_match.group(2):
                        subject = subject_regex_match.group(1) + " " + subject_regex_match.group(2)
                    else:
                        subject = subject_regex_match.group(1)
                    print(subject)

                from_regex_match = from_regex.search(string)
                from_regex2_match = from_regex2.search(string)
                from_regex3_match = from_regex3.search(string)

                if from_regex_match:
                    from1 = from_regex_match.group(1)
                    print("From:"+from1)
                    senders = glob.glob('../megadir/'+from1+'*.txt')
                    potential_mail_places = senders

                elif from_regex2_match:
                    from1 = from_regex2_match.group(1)
                    print("From:"+from1)
                    senders = glob.glob('../megadir/'+from1+'*.txt')
                    potential_mail_places = senders

                elif from_regex3_match:
                    from1 = from_regex3_match.group(1)
                    print("From:"+from1)
                    senders = glob.glob('../megadir/'+from1+'*.txt')
                    potential_mail_places = senders

                to_regex_match = to_regex.search(string)
                to_regex2_match = to_regex2.search(string)
                to_regex3_match = to_regex3.search(string)

                if to_regex_match:
                    to1 = to_regex_match.group(1)
                    print("To:"+to1)
                    receivers = glob.glob('../megadir/'+to1+'*.txt')
                    potential_mail_places = potential_mail_places + receivers

                elif to_regex2_match:
                    to1 = to_regex2_match.group(1)
                    print("To:"+to1)
                    receivers = glob.glob('../megadir/'+to1+'*.txt')
                    potential_mail_places = potential_mail_places + receivers

                elif to_regex3_match:
                    to1 = to_regex3_match.group(1)
                    print("To:"+to1)
                    receivers = glob.glob('../megadir/'+to1+'*.txt')
                    potential_mail_places = potential_mail_places + receivers

                reply_body_regex_match = reply_body_regex.search(string)
                if reply_body_regex_match:
                    reply_body = reply_body_regex_match.group(1)

                for file in potential_mail_places:
                    path = os.path.join(dirname, filename)
                        with codecs.open(path, 'r',"cp1252") as compare:
                            string = compare.read()
                            dictionary_compare = pickle.load(compare)
                            if reply_body==dictionary_compare["Body"]:
                                print("MATCH in: " + file)
                                dictionary_actual["repliedTo"] = file




        except Exception as e:
            print(e)
