#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const arglength = args.length;
if (arglength === 0 || args.length === 1) {
  console.log('0');
} else {
  let max = -Infinity;
  let secondMax = -Infinity;
  for (let i = 0; i < arglength; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] < max) {
      secondMax = args[i];
    }
  }
  console.log(max);
}
