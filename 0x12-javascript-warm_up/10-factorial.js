#!/usr/bin/node

function fact (n) {
    if (n==0) {
        return 1;
    } else {
        fact (n-1);
    }
}

const n = process.argv[2]
if (isNaN(n)) {
    console.log(1);
} else {
    fact(n);
}
