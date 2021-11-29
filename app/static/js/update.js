// Supprime l'installation
//async function update_inst(path) {
  //  console.log(path)
 //   await 
//}

document.getElementById("recherche").addEventListener("submit", function() {
    var glissade = new Object();
    var arrondissement = new Object();
    glissade.nom = document.getElementById("nom").value;
    arrondissement.nom_arr = document.getElementById("nom_arr").value
    arrondissement.cle = document.getElementById("cle").value;
    arrondissement.date_maj = document.getElementById("date_maj").value;
    glissade.arrondissement = arrondissement;
    glissade.ouvert = parseInt(document.getElementById("ouvert").value);
    glissade.deblaye = parseInt(document.getElementById("deblaye").value);
    glissade.condition = document.getElementById("condition").value;
    event.preventDefault()
    fetch(url, {
        method:'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(glissade)
    })
    .then(response => response.text())
    .then(response => JSON.parse(response))
    .then(response => {
        alert(response)
        console.log(response)
        //event.target.submit();
        window.location.replace(url);
    });
})
