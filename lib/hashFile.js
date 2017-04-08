var crypto = require('crypto');
var fs = require('fs');

function checksum (str, algorithm, encoding) {
    return crypto
        .createHash(algorithm || 'sha1')
        .update(str, 'utf8')
        .digest(encoding || 'hex')
}

exports.hashFile = function(fileName,callback){
	fs.readFile(fileName, function (err, data) {
		callback(checksum(data));
	});
}