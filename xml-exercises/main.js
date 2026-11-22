let xx;
xx='<h1>hello world</h1>';
xx+='<label for="myInput">which book?</label><input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for books.."><button onclick="showsBook()">search</button>';
xx+='<div id="suggestions" class="d-none"></div>';
document.body.innerHTML=xx;
function loadXMLDoc(filename) {
let xhttp;
xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
xmlres= this.responseXML;
}
};
xhttp.open("GET", filename, true);
xhttp.send();
return xmlres;
}

function myFunction() {
let answer=document.getElementById("myInput").value;
let xmlDoc = loadXMLDoc("data.xml");
booksSuggest(xmlDoc, answer);
}

function booksSuggest(xml, answer) {
let books = xml.getElementsByTagName("book");

let suggestions = document.getElementById("suggestions");
suggestions.classList.remove("d-none");
suggestions.innerHTML = "";
for (let i = 0; i < books.length; i++) {
    let title = books[i].getElementsByTagName("title")[0].childNodes[0].nodeValue;
    if (title.toLowerCase().includes(answer.toLowerCase()) && answer.trim() !== "") {
        let div = document.createElement("div");
        div.innerHTML = title;
        div.classList.add("p-2", "border-bottom");
        suggestions.appendChild(div);
        div.onclick = function() {
            document.getElementById("myInput").value = title;
            suggestions.classList.add("d-none");
        }
    }}
}
function showsBook() {
let answer=document.getElementById("myInput").value;
let xmlDoc = loadXMLDoc("data.xml");
displayBook(xmlDoc, answer);
}

function displayBook(xml, answer) {
let books = xml.getElementsByTagName("book");
let bookFound = false;
for (let i = 0; i < books.length; i++) {
    let title = books[i].getElementsByTagName("title")[0].childNodes[0].nodeValue;
    if (title.toLowerCase() === answer.toLowerCase()) {
        bookFound = true;
        let author = books[i].getElementsByTagName("author")[0].childNodes[0].nodeValue;
        let year = books[i].getElementsByTagName("year")[0].childNodes[0].nodeValue;
        let genre = books[i].getElementsByTagName("genre")[0].childNodes[0].nodeValue;
        let isbn = books[i].getElementsByTagName("isbn")[0].childNodes[0].nodeValue;
        // Display the book details
        let bookDetails = `
            <h2>${title}</h2>
            <p><strong>Author:</strong> ${author}</p>
            <p><strong>Year:</strong> ${year}</p>
            <p><strong>Genre:</strong> ${genre}</p>
            <p><strong>ISBN:</strong> ${isbn}</p>
        `;
        let display=document.createElement("div");
        display.classList.add("border","p-3","mt-3");
        display.innerHTML=bookDetails;
        document.body.appendChild(display);
        break; 
    }
}
if (!bookFound) {
    document.getElementById("suggestions").innerHTML = "<p>No book found</p>";
}   }