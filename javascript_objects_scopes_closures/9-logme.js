#!/usr/bin/node
let numberArgumentsAlreadyPrinted = 0;
exports.logMe = function (item) {
  console.log(numberArgumentsAlreadyPrinted + ':' + item);
  numberArgumentsAlreadyPrinted = numberArgumentsAlreadyPrinted + 1;
};
