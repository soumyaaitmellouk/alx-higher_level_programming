#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
response=$(curl -s -o /tmp/response.txt -w "%{size_download}" "$url")

echo "Size of the response body: $response bytes"
rm -f /tmp/response.txt
