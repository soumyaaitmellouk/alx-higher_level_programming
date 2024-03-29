#!/bin/bash
# Check if URL argument is provided
curl -sI ALLOW $1 -L | grep "ALLOW" | cut -d " " -f2-
