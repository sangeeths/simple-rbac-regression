#!/bin/bash

roles=$1
resources=$2
step=$3
times=$4

for i in `seq 1 $times`; do
    python main.py -r $roles -R $resources
    let resources=$resources+$step 
done

