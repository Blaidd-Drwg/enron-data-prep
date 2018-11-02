import sys
import os
import re
import pickle
from tqdm import tqdm

X_KEYS = [("To", "X-To"), ("Cc", "X-cc"), ("Bcc", "X-bcc")]
name_str = "[A-Z][a-z]+(-[A-Z][a-z]+)?"
double_name_str = f"{name_str} ({name_str}|[A-Z]\.?)"
surname_str = f"{name_str}(,? [JS]r\.?)?"

double_name_regex = re.compile(f"({double_name_str} {surname_str}|{surname_str}, {double_name_str})$")
full_name_regex = re.compile(f"({name_str} {surname_str}|{surname_str}, {name_str})$")
simple_name_regex = re.compile(f"{name_str}$")

def choose_best_name(name_map):
    chosen_names = {}
    for address, names in name_map.items():
        for name in names:
            if double_name_regex.match(name):
                names[name] *= 1.4
            elif full_name_regex.match(name):
                names[name] *= 1.3
            elif simple_name_regex.match(name):
                names[name] *= 1.1
        chosen_names[address] = max(names, key=names.get)
    return chosen_names

def cleanup_names(chosen_names):
    for address in chosen_names:
        name = chosen_names[address]
        if not name: continue

        if name[0] == '"' and name[-1] == '"':
            name = name[1:-1]
        if name[0] == "'" and name[-1] == "'":
            name = name[1:-1]

        split_name = name.split(',', 1)
        if len(split_name) > 1 and not re.match(" [JS]r\.?", split_name[0]):
            name = f"{split_name[1]} {split_name[0]}".strip()

        # if chosen_names[address] != name:
            # print(name)
        chosen_names[address] = name
    return chosen_names

def main():
    dirname = sys.argv[1]
    name_map = {}

    for filename in tqdm(os.listdir(dirname)):
        path = os.path.join(dirname, filename)
        with open(path, 'rb') as f:
            data_dict = pickle.load(f)

        for key, x_key in X_KEYS:
            if key in data_dict:
                for address, name in zip(data_dict[key], data_dict[x_key]):
                    if address in name_map:
                        if name in name_map[address]:
                            name_map[address][name] += 1
                        else:
                            name_map[address][name] = 1
                    else:
                        name_map[address] = {name: 1}

    # p_chosen_names = {address: max(names, key=names.get) for address, names in name_map.items()}
    chosen_names = choose_best_name(name_map)

    # for address in chosen_names:
        # if chosen_names[address] != p_chosen_names[address]:
            # print(f"{address}: {chosen_names[address]} instead of {p_chosen_names[address]}")

    chosen_names = cleanup_names(chosen_names)
    # for address in chosen_names:
        # print(f"{address}: {chosen_names[address]}")

if __name__ == '__main__':
    main()
