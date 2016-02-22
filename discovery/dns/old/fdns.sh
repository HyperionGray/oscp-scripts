#!/bin/bash

#usage <domain name>

name=$1

for prefix in $(cat list.txt);do
    host -t A $prefix.$name | grep "has address"
done
