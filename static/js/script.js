function deleteRecord() {
    let usn = document.getElementById("usn").value;
    var pattern=/^1SI[0-9]{2}[A-Z]{2}[0-9]{3}$/
    if (usn === "") {
        alert("Enter a USN");
        return false;
    }
    if(usn.length!==10){
        alert("the length of usn must be 10");
        return false;
    }
    if(!pattern.test(usn)){
        alert("Enter a valid USN ");
        return false;
    }

    return true;
}
function saveRecord() {
    let usn = document.getElementById("usn").value;
    let name= document.getElementById("name").value;
    let year=document.getElementById("year").value;
    let cgpa=document.getElementById("cgpa").value;

    if (usn === "") {
        alert("Enter a USN");
        return false;
    }
    if(name===""){
        alert("enter name");
        return false;
    }
    if(year===""){
        alert("enter a Academic year");
        return false;
    }
    if(cgpa===""){
        alert("enter a CGPA");
        return false;
    }

    return true;
}