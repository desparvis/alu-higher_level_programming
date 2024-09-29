#!/usr/bin/node
function add(a, b) {
const args = process.argv.slice(2);
const a = args[0];
const b = args[1];
const x = a+b;
console.log(x);
}
