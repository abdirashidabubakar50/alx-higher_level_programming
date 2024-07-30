#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file content in utf-8
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Print the detailed error object if an error occurred
        console.log({
            Error: `ENOENT: no such file or directory, open '${filePath}'`,
            at: 'Error (native)',
            errno: err.errno,
            code: err.code,
            syscall: err.syscall,
            path: filePath
        });
        return;
    }
    // Print the file content
    console.log(data);
});