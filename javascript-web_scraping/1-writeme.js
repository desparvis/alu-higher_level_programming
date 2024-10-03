#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both arguments are provided, otherwise do nothing
if (filePath && stringToWrite) {
  fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
} else {
  // Log the arguments for debugging
  console.error('File path or string to write is missing.');
}
