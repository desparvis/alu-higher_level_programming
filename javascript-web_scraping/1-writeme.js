#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (!filePath || !stringToWrite) {
  console.log('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error('An error occurred while writing to the file:', err);
    return;
  }
  console.log('File written successfully');
});

