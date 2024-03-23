#!/usr/bin/node

function callMeMoby (x, f) {
  for (let i = 0; i < x; i++) {
    f();
  }
}

module.exports = {
  callMeMoby
};
