// Supprime l'installation
function update_inst(url) {
    fetch(url, {method:'PUT'})
    .then(response => {
        alert('hello')
        window.location.replace(url);
    });
}

document.getElementById("recherche").addEventListener("submit", update_inst(url))
