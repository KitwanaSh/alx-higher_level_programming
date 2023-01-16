#!/bin/bash
# This script sends a JSON POSY request to a URL passed as first argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
