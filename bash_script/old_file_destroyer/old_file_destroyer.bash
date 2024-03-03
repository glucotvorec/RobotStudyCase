#!/bin/bash
#The script checks the specified directory for the occupied space and if it is greater than a threshold value, deletes .bag files older than 7 days.

#diretory for monitoring
directory=/home/
dir_size=0
#Threshold to run the script
space_threshold=80
#check the available space
dir_size=$(du -m "$directory" | awk '{print $1}')
if [ "$dir_size" -gt "$space_threshold" ]
then
    dir_list=$(find "$directory" -iname "*.bag" -atime +7 -type f)
    dir_size=$(du -m "$directory" | awk '{print $1}')
    if [ -z "$dir_list" ] && [ "$dir_size" -gt "$space_threshold" ]
        then
        echo "I've destroyed everyone, but that's not enough!"&& logger -t SIMON_SAY -s "I've destroyed everyone, but that's not enough!"
        else
        rm $(find "$directory" -iname "*.bag" -atime +7 -type f)
    fi
else
    echo "Do nothing!"
fi
echo "Aggr!!"