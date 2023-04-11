#!/usr/bin/node
let x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  const repeatedstr = 'C is fun';
  while (x > 0) {
    console.log(repeatedstr);
    x = x - 1;
  }
}
