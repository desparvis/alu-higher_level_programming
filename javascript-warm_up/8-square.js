#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
