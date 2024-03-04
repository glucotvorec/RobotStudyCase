#!/bin/bash
#Сценарий проверяет указанную директорию на наличие занятого места и, если оно больше порогового значения, удаляет файлы .bag старше 7 дней.

#каталог требующий наблюдения
directory=/home/
dir_size=0
#Пороговое значение используемого места
space_threshold=80
#Проверка свободного места
dir_size=$(du -m "$directory" | awk '{print $1}')
if [ "$dir_size" -gt "$space_threshold" ]
then
    dir_list=$(find "$directory" -iname "*.bag" -atime +7 -type f)
    dir_size=$(du -m "$directory" | awk '{print $1}')
    if [ -z "$dir_list" ] && [ "$dir_size" -gt "$space_threshold" ]
        then
        echo "Я уничтожил всё, но этого мало!"&& logger -t SIMON_SAY -s "Я уничтожил всё, но этого мало!"
        else
        rm $(find "$directory" -iname "*.bag" -atime +7 -type f)
    fi
else
    echo "Делать нечего!"
fi
echo "Тысяча чертей!!"