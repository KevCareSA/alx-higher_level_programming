#!/bin/bash
# display size of http bytes in location
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
