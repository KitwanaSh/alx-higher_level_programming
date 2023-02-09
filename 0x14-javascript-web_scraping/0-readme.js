#!/usr/bin/node

const theFile = process.argv[2];
const req = require('fs');
req.readFile(theFile, 'utf8', function (err, data) {
	if (err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
