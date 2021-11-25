
console.log(document.getElementById('image_delete'))
console.log('***')
var button_delete = document.getElementsByName('_delete');
console.log(button_delete);

console.log(button_delete.length)
for (let i = 0; i < button_delete.length; i++) {
    console.log(i)
}

/*
document.getElementById('image_delete').addEventListener("click", function() {
    console.log(this.name)
    fetch(this.name, {method:'DELETE'})
    .then(response => response.text())
    .then(response => JSON.parse(response))
    .then(response => {
        var nom_installation;
        var nom_arrondissement;
        if (type_inst == "patinoire") {
            nom_installation = response.nom_pat;
            nom_arrondissement = response.nom_arr;
        } else if (type_inst == "piscine") {
            nom_installation = response.nom;
            nom_arrondissement = response.arrondisse;
        } else if (type_inst == "glissade") {
            nom_installation = response.nom;
            nom_arrondissement = response.nom_arr;
        }
        alert("L'installation " + nom_installation + " à " + nom_arrondissement  + " a été suprimée");
        window.location.reload();
    })
});
*/