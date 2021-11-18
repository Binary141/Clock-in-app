clock_in = document.querySelector("#Clock_in");
clock_out = document.querySelector("#Clock_out");
time = document.getElementById("Time");
submit_file = document.getElementById("submit_File")

console.log(time)
time.innerHTML = "test";
var seconds = 55;
var milliseconds = 0;
clock_in.onclick = function(){
	//fetch("http://YOUR_URL/drives").then(function (response) {
	//	response.json().then(function (data) {
		
			
		var data = "firstname=" + "in";
		
		console.log("Data sent to server: ", data);
			fetch("http://YOUR_URL/public", {
			method: "POST",
			body: data,
			headers: {
				"Content-Length": data.length.toString(),
				"Content-Type": "application/x-www-form-urlencoded"
			}

		}).then(function (response) {
			response.blob().then(function (myBlob) {
				console.log("data:", myBlob);
				var objectURL = URL.createObjectURL(myBlob);
				document.querySelector("#image").src=objectURL;
				//var img = document.createElement("img");
				//img.setAttribute("src", data);
				//ele.appendChild(img);
				//append ele to parent div
			});
		});
	seconds = 55;
	milliseconds = 0;
	console.log("The clock in button was pressed");
	var timer = setInterval(function(){
		var checkNum = 0;
		if(milliseconds == 0 || milliseconds < 0){
			if(seconds == 0 || seconds < 0){
				console.log("Reight here");
				time.innerHTML = "0:0";
				clearInterval(timer);
				checkNum = 1;
			}
			seconds -= 1;
			milliseconds = 99;
		}
		if(checkNum == 0){
			time.innerHTML = seconds + ":" + milliseconds;
			console.log(seconds, ":", milliseconds);
			milliseconds -= 1;
		}
	}, 10);
	console.log("after");

}

clock_out.onclick = function(){
	console.log("The clock out button was pressed");
	//fetch("http://YOUR_URL/drives").then(function (response) {
	//	response.json().then(function (data) {
		
			
		var data = "firstname=" + "out";
		
		console.log("Data sent to server: ", data);
			fetch("http://YOUR_URL/public", {
			method: "POST",
			body: data,
			headers: {
				"Content-Length": data.length.toString(),
				"Content-Type": "application/x-www-form-urlencoded"
			}

		}).then(function (response) {
			response.blob().then(function (myBlob) {
				console.log("data:", myBlob);
				var objectURL = URL.createObjectURL(myBlob);
				document.querySelector("#image").src=objectURL;
				//var img = document.createElement("img");
				//img.setAttribute("src", data);
				//ele.appendChild(img);
				//append ele to parent div
			});
		});
	seconds = 55;
	milliseconds = 0;
	console.log("The clock in button was pressed");
	var timer = setInterval(function(){
		var checkNum = 0;
		if(milliseconds == 0 || milliseconds < 0){
			if(seconds == 0 || seconds < 0){
				console.log("Reight here");
				time.innerHTML = "0:0";
				clearInterval(timer);
				checkNum = 1;
			}
			seconds -= 1;
			milliseconds = 99;
		}
		if(checkNum == 0){
			time.innerHTML = seconds + ":" + milliseconds;
			console.log(seconds, ":", milliseconds);
			milliseconds -= 1;
		}
	}, 10);
	console.log("after");
}

submit_file.onclick = function(){
	let formData = new FormData();
	formData.append("file", document.querySelector("#File_upload").files[0]);
	console.log(document.querySelector("#File_upload").files[0])
	fetch('http://YOUR_URL/fileUpload', {
		method: "POST",
		body: formData
	});
//	alert('The file has been uploaded successfully.');
}
