#!/bin/bash
# This is a script that fetches a URL using curl
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
