#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
let fInput = "C is super fun!"
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    fInput = data.toString();
    console.log(fInput);
});
