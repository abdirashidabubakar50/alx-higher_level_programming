#!/usr/bin/node
const n = Number(process.argv[2]);
function factorial (n) {
  if ((n === 0) || (isNaN(n))) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const result = factorial(n);
console.log(result);
