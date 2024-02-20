#!/usr/bin/node

const process = require('node:process');
const fName = process.argv[2];
const fData = process.argv[3];
const fs = require('node:fs');
fs.writeFile(fName, fData, 'utf-8', (error, f) => {
  if (error) {
    console.log(error);
  }
});
