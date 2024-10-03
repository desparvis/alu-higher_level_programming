#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.log('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  console.log(data);
});
