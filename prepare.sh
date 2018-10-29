#!/bin/bash

script_dir=$(dirname "$0")
"$script_dir"/replace.sh $1
python3 "$script_dir"/parse.py $1
