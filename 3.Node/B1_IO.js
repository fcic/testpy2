var fs = require("fs");


//read
console.log(fs.readFileSync('test.js').toString());

//write
fs.writeFile('input.txt', '我是通 过fs.writeFile 写入文件的内容',function(){});