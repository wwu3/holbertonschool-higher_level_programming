#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined) {
      return;
    }
    if (h <= 0 || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
