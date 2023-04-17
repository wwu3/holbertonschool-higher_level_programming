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
}

module.exports = Rectangle;
