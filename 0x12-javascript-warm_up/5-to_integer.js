#!/usr/bin/node
const args = process.argv[2]
const argsInt = Number(args);
if (!isNaN(argsInt)) {
  console.log('My number:', argsInt);
} else {
  console.log('Not a number');
}
