var unirest = require("unirest");

exports.AuthenticateiWF = function(ip, user, password, strictSSL) {
	var reqAuth = unirest("POST", "https://" + ip + "/mgmt/shared/authn/login");

	reqAuth.headers({
		"cache-control": "no-cache",
		"content-type": "application/json",
		"authorization": "Basic YWRtaW46YWRtaW4="
	});

	reqAuth.type("json");
	reqAuth.send({
		"username": user,
		"password": password,
		"loginProvidername": "tmos"
	});

	reqAuth.strictSSL(strictSSL);

	reqAuth.end(function (res) {
		if (res.error) throw new Error(res.error);

		//console.log(res.body);
		parsedBody = JSON.parse(res.body);
		console.log(parsedBody.body);
	});
}

exports.deployiApp = function(ip, token, tenant, serviceName, jsonPayload, strictssl) {
		reqiApp = unirest("POST", "https://" + ip + "/mgmt/cm/cloud/tenants/" + tenant + "/services/iapp/" + serviceName);

	reqiApp.headers({
		"cache-control": "no-cache",
		"x-f5-auth-token": token,
		"content-type": "application/json"
	});

	reqiApp.type("json");
	reqiApp.send(jsonPayload);

	reqiApp.end(function (res) {
		if (res.error) throw new Error(res.error);

		console.log(res.body);
	});
}