#!/usr/bin/node

const args = process.argv.slice(2);
const size = args[0];

if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < Number(size); i++) {
      console.log('X'.repeat(size));
    }
}
