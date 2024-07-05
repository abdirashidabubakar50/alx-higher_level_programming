#!/bin/bash
# This script send a DELETE request to the URL passed as the first and displays the body of the response
curl -sX DELETE "$1"
