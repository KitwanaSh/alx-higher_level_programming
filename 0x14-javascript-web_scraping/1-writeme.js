#!/usr/bin/node

const theFile = process.argv[2]
const txt = process.argv[3]
const req = require('fs')
req.writeFile(theFile, txt, 'utf8', function(err) {
	if (err) {
		console.log(err);
	}
});
