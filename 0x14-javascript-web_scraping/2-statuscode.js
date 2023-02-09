#!/usr/bin/node


const URL = process.argv[2]
const req = require('request')

req(URL, function (err, response) {
	if (err) {
		console.log(err);
	} else {
		console.log('code: ' + response.statusCode)
	}
});
