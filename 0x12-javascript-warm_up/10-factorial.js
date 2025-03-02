#!/usr/bin/node
/* Write a script that computes and prints a factorial */

let args = parseInt(process.argv[2]);
if (isNaN(args)) {
  args = 1;
}

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(args));
