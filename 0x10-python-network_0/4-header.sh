#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
curl -sX GET $1 -H "X-School-User-Id" -L
