#!/bin/bash

script_dir=$(dirname "$0")
megadir="$1/megadir"

"$script_dir/replace.sh" "$1"
python3 "$script_dir/parse.py" "$1" "$megadir"
fdupes -dN "$megadir"
