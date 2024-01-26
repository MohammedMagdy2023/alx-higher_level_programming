#!/bin/bash
# This file Get all methods in the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
