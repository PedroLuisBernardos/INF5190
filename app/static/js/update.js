/**
 * Méthode qui retourne si l'installation existe
 * @param {*} url l'url de l'isntallation
 * @returns true elle existe, false elle n'exise pas
 */
async function nom_existe(url, type, nom_request, style_request) {
    let reponse = await fetch(url)
    .then((response) => response.json()
    .then(res => ({status: response.status, data: res})))
    .then((apiResponse) => {
        return apiResponse;
    })
    .catch((error) => {
        console.error('Erreur:', error);
    });

    if (reponse.status == 200) {
        if ((type === 'glissade' && reponse.data.nom != nom_request) || (type === 'patinoire' && reponse.data.nom_pat != nom_request) || (type === 'piscine' && (reponse.data.nom != nom_request || reponse.data.type != style_request))) {
            return true;
        }
    } 
    return false;
}

/**
 * Méthode qui valide le formulaire
 * @param {*} json_installation JSON contenant les informations du formulaire
 * @param {*} installation type d'installation
 * @returns 
 */
async function validateForm(json_installation, installation, nom_request, style_request) {
    var validated;
    var url;

    if (installation === 'glissade') {
        var nom = (json_installation.nom != null && json_installation.nom != "" && json_installation.nom.length <= 255)
        if (!nom) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de la glissade")
        }

        url = '/api/glissade/' + json_installation.nom;
        var reponse = await nom_existe(url, 'glissade', nom_request, style_request);
        if (reponse) {
            alert("Le nom de la glissade existe déjà")
        }

        var nom_arr = (json_installation.arrondissement.nom_arr != null && json_installation.arrondissement.nom_arr != "" && json_installation.arrondissement.nom_arr.length <= 255)
        if (!nom_arr) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de l'arrondissement")
        }

        var cle = (json_installation.arrondissement.cle != null && json_installation.arrondissement.cle != "" && json_installation.arrondissement.cle.length <= 5)
        if (!cle) {
            alert("Vous devez entrer entre 1 et 5 caractères pour la clé de l'arrondissement")
        }

        var ISO8601 = new RegExp(/^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}$/)
        var date_maj = (ISO8601.test(json_installation.arrondissement.date_maj))
        if (!date_maj) {
            alert("Vous devez entrer une date respectant le format ISO8601, par exemple: 2021-10-18 13:45:13")
        }

        var ouvert = Number.isInteger(json_installation.ouvert) && (json_installation.ouvert == 0 || json_installation.ouvert == 1)
        if (!ouvert) {
            alert("Votre champ ouvert doit être 0 ou 1 uniquement")
        }

        var deblaye = Number.isInteger(json_installation.deblaye) && (json_installation.deblaye == 0 || json_installation.deblaye == 1)
        if (!deblaye) {
            alert("Votre champ deblaye doit être 0 ou 1 uniquement")
        }

        var condition = (json_installation.condition != null && json_installation.condition != "" && json_installation.condition.length <= 255)
        if (!condition) {
            alert("Vous devez entrer entre 1 et 255 caractères pour la condition de la glissade")
        }

        validated = nom && nom_arr && cle && date_maj && ouvert && deblaye && condition

    } else if (installation === 'patinoire') {
        var nom_pat = (json_installation.nom_pat != null && json_installation.nom_pat != "" && json_installation.nom_pat.length <= 255)
        if (!nom_pat) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de la patinoire")
        }

        url = '/api/patinoire/' + json_installation.nom_pat;
        var reponse = await nom_existe(url, 'patinoire', nom_request, style_request);
        if (reponse) {
            alert("Le nom de la patinoire existe déjà")
        }

        var nom_arr = (json_installation.nom_arr != null && json_installation.nom_arr != "" && json_installation.nom_arr.length <= 255)
        if (!nom_arr) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de l'arrondissement")
        }

        validated = nom_pat && nom_arr

    } else if (installation === 'piscine') {
        var id_uev = Number.isInteger(json_installation.id_uev)
        if (!id_uev) {
            alert("Vous devez entrer un entier valide pour l'id_uev de la piscine")
        }

        var style = (json_installation.style != null && json_installation.style != "" && json_installation.style.length <= 255)
        if (!style) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le type de la piscine")
        }

        var nom = (json_installation.nom != null && json_installation.nom != "" && json_installation.nom.length <= 255)
        if (!nom) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de la piscine")
        }

        url = '/api/piscine/' + json_installation.style + '/' + json_installation.nom;
        var reponse = await nom_existe(url, 'piscine', nom_request, style_request);
        if (reponse) {
            alert("Le nom de la pisicne existe déjà")
        }

        var arrondisse = (json_installation.arrondisse != null && json_installation.arrondisse != "" && json_installation.arrondisse.length <= 255)
        if (!arrondisse) {
            alert("Vous devez entrer entre 1 et 255 caractères pour le nom de l'arrondissement")
        }

        var point_x = Number.isInteger(parseInt(json_installation.point_x))
        if (!point_x) {
            alert('Vous devez entrer un point_x de cette façon-ci: 304846,2071 ou 5039975909, par exemple')
        }

        var point_y = Number.isInteger(parseInt(json_installation.point_y))
        if (!point_y) {
            alert('Vous devez entrer un point_y de cette façon-ci: 304846,2071 ou 5039975909, par exemple')
        }

        var longitude_latitude = new RegExp(/^-?\d{2}\.\d{0,6}$/)
        var longitude = (longitude_latitude.test(json_installation.longitude))
        if (!longitude) {
            alert("Vous devez entrer une valeur valide, par exemple: -73.49941 ou 45.640521")
        }

        var latitude = (longitude_latitude.test(json_installation.latitude))
        if (!latitude) {
            alert("Vous devez entrer une valeur valide, par exemple: -73.49941 ou 45.640521")
        }

        validated = id_uev && style && nom && arrondisse && point_x && point_y && longitude && latitude
    }

    return validated;
}


let formulaire = document.querySelector("form");
formulaire.id = "recherche";

/**
 * Handler pour l'envoit du formulaire
 * @param {SubmitEvent} event
 */
document.getElementById("recherche").addEventListener("submit", async function(event) {
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
    var validated = await validateForm(json_installation, installation, nom_request, style_request);

    if (validated) {
        await fetch(url_fetch, {
            method:'PUT',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(json_installation, installation)
        })
        .then(response => {
            alert("L'installation a été modifiée avec succès")
            window.location.replace('/')
        })
    }
})
