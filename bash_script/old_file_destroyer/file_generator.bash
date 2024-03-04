#!/bin/bash
#The script uses the dd utility to create fixed-length files.
filename=empty
dir_size=0
directory=$1
cd "$directory" || exit
dir_size=$(du -m "$directory" | awk '{print $1}')
while [ "$dir_size" -le 100 ]
    do
        filename=$(date +"%FT%H%M%S").bag
        sleep 2
        dd if=/dev/zero of="$filename" bs=1M count=10 &> /dev/null
        if [ "$dir_size" -ge 50 ]
            then
            touch -d "2 days ago" "$filename"
        fi
        dir_size=$(du -m "$directory" | awk '{print $1}')
    done



