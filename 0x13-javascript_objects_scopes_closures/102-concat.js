#!/usr/bin/node
const fs = require('fs');

const [fileA, fileB, fileC] = process.argv.slice(2);
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;
    const dataC = dataA + '\n' + dataB + '\n';
    fs.writeFile(fileC, dataC, (err) => {
      if (err) throw err;
    });
  });
});
