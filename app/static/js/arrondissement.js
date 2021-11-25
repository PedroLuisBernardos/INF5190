// Ajoute l'entete du tableau
function headers(table, keys) {
    var row = table.insertRow();
    header_keys = Object.keys(keys[0]);
    for( var i = 0; i < header_keys.length; i++ ) {
        var cell = row.insertCell();
        cell.scope = 'col';
        cell.className = 'header-table';
        cell.appendChild(document.createTextNode(header_keys[i]));
    }

    var update = row.insertCell();
    update.scope = 'col';
    update.className = 'header-table';
    update.id = 'modifier_table';
    update.appendChild(document.createTextNode('Modifier'));

    var errase = row.insertCell();
    errase.scope = 'col';
    errase.className = 'header-table';
    errase.id = 'supprimer_table';
    errase.appendChild(document.createTextNode('Suprimer')); 
}

function getNom(r, type_installation) {
    if (type_installation === "glissades") {
        return r[Object.keys(r)[0]];
    } else if (type_installation === "patinoires" ) {
        return r[Object.keys(r)[1]];
    } else if (type_installation === "piscines") {
        return r[Object.keys(r)[2]];
    }
}

function getPrimaryKey(r, type_installation){
    if (type_installation === "glissades") {
        return r[Object.keys(r)[0]];
    } else if (type_installation === "patinoires" ) {
        return r[Object.keys(r)[0]] + r[Object.keys(r)[1]];
    } else if (type_installation === "piscines") {
        return r[Object.keys(r)[1]] + r[Object.keys(r)[2]];
    }
}

// Supprime l'installation
function supprimer(nom, type_installation) {
    alert(nom + type_installation);
}

// Lancee lorsque la recherche pour un arrondissement est lancee
async function arrondissementRecherche(arrondissement, type_installation) {
    var table = document.createElement('table');
    table.className = 'table table-striped'
    document.getElementById(type_installation).appendChild(table);

    if (!(arrondissement === "")) {
        await fetch("/api/installations?arrondissement="+arrondissement)
        .then(response => response.text())
        .then(response => JSON.parse(response))
        .then(response => {
            if (response.error) {
                console.log(response)
                return response
            } else if (type_installation === "glissades") {
                return JSON.parse(response.glissades)
            } else if (type_installation === "patinoires" ) {
                return JSON.parse(response.patinoires)
            } else if (type_installation === "piscines") {
                return JSON.parse(response.piscines)
            } else {
                console.log("Erreur avec le serveur :", err);
            }
        })
        .then(response => {
            if (response.length != 0 && !response.error) {
                headers(table, response);
                for( var i = 0; i < response.length; i++ ) {
                    var r = response[i];
                    var row = table.insertRow();
                    Object.keys(r).forEach(function(k) {
                        var cell = row.insertCell();
                        cell.scope = 'row'
                        if (typeof r[k] == "object"){
                            cell.appendChild(document.createTextNode(r[Object.keys(r)[1]].nom_arr));
                        } else {
                            cell.appendChild(document.createTextNode(r[k]));
                        }
                    })

                    var nom = getNom(r, type_installation);
                    //var primaryKey = getPrimaryKey(r, type_installation);
                    var type_inst = type_installation.slice(0, type_installation.length-1);

                    // Ajout du bouton de modification
                    var cell = row.insertCell();
                    var button_update = document.createElement('button');
                    button_update.type = 'button';
                    button_update.className = 'btn-styled';
                    button_update.innerHTML = '<img src="update.png" alt="Icone pour la modification" width=20 height=20/>';
                    button_update.class = 'image_update';
                    //button_update.id = primaryKey + '_update';
                    cell.scope = 'row';
                    cell.appendChild(button_update);

                    //document.getElementById(primaryKey+'_update').addEventListener("click", (nom, type_installation) => {
                    //    alert(nom + type_installation);
                    //});

                    // Ajout du bouton de suppression
                    cell = row.insertCell();
                    var button_delete = document.createElement('button');
                    button_delete.type = 'button';
                    button_delete.className = 'btn-styled';
                    button_delete.innerHTML = '<img src="delete.png" alt="Icone pour la suppression" width=20 height=20/>';
                    button_delete.class = 'image_delete';
                    button_delete.id = 'image_delete';
                    button_delete.name = '_delete';
                    button_delete.value = "/api/"+type_inst+"/"+nom;
                    cell.scope = 'row';
                    cell.appendChild(button_delete);
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
