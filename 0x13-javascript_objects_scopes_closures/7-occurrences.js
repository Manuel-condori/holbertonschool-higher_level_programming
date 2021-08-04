#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i;
  for (i of list) {
    if (i === searchElement) {
      count++;
    }
  }
  return (count);
};
