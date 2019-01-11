#!/bin/bash

progname=$1

cat sample.txt | $progname | uniq -c
