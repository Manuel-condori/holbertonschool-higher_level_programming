#!/usr/bin/node
//  script that prints the addition of 2 integers
function add (a, b) {
  return (a + b);
}
const firstArgument = parseInt(process.argv[2]);
const secondArgument = parseInt(process.argv[3]);
const total = add(firstArgument, secondArgument);
console.log(total);
