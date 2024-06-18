#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No Argument');
} else {
  console.log(args[0]);
}
