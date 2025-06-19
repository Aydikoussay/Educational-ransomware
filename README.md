# 🦠 Educational Ransomware Simulator (Python)

> ⚠️ **Projet à but pédagogique uniquement.** Ce simulateur chiffre réellement des fichiers localement à l’aide de l’AES, mais n’exfiltre aucune donnée. N’exécutez ce script que dans une **machine virtuelle** ou un **environnement de test isolé**.

---

## 📌 Présentation

Ce projet est un **simulateur de ransomware éducatif** développé en Python. Il permet de découvrir le fonctionnement de base d’un ransomware à travers :

- Le parcours et le chiffrement des fichiers d’un dossier
- La génération et la gestion d’une clé AES (Fernet)
- L’affichage d’une fausse **note de rançon**
- Un script de **déchiffrement** pour restauration

> Idéal pour apprendre les bases du **chiffrement symétrique** et de la **cybersécurité offensive/éducative**.

---

## ⚙️ Fonctionnalités principales

- 🔐 Chiffrement AES-256 (via `cryptography.fernet`)
- 📁 Parcours récursif d’un répertoire cible
- 🗝️ Génération automatique de la clé de chiffrement
- 📝 Affichage d’une note de rançon simulée dans le terminal
- 🔓 Script de déchiffrement inclus pour tests

---

## 🧰 Technologies utilisées

- Python 3.x
- [cryptography](https://cryptography.io/en/latest/) — chiffrement AES/Fernet

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Aydikoussay/Educational-ransomware.git
cd Educational-ransomware
```
### 2. Installer la dépendance principale
```bash
pip install cryptography
