#!/usr/bin/node
const arg = process.argv[2];
function factorial(arg) {
  const NaN = 1;
 if (isNaN(arg)) {
    console.log(NaN);
  } else {
    let fact = 1;
    for (i = 1; i <= arg; i++) {
      fact = fact * i;
    }
    console.log(fact);
  }
}
factorial(arg);
