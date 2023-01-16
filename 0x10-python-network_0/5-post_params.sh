#!/bin/bash
# This script takes in a URL, sends a POST rquest to the pass URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
