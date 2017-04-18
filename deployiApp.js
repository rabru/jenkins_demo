config = require('./config');
deployService = require('./lib/deploy_service_iWF');
unirest = require("unirest");
fs = require('fs')
wait=require('wait.for');

var iAppTemplate = fs.readFileSync(process.argv[2], 'utf8');

console.log(deployService.AuthenticateiWF(config.iWorkflow.ip,config.iWorkflow.username,config.iWorkflow.password, config.strictSSL));


/*
var req = unirest("POST", "https://" + config.iWorkflow.ip + "/mgmt/cm/cloud/tenants/" + config.tenant + "/services/iapp");

req.headers({
  "cache-control": "no-cache",
  "authorization": "Basic dGVuYW50OnRlbmFudA==",
  "content-type": "application/json"
});

req.strictSSL(config.strictSSL);

req.type("json");
req.send(iAppTemplate);

req.end(function (res) {
	console.log(res.body);
	
	if (res.error) throw new Error(res.error);
});
*/