#!/usr/bin/node
/* Write a class Square that defines a square and inherits
from Square of 5-square.js */

const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
