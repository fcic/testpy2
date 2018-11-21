var http = require("http");

http.createServer(function(req,res){
   res.writeHead(200,{"Content-type":"text/blain"});
   res.write("Hello NodeJs");
   res.write("test2");
   res.end();
}).listen(8888);