#!/bin/bash
# docstrings
curl -sI -X OPTIONS "$1" | grep 'Allow:' | cut -d ' ' -f2-
