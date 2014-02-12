#!/bin/bash

for a in *.txt; do echo ${a}; cut -d , -f 2 ${a} | sort | uniq -c | grep -v Species; done
