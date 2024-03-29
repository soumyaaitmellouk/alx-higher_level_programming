#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a GET request to the URL and display the body of the response if status code is 200
response=$(curl -s -w "%{http_code}" -o /tmp/response.txt "$url")
status_code=$(tail -n1 /tmp/response.txt)

if [ $status_code -eq 200 ]; then
    cat /tmp/response.txt
fi

# Clean up the temporary file
rm -f /tmp/response.txt
