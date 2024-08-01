#!/bin/bash
# i dont have to explain myself
curl -sL "$1" -o /dev/null && curl -s "$1"
