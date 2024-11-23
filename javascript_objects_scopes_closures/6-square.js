#!/usr/bin/node

const SquareMain = require('./5-square');

class Square extends SquareMain {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.height));
    }
  }
}
module.exports = Square;
