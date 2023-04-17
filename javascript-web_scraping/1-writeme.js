#!/usr/bin/node
const fs = require('fs');
let filePath = process.argv[2];
const content = 'Python is cool';
fs.writeFile(filePath, content, 'utf8', err => {
  if(err){
    console.err;
    return;
  }
});
