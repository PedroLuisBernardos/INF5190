// Supprime l'installation
//async function update_inst(path) {
  //  console.log(path)
 //   await 
//}

document.getElementById("recherche").addEventListener("submit", function() {
    var json_installation = new Object();
    if (installation === 'glissade') {
        var arrondissement = new Object();
        json_installation.nom = document.getElementById("nom").value;
        arrondissement.nom_arr = document.getElementById("nom_arr").value
        arrondissement.cle = document.getElementById("cle").value;
        arrondissement.date_maj = document.getElementById("date_maj").value;
        json_installation.arrondissement = arrondissement;
        json_installation.ouvert = parseInt(document.getElementById("ouvert").value);
        json_installation.deblaye = parseInt(document.getElementById("deblaye").value);
        json_installation.condition = document.getElementById("condition").value;
    } else if (installation === 'patinoire') {

    } else if (installation === 'piscine') {

    }
    
    event.preventDefault()
    fetch(url, {
        method:'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(json_installation)
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
