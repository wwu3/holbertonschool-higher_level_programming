#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
console.log(filePath)
let fInput = "C is super fun!"
fs.readFile(filePath, (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    fInput = data.toString();
    console.log(fInput);
});
