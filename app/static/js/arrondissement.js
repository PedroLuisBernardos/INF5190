function headers(table, keys) {
    var row = table.insertRow();
    for( var i = 0; i < keys.length; i++ ) {
        var cell = row.insertCell();
        cell.scope = 'col'
        cell.className = 'header-table'
        cell.appendChild(document.createTextNode(keys[i]));
    }
}

// Lancee lorsque la recherche pour un arrondissement est lancee
async function arrondissementRecherche(arrondissement, id_table) {
    var table = document.createElement('table');
    table.className = 'table table-striped'
    document.getElementById(id_table).appendChild(table);

    if (!(arrondissement === "")) {
        await fetch("/api/installations/"+arrondissement)
        .then(response => response.text())
        .then(response => JSON.parse(response))
        .then(response => {
            if (id_table === "glissades") {
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
            console.log(response)
            if (response.length != 0) {
                headers(table, Object.keys(response[0]));
                for( var i = 0; i < response.length; i++ ) {
                    var r = response[i];
                    var row = table.insertRow();
                    Object.keys(r).forEach(function(k) {
                        console.log(k);
                        var cell = row.insertCell();
                        cell.scope = 'row'
                        cell.appendChild(document.createTextNode(r[k]));
                    })
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