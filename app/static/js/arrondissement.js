// Ajoute l'entete du tableau
function headers(table, keys) {
    var row = table.insertRow();
    for( var i = 0; i < keys.length; i++ ) {
        var cell = row.insertCell();
        cell.scope = 'col'
        cell.className = 'header-table'
        cell.appendChild(document.createTextNode(keys[i]));
    }
    var update = row.insertCell();
    update.scope = 'col';
    update.className = 'header-table';
    update.id = 'modifier_table'
    update.appendChild(document.createTextNode('Modifier'));

    var errase = row.insertCell();
    errase.scope = 'col';
    errase.className = 'header-table'
    errase.id = 'supprimer_table'
    errase.appendChild(document.createTextNode('Suprimer'));
}

// Lancee lorsque la recherche pour un arrondissement est lancee
async function arrondissementRecherche(arrondissement, id_table) {
    var table = document.createElement('table');
    table.className = 'table table-striped'
    document.getElementById(id_table).appendChild(table);

    if (!(arrondissement === "")) {
        await fetch("/api/installations?arrondissement="+arrondissement)
        .then(response => response.text())
        .then(response => JSON.parse(response))
        .then(response => {
            if (response.error) {
                console.log(response)
                return response
            } else if (id_table === "glissades") {
                return JSON.parse(response.glissades)
            } else if (id_table === "patinoires" ) {
                return JSON.parse(response.patinoires)
            } else if (id_table === "piscines") {
                return JSON.parse(response.piscines)
            } else {
                console.log("Erreur avec le serveur :", err);
            }
        })
        .then(response => {
            if (response.length != 0 && !response.error) {
                headers(table, Object.keys(response[0]));
                for( var i = 0; i < response.length; i++ ) {
                    var r = response[i];
                    var row = table.insertRow();
                    Object.keys(r).forEach(function(k) {
                        var cell = row.insertCell();
                        cell.scope = 'row'
                        cell.appendChild(document.createTextNode(r[k]));
                    })
                    // Ajout du bouton de modification
                    var cell = row.insertCell();
                    var image_update = document.createElement('img');
                    image_update.src = 'update.png';
                    image_update.width = '20';
                    image_update.height = '20';
                    image_update.id = 'image_update'
                    cell.scope = 'row';
                    cell.appendChild(image_update);

                    // Ajout du bouton de suppression
                    cell = row.insertCell();
                    var image_delete = document.createElement('img');
                    image_delete.src = 'delete.png'
                    image_delete.width = '20';
                    image_delete.height = '20';
                    image_delete.id = 'image_delete'
                    cell.scope = 'row';
                    cell.appendChild(image_delete);
                }
            }
        })
        .catch(err => {
            console.log("Erreur avec le serveur :", err);
        });
    }
}

document.getElementById("recherche").addEventListener("submit", arrondissementRecherche(arr, 'glissades'))
document.getElementById("recherche").addEventListener("submit", arrondissementRecherche(arr, 'patinoires'))
document.getElementById("recherche").addEventListener("submit", arrondissementRecherche(arr, 'piscines'))