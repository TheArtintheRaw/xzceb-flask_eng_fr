let translateToFrench = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translatedText").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "englishToFrench?english_text"+"="+textToTranslate, true);
    xhttp.send();
}

let translateToEnglish = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translatedText").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "frenchToEnglish?french_text"+"="+textToTranslate, true);
    xhttp.send();
}

