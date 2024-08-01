#!/bin/bash
# documenting modules for no reason
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
