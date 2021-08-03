#!/usr/bin/node
// script that prints x times “C is fun”
let i;
const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 1; i <= argument; i++) {
    console.log('C is fun');
  }
}
