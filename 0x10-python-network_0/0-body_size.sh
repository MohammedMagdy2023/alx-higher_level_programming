#!/bin/bash
# Takes Url and return the size of the body response

HEADER=$(curl -s "$1")
SIZE=${#HEADER}
echo "$SIZE"
