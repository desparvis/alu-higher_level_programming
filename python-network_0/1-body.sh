#!/bin/bash
curl -sL "$1" -o /dev/null && curl -s "$1"
