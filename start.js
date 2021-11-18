var bodyParser = require('body-parser');
var express = require('express'); 
var app = express(); 
var http = require('http');
var fs = require('fs');
var formidable = require('formidable');
var cors = require('cors');
 
// html file containing upload form
//var upload_html = fs.readFileSync("upload_file.html");
 
// replace this with the location to save uploaded files
//var upload_path = "./";

app.use(express.static('./'));
app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});
app.use(bodyParser.urlencoded({ extended: true })); 

app.listen(8080, function() { 
    console.log('server running on port 8080'); 
} ) 
  
app.post('/public', callName); 
app.post('/fileupload', FileUpload);
app.get('/', uploadForm);

app.all('/*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  next();
});

function Main(req, res) {
	res.status(200).sendFile('./index.html', {root: __dirname });
}

function callName(req, res) { 
	//res.header("Access-Control-Allow-Origin", "*");
	//res.header("Access-Control-Allow-Headers","Origin, X-Requested-With, Content-Type, Accept");
    	//res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
	console.log("New request")

	var spawn = require("child_process").spawn; 
	console.log("Spawned a new process")

	console.log("Started the process")
	console.log(req.body.firstname);
	console.log("Request Body: ", req.body.firstname)
	console.log("clocked_"+req.body.firstname+".png")
	var process = spawn('python',["./WebsitesLoginAutomation.py", req.body.firstname] ); 
	console.log("After the process");

	console.log("clocked_"+req.body.firstname+".png")
	process.stdout.on('data', function(data) { 
		console.log("parsing the data")
		console.log(data.toString());
		//res.sendFile('clocked_'+req.query.firstname+'.png', {root: __dirname });//data.toString()); 
		res.status(200).sendFile('./clocked_out.png', {root: __dirname });
		//res.status(200).sendFile('./clocked_'+req.body.firstname+'.png', {root: __dirname });
	} ) 
} 

function FileUpload(req, res) {
	console.log("A request has been made");
	var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            // oldpath : temporary folder to which file is saved to
            var oldpath = files.filetoupload.path;
	    console.log("Files: ", files);
            var newpath = upload_path + files.filetoupload.name;
            // copy the file to a new location
            fs.rename(oldpath, newpath, function (err) {
                if (err) throw err;
                // you may respond with another html page
                res.write('File uploaded and moved!');
                res.end();
            });
        });


}
function uploadForm(req, res) {
	console.log("A request has been made");
	res.status(200).sendFile('./upload_file.html', {root: __dirname });
}
  
