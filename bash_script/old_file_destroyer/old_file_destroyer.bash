#!/bin/bash
#The script checks the specified directory for the occupied space and if it is greater than a threshold value, deletes .bag files older than 7 days.

#diretory for monitoring
directory=/home/glucotvorec/temp/
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
        dir_list_1day=$(find "$directory" -iname "*.bag" -atime +1 -type f)
        #Check if there are files older than one day. If there are, archive them.
        if [ -n "$dir_list_1day" ]
            then
            $(find "$directory" -iname "*.bag" -atime +1 -type f -exec gzip {} +)
            echo "Compressed everything older than a day, that's it."&& logger -t SIMON_SAY -s "Compressed everything older than a day, that's it."
        fi
        else
        echo "$dir_list"
        rm $(find "$directory" -iname "*.bag" -atime +7 -type f)
    fi
else
    echo "Do nothing!"
fi
echo "Aggr!!"