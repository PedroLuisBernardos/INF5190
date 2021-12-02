/**
 * Affiche les informations selon un nom d'installation
 * @param {*} nom_installation nom d'installation choisi
 */
async function nomInstallationAffichage(nom_installation) {
    let installation = document.getElementById("installation");
    await fetch("/api/installation/"+nom_installation)
    .then(response => response.text())
    .then(response => {
        installation.innerHTML = response;
        installation.value = "";
    })
    .catch(err => {
        console.log("Erreur avec le serveur :", err);
    });
}

document.getElementById("recherche").addEventListener("submit", nomInstallationAffichage(nom_installation))