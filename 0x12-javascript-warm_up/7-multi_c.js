#!/usr/bin/node
const { argv } = require('process');
const x = Number(argv[2]);
for (let i = 0; i < x; i++) {
	if (isNaN(x)) {
		console.log('Missing number of occurences');
	}
	else {
		console.log('C is fun');
	}
}
