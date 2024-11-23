#!/usr/bin/node

const SquareMain = require('./5-square');

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends SquareMain {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = C || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.height));
    }
  }
}
module.exports = Square;
