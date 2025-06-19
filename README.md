# 🦠 Educational Ransomware Simulator (Python)

> ⚠️ **Ce projet est uniquement à but pédagogique. N'exécutez ce script que dans une machine virtuelle ou un environnement de test contrôlé.** Il ne vole, n’exfiltre ni ne chiffre de données sensibles – mais il chiffre réellement des fichiers localement avec AES.

---

## 📌 Description

Ce simulateur de ransomware est un outil éducatif écrit en Python. Il parcourt un dossier local, chiffre les fichiers à l’aide d’AES-256 (via la bibliothèque `cryptography`), puis affiche une fausse note de rançon. Le projet est conçu pour apprendre :

- Le fonctionnement basique d’un ransomware
- Le chiffrement symétrique avec AES
- La sécurité des fichiers locaux
- Les bonnes pratiques de protection contre ce type d’attaque

---

## ⚙️ Fonctionnalités

- 🔐 Chiffrement de fichiers avec AES (Fernet)
- 🔎 Parcours récursif d’un dossier
- 🗝️ Génération et sauvegarde automatique de la clé
- 💬 Affichage d’une note de rançon fictive
- ✅ Script de déchiffrement inclus

---

## 🧰 Technologies utilisées

- Python 3.x
- [`cryptography`](https://cryptography.io/en/latest/)

---

## 🚀 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-utilisateur/educational-ransomware.git
cd educational-ransomware
---


## Installez les dépendances :
```bash
pip install cryptography

