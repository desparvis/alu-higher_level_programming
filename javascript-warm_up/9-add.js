#!/usr/bin/node
function add(a, b) {
const args = process.argv.slice(2);
a = args[0];
b = args[1];
const x = a+b;
console.log(x);
}
