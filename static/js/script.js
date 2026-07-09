function deleteRecord() {
    var usn = document.getElementById("usn").value;

    if (usn === "") {
        alert("Enter a USN");
        return false;
    }

    return true;
}