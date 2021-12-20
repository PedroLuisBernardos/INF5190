# INF5190-A21 - Projet de session

Le but de ce projet est d'utiliser des données de la ville de Montréal pour construire une base de données et manipuler les tables avec des requêtes REST.

### Crédits

Les icônes ont été prises du site: http://www.onlinewebfonts.com/icon

Jacques Berger

## :clipboard: Prérequis

- VirtualBox: https://www.virtualbox.org/wiki/Downloads
- Vagrant: https://www.vagrantup.com/downloads.html
- git: https://git-scm.com/downloads
- Les extensions de virtualisation (VT-x ou AMD-V) doivent être activées dans le BIOS de votre ordinateur.


## :wrench: Installation

> :warning: L'exécution de la commande `vagrant up` prend plusieurs minutes à se compléter. Créez un répertoire vide et placez-y le Vagrantfile et le fichier [requirements.txt](requirements.txt).

### Linux / MacOS

Dans un terminal:

```bash
$ vagrant up
```

### Windows

Dans PowerShell::

```bash
vagrant.exe up
```

## :shell: Autres commandes

### Ouvrir une connexion SSH sur la machine virtuelle:

```bash
$ vagrant ssh
```

### Sortir de la machine virtuelle:

```bash
$ vagrant@vagrant$ exit
```

### Supprimer la machine virtuelle et libérer l'espace disque:

```bash
$ vagrant destroy
```
### Arrêter la machine virtuelle

```bash
$ vagrant halt
```

### Redémarrer la machine virtuelle

```bash
$ vagrant reload
```

## :bomb: Troubleshooting

### VT-x is disabled in the BIOS for all CPU modes

Le message suivant peut subvenir lors de la première exécution de Vagrant:

    VBoxManage.exe: error: Not in a hypervisor partition (HVP=0) (VERR_NEM_NOT_AVAILABLE).
    VBoxManage.exe: error: VT-x is disabled in the BIOS for all CPU modes (VERR_VMX_MSR_ALL_VMX_DISABLED)

Les architectures Intel requièrent parfois l'activation des extensions de virtualisation (VT-x) dans le BIOS de votre ordinateur. Vérifiez la documentation du manufacturier pour savoir comment entrer dans le BIOS (généralement en appuyant sur F2 ou F12 au boot). Vous pourrez alors activer l'option.

L'option équivalente pour les architectures AMD (AMD-V) est habituellement déjà activée et la modification du BIOS n'est pas nécessaire.


### The guest machine entered an invalid state while waiting for it to boot.

Ce message d'erreur vagrant peut apparaître pour différentes raisons.

Vérifiez d'abord que les extensions de virtualisation sont activées dans le BIOS et que vous utilisez une version à jour de VirtualBox et que celle-ci est adéquate pour votre système d'exploitation.

L'exécution de la commande `vagrant reload` peut être suffisante pour régler le problème. L'exécution de `vagrant destroy` puis de `vagrant up` pourrait être nécessaire.


## Développement avec Python3 et Flask

### Activation de l'environnement virtuel

Une fois connecté sur la VM, il faut activer l'environnement virtuel de Python avec la commande suivante.

```bash
$ source /home/vagrant/inf5190_projet_venv/bin/activate
```

### Répertoire partagé entre l'ordinateur hôte et la VM

Le répertoire où vous avez lancé le `vagrant up` sera disponible dans la VM sous `/vagrant`

### Installation des dépendances

```bash
$ cd /vagrant
$ make install
```

### Partir l'API

Lancer la commande suivante:

```bash
$ make run
```

### Tests dans un fureteur

Lors de la connexion à la VM via SSH, le système d'exploitation vous donnera
l'adresse IP de la VM. Prenez l'adresse IP de l'interface **eth1**.

Une fois l'application Flask lancée dans votre VM, utilisez le fureteur de votre ordinateur pour accéder à l'application Flask. Vous pouvez y accéder en utilisant l'adresse IP de eth1 et en spécifiant le port de Flask.
Exemple : http://192.168.50.12:5000/

### Documentation des services REST

Toute la documentation des services REST sera disponible à la route `/doc`.

### Déploiement sur Heroku

L'API est aussi disponible sur [Heroku](https://inf5190-projet-berp01039907.herokuapp.com).
