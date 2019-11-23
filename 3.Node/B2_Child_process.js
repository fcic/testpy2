//fcic: linux 和win可以用这个

var cmd = require('child_process');


cmd.exec('ls', function (err, stdout, stderr) {
    console.log(stdout);
});



cmd.exec('curl ip.sb', function (err, stdout, stderr) {
    console.log(stdout);
});


