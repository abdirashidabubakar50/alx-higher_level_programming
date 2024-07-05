#!/bin/bash
# This is a script that fetches a URL using curl
curl -s "$1" -w '%{size_download}\n' -o /dev/null
