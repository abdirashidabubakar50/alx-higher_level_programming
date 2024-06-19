#!/usr/bin/node
const x = process.argv[2];
const numX = Number(x);
if (isNaN(numX)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numX; i++) {
    console.log('C is fun');
  }
}
