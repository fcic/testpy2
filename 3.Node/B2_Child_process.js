var child_process = require('child_process');
var sh = child_process.exec('ls', function (err, stdout, stderr) {
    console.log(stdout);
});