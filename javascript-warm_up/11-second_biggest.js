#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg) || isNaN(process.argv[3])) {
  console.log(0);
} else {
  const sorted = process.argv.slice(2).map(Number).sort((a, b) => a - b).reverse();
  console.log(sorted[1]);
}
