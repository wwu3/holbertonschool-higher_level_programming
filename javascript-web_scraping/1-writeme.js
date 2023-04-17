#!/usr/bin/node
const fs = require('fs');
const content = 'Python is cool';
fs.writeFile('my_file.txt', content, 'utf8', err => {
  if(err){
    console.error(err);
    return;
  }
});
