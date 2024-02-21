#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const res = JSON.parse(body);
    const count = {};

    for (const task of res) {
      const userId = task.userId;
      const completed = task.completed;

      if (completed) {
        count[userId] = (count[userId] || 0) + 1;
      }
    }

    for (const userId in count) {
      console.log(`${userId}: ${count[userId]}`);
    }
  }
});
