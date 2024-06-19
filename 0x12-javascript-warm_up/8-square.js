#!/usr/bin/node
const firstArgument = Number(process.argv[2]);
if (isNaN(firstArgument)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgument; i++) {
    let line = '';
    for (let j = 0; j < firstArgument; j++) {
      line += 'x';
    }
    console.log(line);
  }
}
