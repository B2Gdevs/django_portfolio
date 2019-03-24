document.getElementById("btn-dark-theme").addEventListener('click', darkTheme);
document.getElementById("btn-light-theme").addEventListener('click', lightTheme);

function darkTheme(event){
    document.body.style.backgroundColor = "#1E1E1E";
    let shownText = document.getElementsByClassName("dynamic-text");

    for (let text of shownText){
        text.style.color = "#FFFFFF";
    }
}

function lightTheme(event){
    document.body.style.backgroundColor = "#FFFFFF";
    let shownText = document.getElementsByClassName("dynamic-text");

    for (let text of shownText){
        text.style.color = "#1E1E1E";
    }
}