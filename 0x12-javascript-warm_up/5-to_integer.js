#!/usr/bin/node

const args = process.argv.slice(2);

if (Number(args[0]) == undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(args[0]));
}
