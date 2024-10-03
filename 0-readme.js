#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

if (!filePath) {
    console.log("Usage: node script.js <file_path>");
    process.exit(1);
}

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Print the error object if an error occurred
        console.error("An error occurred:", err);
        return;
    }
    // Print the file content
    console.log(data);
});
