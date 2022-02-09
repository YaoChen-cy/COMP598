#!/bin/bash

if [ $(wc -l < $1 ) -lt 10000 ]
then
        echo "Error Message: File should has at least 10000 lines!"
else
	echo "$(wc -l < $1 | xargs )"
	echo "$(head -n1 $1)"
	echo "$(tail -n10000 $1 | grep -c -i "potus" )"
	echo "$(sed -n '100,200p' $1 | grep -c -w "fake" )"
fi
