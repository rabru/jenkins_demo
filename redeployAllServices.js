var config = require('./config');
var deployService = require('./lib/deploy_service_iWF');

deployService.deployServiceiWF(config.iWorkflow.ip,config.iWorkflow.username,config.iWorkflow.password, config.strictSSL);
