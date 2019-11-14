//fcic:
//this is build in http server, the A3_Express is better

var http = require('http');
var url = require('url');  //reequest.get

var querystring = require('querystring'); //request.post

var util = require('util'); //obj-> string

var fs = require('fs');  //view index.html

http.createServer(function (request, response) {

    //1.response
    // response.writeHead(200, {"Content-Type": "text/plain"});
    // response.write("Hello World\n");
    // response.end();

    //2.request get
    // var params = url.parse(request.url, true).query;
    // response.write(params.name);   //http://xxx?name=xxx&age=11
    // response.write(util.inspect(params));  //obj->str : show all get parameters

    //2.2request post
    // var post = '';     
 
    //     // 通过req的data事件监听函数，每当接受到请求体的数据，就累加到post变量中
    //     request.on('data', function(chunk){    
    //         post += chunk;
    //     });
    
    //     // 在end事件触发后，通过querystring.parse将post解析为真正的POST请求格式，然后向客户端返回。
    //     request.on('end', function(){    
    //         post = querystring.parse(post);
               //response.write(post.name);   //
               //response.write(util.inspect(post));  //obj->str : show all get parameters
    //     });

    //3. view index.html
        // 解析请求，包括文件名
        var pathname = url.parse(request.url).pathname;
        
        // 输出请求的文件名
        console.log("Request for " + pathname + " received.");

        // 从文件系统中读取请求的文件内容
        fs.readFile(pathname.substr(1), function (err, data) {
        if (err) {
            console.log(err);
            // HTTP 状态码: 404 : NOT FOUND
            // Content Type: text/html
            response.writeHead(404, {'Content-Type': 'text/html'});
        }else{             
            // HTTP 状态码: 200 : OK
            // Content Type: text/html
            response.writeHead(200, {'Content-Type': 'text/html'});    
            
            // 响应文件内容
            response.write(data.toString());        
        }
        //  发送响应数据
        response.end();
        });   

 


}).listen(8080);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8080/');


//test
//http://127.0.0.1:8080/?name=fcic&age=13