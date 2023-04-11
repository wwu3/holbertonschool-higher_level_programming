#!/usr/bin/node
const arg = process.argv[2];
function factorial (arg) {
	if (isNaN(arg)) {
		console.log(1);
	} else {
		let fact = 1;
		for (let i = 1; i <= arg; i++) {
			fact = fact * i;
		}
		console.log(fact);
	}
}
factorial(arg);
