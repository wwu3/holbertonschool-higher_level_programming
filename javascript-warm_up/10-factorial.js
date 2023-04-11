#!/usr/bin/node
const NaN = 1;
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log(NaN);
  process.exit();
} else {
  let fact = 1;
  for (i = 1; i <= arg; i++) {
    fact = fact * i;
  }
  console.log(fact);
}
