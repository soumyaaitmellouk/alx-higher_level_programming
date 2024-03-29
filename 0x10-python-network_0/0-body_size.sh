#!/bin/bash
# Check if URL argument is provided
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
