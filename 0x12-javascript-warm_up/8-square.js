#!/usr/bin/node
// script that prints a square
let row, colum;
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (row = 1; row <= size; row++) {
    let fila = '';
    for (colum = 1; colum <= size; colum++) {
      fila += 'X';
    }
    console.log(fila);
  }
}
