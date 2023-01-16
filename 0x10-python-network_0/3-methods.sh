#!/bin/bash
# This script takes in a URL and diaplays all HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
