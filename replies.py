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
    for filename in files:
        path = os.path.join(dirname, filename)
        with open(path, 'rb') as f:
            dictionary_actual = pickle.load(f)
            body = dictionary_actual["Body"]

            potential_mail_places = list()

            subject_regex_match = subject_regex.search(body)
            if subject_regex_match:
                print(filename)
                if subject_regex_match.group(2):
                    subject = subject_regex_match.group(1) + " " + subject_regex_match.group(2)
                else:
                    subject = subject_regex_match.group(1)
                print(subject)

            from_regex_match = from_regex.search(body)
            from_regex2_match = from_regex2.search(body)
            from_regex3_match = from_regex3.search(body)

            if from_regex_match:
                from1 = from_regex_match.group(1)
                print("From:"+from1)
                senders = glob.glob('../megadir/'+from1+'*.txt')
                potential_mail_places.append(senders)

            elif from_regex2_match:
                from1 = from_regex2_match.group(1)
                print("From:"+from1)
                senders = glob.glob('../megadir/'+from1+'*.txt')
                potential_mail_places.append(senders)

            elif from_regex3_match:
                from1 = from_regex3_match.group(1)
                print("From:"+from1)
                senders = glob.glob('../megadir/'+from1+'*.txt')
                potential_mail_places.append(senders)

            to_regex_match = to_regex.search(body)
            to_regex2_match = to_regex2.search(body)
            to_regex3_match = to_regex3.search(body)

            if to_regex_match:
                to1 = to_regex_match.group(1)
                print("To:"+to1)
                receivers = glob.glob('../megadir/'+to1+'*.txt')
                potential_mail_places.append(receivers)

            elif to_regex2_match:
                to1 = to_regex2_match.group(1)
                print("To:"+to1)
                receivers = glob.glob('../megadir/'+to1+'*.txt')
                potential_mail_places.append(receivers)

            elif to_regex3_match:
                to1 = to_regex3_match.group(1)
                print("To:"+to1)
                receivers = glob.glob('../megadir/'+to1+'*.txt')
                potential_mail_places.append(receivers)

            reply_body_regex_match = reply_body_regex.search(body)
            if reply_body_regex_match:
                reply_body = reply_body_regex_match.group(1)
                reply_body.replace("^>\s(?!>)","")

            for file in potential_mail_places:
                path = os.path.join(dirname, filename)
                print(path)
                with open(path, 'rb') as compare:
                    dictionary_compare = pickle.load(compare)
                    if reply_body==dictionary_compare["Body"]:
                        print("MATCH in: " + file)
                        dictionary_actual["repliedTo"] = file
