#!/usr/bin/env bash

[[ -f /usr/bin/xdotool ]] || sudo apt install xdotool -y


read -p "Enter test cycles: " cycles
count=0
while [ $count -lt $cycles ]
do    
	[[ -f ~/Desktop/KB_Test.txt ]] || touch ~/Desktop/KB_Test.txt
	open ~/Desktop/KB_Test.txt
	xdotool key super
	sleep 1
	xdotool key super
	sleep 2
	xdotool key h
	sleep 1
	xdotool key p
	sleep 1
	xdotool key space
	sleep 1
	xdotool key c
	sleep 1
	xdotool key o
	sleep 1
	xdotool key m
	sleep 1
	xdotool key Return
	sleep 1
	count=$(($count+1))
done
echo ***TEST COMPLETED***
