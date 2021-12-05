var contactobj ={
    email:'',
    name:'',
    country:'',
    subject:''
}
function contactUsSubmission(name,email,country,subject)
{
    debugger;
    if (name!="" && email !="" && subject!="") {

        contactobj.name = name;
        contactobj.email = email;
        contactobj.country = country;
        contactobj.subject = subject;
        debugger;
        //console.log(contactobj)
        //send_mail()
        send_contactUs_details()

    }
}

async function send_mail()
{
    let response = await fetch('/send-mail/')
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json)
      } else {
        alert("HTTP-Error: " + response.status);
      }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

async function send_contactUs_details()
{
    debugger;
    let response = await fetch('/sendContact_us/',
    {
      method:"POST",
      headers: {"Content-type": "application/json; charset=UTF-8"},
      body: JSON.stringify({contactobj})
    })
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json +'response')
      } else {
        alert("HTTP-Error: " + response.status);
      }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

async function get_contactUs()
{
    let response = await fetch('/get_contact_us/')
    debugger;
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        debugger;
        console.log(json)
      } else {
        alert("HTTP-Error: " + response.status);
      }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

