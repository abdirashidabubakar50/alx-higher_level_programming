#!/bin/bash
#This script takes in a url, sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" -o response_body | { read status; [ "$status" -eq 200 ] && cat response_body; }
