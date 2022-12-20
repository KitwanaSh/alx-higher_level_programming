#!/usr/bin/node
const { argv } = require('process');
const makeit = Number(argv[2]);
if (isNaN(makeit)) { console.log('Not a number'); } else { console.log('My number: ' + makeit); }
