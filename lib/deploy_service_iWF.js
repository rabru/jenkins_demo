var unirest = require("unirest");

exports.deployServiceiWF = function(ip, user, password) {
  var req = unirest("POST", "https://" + ip + "/mgmt/shared/authn/login");

  req.headers({
    "cache-control": "no-cache",
    "content-type": "application/json",
    "authorization": "Basic YWRtaW46YWRtaW4="
  });

  req.type("json");
  req.send({
    "username": user,
    "password": password,
    "loginProvidername": "tmos"
  });

  req.end(function (res) {
    if (res.error) throw new Error(res.error);

    console.log(res.body);
  });
}
