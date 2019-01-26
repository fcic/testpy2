
//fcic http server
//var http = require("http");

// http.createServer(function(req,res){
//    res.writeHead(200,{"Content-type":"text/blain"});
//    res.write("Hello NodeJs");
//    res.write("test2");
//    res.end();
// }).listen(8080);

const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  //await page.goto('https://example.com');
  await page.goto('http://www.cnblogs.com');
  //await page.screenshot({path: 'example.png'});
  await page.pdf({path: 'hn.pdf', format: 'A4'});
  await browser.close();
})();