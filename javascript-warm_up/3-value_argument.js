#!/usr/bin/node
if (process.argv[2] === '-f') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
