#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log(0);
} else if (Number(args[0]) === 1) {
  console.log(0);
} else {
  Number(args);
  args.sort().reverse();
  console.log(args[1]);
}
