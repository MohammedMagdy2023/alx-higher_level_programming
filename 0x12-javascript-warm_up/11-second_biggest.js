#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  let arr = args.map(Number);
  let set = new Set(arr);
  arr = Array.from(set);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
