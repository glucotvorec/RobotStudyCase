#/bin/bash
packag=$(apt list --installed | grep wine/stable)
if [ -z "$packag" ]
    then
    echo "No package find"
    else 
    echo "$packag"
fi