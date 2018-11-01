#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./prepare.sh maildir"
    exit 1
fi

script_dir=$(dirname "$0")
megadir="$1/../megadir"

echo "Replacing non-1252 characters..."
"$script_dir/replace.sh" "$1"
echo "Parsing files..."
python3 "$script_dir/parse.py" "$1" "$megadir"
echo "Deduplicating..."
fdupes -dN "$megadir"
