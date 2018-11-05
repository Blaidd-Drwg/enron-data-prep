import sys
import re
import os
import codecs
import glob
import pickle
from tqdm import tqdm


subject_regex = re.compile(r"^>\sSubject:\s+(.*)$(.*)$",flags=re.MULTILINE)

from_regex = re.compile(r"^>\sFrom:.*?(\w+)@", flags=re.MULTILINE)
from_regex2 = re.compile(r"^>\sFrom:\s\w+\s(\w+)", flags=re.MULTILINE)
from_regex3 = re.compile(r"^>\sFrom:\s(\w+),?", flags=re.MULTILINE)

to_regex = re.compile(r"^>\sTo:.*?(\w+)@", flags=re.MULTILINE)
to_regex2 = re.compile(r"^>\sTo:\s\w+\s(\w+)", flags=re.MULTILINE)
to_regex3 = re.compile(r"^>\sTo:\s(\w+),?", flags=re.MULTILINE)

reply_body_regex = re.compile(r".*?>\n>(.*)", flags=re.MULTILINE|re.S)

root = sys.argv[1]
numberOfFiles = next(os.walk(root))[2]
for dirname, _, files in os.walk(root):
    for filename in tqdm(files):
        path = os.path.join(dirname, filename)
        with open(path, 'rb') as f:
            dictionary_actual = pickle.load(f)
            body = dictionary_actual["Body"]
            print(body)

            potential_mail_places = list()

            subject_regex_match = subject_regex.search(body)
            if subject_regex_match:
                if subject_regex_match.group(2):
                    subject = subject_regex_match.group(1) + " " + subject_regex_match.group(2)
                else:
                    subject = subject_regex_match.group(1)

            from_regex_match = from_regex.search(body)
            from_regex2_match = from_regex2.search(body)
            from_regex3_match = from_regex3.search(body)

            if from_regex_match:
                from1 = from_regex_match.group(1)
                senders = glob.glob('megadir/'+'*'+from1+'*.txt')
                potential_mail_places.extend(senders)

            elif from_regex2_match:
                from1 = from_regex2_match.group(1)
                senders = glob.glob('megadir/'+'*'+from1+'*.txt')
                potential_mail_places.extend(senders)

            elif from_regex3_match:
                from1 = from_regex3_match.group(1)
                senders = glob.glob('megadir/'+'*'+from1+'*.txt')
                potential_mail_places.extend(senders)

            to_regex_match = to_regex.search(body)
            to_regex2_match = to_regex2.search(body)
            to_regex3_match = to_regex3.search(body)

            if to_regex_match:
                to1 = to_regex_match.group(1)
                receivers = glob.glob('megadir/'+'*'+to1+'*.txt')
                potential_mail_places.extend(receivers)

            elif to_regex2_match:
                to1 = to_regex2_match.group(1)
                receivers = glob.glob('megadir/'+'*'+to1+'*.txt')
                potential_mail_places.extend(receivers)

            elif to_regex3_match:
                to1 = to_regex3_match.group(1)
                receivers = glob.glob('megadir/'+'*'+to1+'*.txt')
                potential_mail_places.extend(receivers)

            reply_body_regex_match = reply_body_regex.search(body)
            if reply_body_regex_match:
                reply_body = reply_body_regex_match.group(1)
                reply_body = reply_body.replace("> ","")
                for file in potential_mail_places:
                    #print(file)
                    path = os.path.abspath(str(file))
                    with open(path, 'rb') as compare:
                        dictionary_compare = pickle.load(compare)
                        compare_body = dictionary_compare["Body"]
                        #print (compare_body)
                        #print (reply_body)
                        if reply_body==dictionary_compare["Body"]:
                            print(filename + " replies to: " + file)
                            dictionary_actual["repliedTo"] = file

            
