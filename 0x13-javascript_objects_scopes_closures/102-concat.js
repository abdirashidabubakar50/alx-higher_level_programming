#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const fileA = args[0];
const fileB = args[1];
const fileC = args[2];
if (args.length < 3) {
  console.log('usage: ./102-concat.js fileA fileB fileC');
}
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
