#!/usr/bin/node
const { argv } = require('process');
const X = Number(argv[2]);
const say = 'X'.repeat(X);
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    console.log(say);
  }
}
