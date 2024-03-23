#!/usr/bin/node

function callMeMoby(x, f) {
  for (var i = 0; i < x; i++) {
    f();
  };
};

module.exports = {
  callMeMoby,
};
