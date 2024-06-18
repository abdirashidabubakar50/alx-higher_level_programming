#!/usr/bin/node
if (process.argv.slice(2) === null) {
  console.log('No Argument');
} else {
  console.log(process.argv[3]);
}
