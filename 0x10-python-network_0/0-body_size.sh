#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request to the URL and display the size of the response body in bytes
curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}'
