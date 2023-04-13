#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined) {
      w = undefined;
      h = undefined;
    }
    if (h <= 0 || h === undefined) {
      h = undefined;
      w = undefined;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
