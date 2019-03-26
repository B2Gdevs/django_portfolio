
if (localStorage.getItem("dynamic-text-color") === "dark"){
darkTheme();
}

document.getElementById("btn-dark-theme").addEventListener('click', darkTheme);
document.getElementById("btn-light-theme").addEventListener('click', lightTheme);
document.getElementById("normal-disclaimer").addEventListener('click', normalDisclaimer);
document.getElementById("data-disclaimer").addEventListener('click', dataDislcaimer);

function darkTheme(){
    document.body.style.backgroundColor = "#1E1E1E";
    let shownText = document.getElementsByClassName("dynamic-text");

    let darkBtn = document.getElementById("btn-dark-theme");
    let lightBtn = document.getElementById("btn-light-theme");

    darkBtn.style.color = "#FFFFFF";
    lightBtn.style.color = "#FFFFFF";

    for (let text of shownText){
        text.style.color = "#FFFFFF";
    }
    localStorage.setItem("dynamic-text-color", "dark");
}

function lightTheme(){
    document.body.style.backgroundColor = "#F5F5F5";
    let shownText = document.getElementsByClassName("dynamic-text");

    let darkBtn = document.getElementById("btn-dark-theme");
    let lightBtn = document.getElementById("btn-light-theme");

    lightBtn.style.color = "#1E1E1E";

    for (let text of shownText){
        text.style.color = "#1E1E1E";
    }

    localStorage.setItem("dynamic-text-color", "light");
}

function normalDisclaimer(){
    let disclaimer = document.getElementById("disclaimer");

    disclaimer.innerText = 
    `This predicter isn't very good at determining every time a team will be under twenty points in a quarter. ` 
    + `So it misses a few times where the outcome actually would be that the team would score under 20.  So it `
    + `is a little difficult to trust the team won't be under twenty.  However, the inverse isn't true.  This `
    + `predictor is very reliable in its true values.  So if it says a team will be under twenty points in the `
    + `quarter then it is more than likely right.  So in better words you can't trust the false values, but you `
    + `can trust the true values.`;
}

function dataDislcaimer(){
    let disclaimer = document.getElementById("disclaimer");

    disclaimer.innerText =
     `The model has very high precision and very low recall.  The model right now is an SVM using an RBF Kernel.`
     + `\n\nCross Validation was performed using 10 folds:\n\n`
     + ` Precision = 0.9895731428344113, Recall = 0.10517347409419361, Accuracy = 0.8548280580923453`
                        
}