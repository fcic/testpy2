// mysql默认协议报错ER_NOT_SUPPORTED_AUTH_MODE
// ans: alert user 'root'@'localhost' identified with mysql_native_password by 'fcic123456';

//PS: create new
// CREATE USER 'fcic'@'%' IDENTIFIED BY 'fcic123456';
// GRANT ALL PRIVILEGES ON *.* TO 'fcic'@'localhost';

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'fcic123456',
  database : 'test'
});
 
connection.connect();
 
connection.query('SELECT * from websites', function (error, results, fields) {
  if (error) throw error;
  console.log( JSON.stringify( results));
});

