#!/usr/bin/node
//  script that prints two arguments passed to it, in the following format: “is”
const firstArgument = process.argv[2];
const secondArgument = process.argv[3];
console.log(firstArgument + ' is ' + secondArgument);
