#!/bin/bash
# Use Post method to send data
curl -sX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
