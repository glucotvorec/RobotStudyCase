#/bin/bash
packag=$(apt list --installed | grep wine/stable)
if [ -z "$packag" ]
    then
    echo "No packege find"
    else 
    echo "$packag"
fi