#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
if (typeof process.argv[2] === 'undefined' || process.argv.length < 4) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i], 10));
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
