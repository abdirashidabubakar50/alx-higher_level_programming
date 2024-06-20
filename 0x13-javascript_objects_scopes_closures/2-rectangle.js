#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      const Rectangle = {};
      Rectangle.width = 0;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
