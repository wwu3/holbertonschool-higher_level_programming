#!/usr/bin/node
const str = 'X';
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
  process.exit();
} else {
  for (let x = 0; x < size; x++) {
    let line = '';
    for (let y = 0; y < size; y++) {
      line += str;
    }
    console.log(line);
  }
}
