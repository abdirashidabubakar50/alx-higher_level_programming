#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response with a custom header
curl -s -H "X-School-User-Id: 98" "$1"
