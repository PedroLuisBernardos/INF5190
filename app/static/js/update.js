document.getElementById("recherche").addEventListener("submit", function() {
    var url_fetch = url
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

        url = url + document.getElementById("nom").value
        url_fetch = url_fetch + nom_request
    } else if (installation === 'patinoire') {
        json_installation.nom_pat = document.getElementById("nom_pat").value;
        json_installation.nom_arr = document.getElementById("nom_arr").value;

        url = url + document.getElementById("nom_pat").value
        url_fetch = url_fetch + nom_request
    } else if (installation === 'piscine') {
        json_installation.id_uev = parseInt(document.getElementById("id_uev").value);
        json_installation.style = document.getElementById("style").value;
        json_installation.nom = document.getElementById("nom").value;
        json_installation.arrondisse = document.getElementById("arrondisse").value;
        json_installation.adresse = document.getElementById("adresse").value;
        json_installation.propriete = document.getElementById("propriete").value;
        json_installation.gestion = document.getElementById("gestion").value;
        json_installation.point_x = document.getElementById("point_x").value;
        json_installation.point_y = document.getElementById("point_y").value;
        json_installation.equipeme = document.getElementById("equipeme").value;
        json_installation.longitude = parseFloat(document.getElementById("longitude").value);
        json_installation.latitude = parseFloat(document.getElementById("latitude").value);

        url = url + document.getElementById("style").value + '/' + document.getElementById("nom").value
        url_fetch = url_fetch + style_request + '/' + nom_request
    }
    event.preventDefault()
    fetch(url_fetch, {
        method:'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(json_installation)
    })
    .then(response => response.text())
    .then(response => JSON.parse(response))
    .then(response => {
        console.log(response)
        event.target.submit();
        window.location.replace(url);
    });
})
