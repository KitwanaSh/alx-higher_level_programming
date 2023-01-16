#!/bin/bash
# Takes URL  and sends a request
curl -s "$1" | wc -c
