var config = require('./config');
var deployService = require('./lib/deploy_service_iWF');
var hashFile = require('./lib/hashFile').hashFile;

//deployService.deployServiceiWF(config.iWorkflow.ip,config.iWorkflow.username,config.iWorkflow.password, config.strictSSL);
hashFile('main.py', function(data) {
	console.log(data);
});