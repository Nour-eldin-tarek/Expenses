function toggleNav() {
    var sideNavWidth = document.getElementById("mySidenav").style.width;
    if (sideNavWidth === "60%") {
        document.getElementById("mySidenav").style.width = "0";
    } else {
        document.getElementById("mySidenav").style.width = "60%";
    }
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var closeul = document.getElementsByClassName("closeul");
var i;
var count = 0;



// Create a new list item when clicking on the "Add" button
function newElement() {
    var tr =document.createElement("tr");
    var th1 = document.createElement("th");
    var th2 = document.createElement("th");
    var th3 = document.createElement("th");
    var inputValue = document.getElementById("myInput").value;
    var priceValue = document.getElementById("myInputprice").value;
    var categories= document.getElementById("category").value;
    var t = document.createTextNode(inputValue);
    var p = document.createTextNode(priceValue);
    var c = document.createTextNode(categories);
    th1.appendChild(t);
    th2.appendChild(p);
    th3.appendChild(c);
    if (inputValue === '') {
        alert("You must write something!");
    }
    else if (categories === 'الفئآت') {
        alert("You have to choose the category!");
    }
    else if (priceValue === '') {
        alert("You have to write the price!");
    }
    else {
        tr.appendChild(th1);
        tr.appendChild(th2);
        tr.appendChild(th3);
        document.getElementById("myTR").appendChild(tr);
    }
    // document.getElementById("myInput").value = "";
    // document.getElementById("myInputprice").value = "";
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    tr.appendChild(span);

    for (i = 0; i < close.length; i++) {   // Click on a close button to hide the current list item
        close[i].onclick = function() {
            var div = this.parentElement;
            div.parentElement.removeChild(div);
        }
    }
}

function newElement4() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput4").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must write something!");
    }
    else if (count>=1) {
        console.log("It takes one value");
    }
    else {
        document.getElementById("myUL4").appendChild(li);
        count++;
    }
    document.getElementById("myInput4").value = "";
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "closeul";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < closeul.length; i++) {
        closeul[i].onclick = function() {
            var div = this.parentElement;
            div.parentElement.removeChild(div);
            count=0;
        }
    }
}
function filtrers() {
    var filtrersValue = document.getElementById("filterCategory").value;
    if (filtrersValue === 'التصنيف') {
        document.getElementById("main").style.display = "block";
        document.getElementById("all").style.display = "none";
    }
    else {
        document.getElementById("all").style.display = "block";
        document.getElementById("main").style.display = "none";
    }
    }

// to confirm before delet bill 
var config = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == config) {
        config.style.display = "none";
    }
}