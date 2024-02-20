#!/usr/bin/node

const process = require('node:process');
const fName = process.argv[2];
const fs = require('node:fs');
fs.readFile(fName, 'utf-8', (error, f) => {
  if (error) {
    console.log(error);
  } else {
    console.log(f);
  }
});
