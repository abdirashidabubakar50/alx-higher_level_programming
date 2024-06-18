#!/usr/bin/node
const args = process.argv.slice(2);
const argsInt = parseInt(args[0], 10);
if (isNaN(argsInt)) {
  console.log('Not a number');
} else {
  console.log('My number :', args[0]);
}
