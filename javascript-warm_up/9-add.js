#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  if (isNaN(a)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}
add(a, b);
