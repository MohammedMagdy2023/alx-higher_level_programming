#!/usr/bin/node

function addMeMaybe (x, f) {
  f(++x);
}

module.exports = {
  addMeMaybe
};
