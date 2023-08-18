#!/usr/bin/env bash

count=0
doc=~/Desktop/KB_Test.txt

[[ -f /usr/bin/xdotool ]] || sudo apt install xdotool -y
read -p "Enter test cycles: " cycles
while [ $count -lt $cycles ]
do    
	[[ -f ~/Desktop/KB_Test.txt ]] || touch $doc
	open $doc
	xdotool key super
	sleep 1
	xdotool key super
	sleep 1
	xdotool key h
	sleep 0.5
	xdotool key p
	sleep 0.5
	xdotool key period
	sleep 0.5
	xdotool key c
	sleep 0.5
	xdotool key o
	sleep 0.5
	xdotool key m
	sleep 0.5
	xdotool key Return
	sleep 1
	count=$(($count+1))
done
xdotool key ctrl+s
killall gedit
grep "[^hp.com$]" $doc 
if [ $? == 1 ]; then 
	echo -e '\n***Test COMPLETED w/o incorrect strings***'
else
	echo -e '\nWRONG strings found!!'
fi

