#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const arglength = args.length;
if (arglength === 0 || args.length === 1) {
  console.log('0');
} else {
  const uniqueNumbers = [...new Set(args)];
  uniqueNumbers.sort((a, b) => b - a);
  console.log(uniqueNumbers[1]);
}
