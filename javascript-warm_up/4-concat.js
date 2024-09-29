#!/usr/bin/node
const args = proess.args.slice(2);
console.log(`${args[0] || 'undefined' is ${args[1] || 'undefined'}`);
