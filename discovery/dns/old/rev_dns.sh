#!/bin/bash

#usage: rev_dns.sh <beginning ip address range> <orgname>
#This script will take the beginning 3 octates of an IP and return
#other stuff that matches <orgname> by doing reverse dns lookups
#in other words it just loops the last 0-255 of an IP and looks for
#an orgname after a reverse DNS lookup


beginningrange=$1
orgname=$2

for ip in $(seq 0 255);
do
    #dbg echo trying $beginningrange.$ip
    host $beginningrange.$ip | grep "$2"
done
