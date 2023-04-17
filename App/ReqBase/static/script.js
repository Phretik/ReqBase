function deleteReq(reqId){           
    responseReq = window.confirm("Do you want to delete this request?"); //Creates a confirmation pop up
    if (responseReq == true){            //Checks if the user confirmed
        fetch('/delete-req', {     //Calls the /delete-req route
            method: "POST",
            body: JSON.stringify({ reqId: reqId}),   //Deletes the request with the passed in ID 
        }).then((_res) => {
            window.location.href = "/";
        });
    }
}

function deleteLog(postId){   
    responseLog = window.confirm("Do you want to delete this post?"); //Creates a confirmation pop up
    if (responseLog == true){                   //Checks if the user confirmed
        fetch('/delete-log', {                //Calls the /delete-log route
            method: "POST",
            body: JSON.stringify({ postId: postId}),       //Deletes the log with the passed in ID 
        }).then((_res) => {
            window.location.href = "/teamLog";
        });
    }
}
