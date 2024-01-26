#!/bin/bash
# Display the body of success curls 
curl -s "$1" -w "\n%{http_code}"
