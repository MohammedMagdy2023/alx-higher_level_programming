#!/bin/bash
# Takes Url and return the size of the body response
curl -s "$1" | wc -c
