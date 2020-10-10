const api_url =
      "https://dobx33oc0d.execute-api.us-east-1.amazonaws.com/test";
// Defining async function
async function getapi(url) {

	// Storing response
	const response = await fetch(url);

	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	data.sort(function(a, b){
    return a.Rollno - b.Rollno;
    });
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab =
		`<tr>
		<th>Roll no</th>
		<th>Attendance</th>
		<th>Name</th>
		</tr>`;


    for (var i = 0; i < data.length; i++){
    var obj = data[i];
    for (var key in obj){
        var attrName = key;
        var attrValue = obj[key];
            tab += `
    	<td><center>${attrValue}</center></td>
       `;
    }
    tab += `<tr></tr>`;
}

	// Setting innerHTML as tab variable
	document.getElementById("students").innerHTML = tab;
}
