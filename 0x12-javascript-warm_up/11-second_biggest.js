#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined || Number(args[0]) == 1) {
  console.log(0);
} else {
  Number(args);
  args.sort();
  args.reverse();
  console.log(args[1]);
}
