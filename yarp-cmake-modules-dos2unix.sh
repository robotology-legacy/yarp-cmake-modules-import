#!/bin/sh

if [ -d keep ]; then
    for file in `find keep -type f`; do
        echo dos2unix $file
    done
fi