# WindowsTools

**Une collection d'outils utiles pour Windows, développés en Python.**  
Chaque outil a été conçu pour répondre à des besoins spécifiques tout en restant simple d'utilisation.

## Outils disponibles

### 1. [`Check_Film.py`](https://github.com/IAidenI/WindowsTools/blob/main/Check_Film.py)
- **Description** : Scanne un dossier et ses sous-dossiers pour répertorier les fichiers (en excluant ceux avec l'extension `.srt`) et les dossiers.
- **Fonctionnalités** :
  - Génération d'un fichier `list.txt` contenant la liste des fichiers.
  - Identification des doublons avec un résumé détaillé :
    - Nombre total de fichiers analysés.
    - Nombre de dossiers analysés.
    - Nombre de doublons détectés.
- **Utilisation idéale** : Organiser et auditer les fichiers multimédias.

### 2. [`Solver_Polynome_Second_Degree.py`](https://github.com/IAidenI/WindowsTools/blob/main/Solver%20Polynome%20Second%20Degree.py)
- **Description** : Résout des équations polynomiales du second degré (de la forme `ax² + bx + c`).
- **Fonctionnalités** :
  - Deux modes de calcul disponibles :
    - Avec ou sans prise en compte des solutions complexes.
  - Vérification des étapes de calcul (simple ou détaillée).
  - Calcul des racines en fonction du discriminant (Δ).
- **Utilisation idéale** : Étudiants, enseignants ou amateurs de mathématiques.

### 3. [`Wifi_Find_Password.py`](https://github.com/IAidenI/WindowsTools/blob/main/Wifi_Find_Password.py)
- **Description** : Permet de retrouver les mots de passe Wi-Fi enregistrés sur un PC Windows.
- **Fonctionnalités** :
  - Affiche les réseaux Wi-Fi et leurs mots de passe enregistrés.
- **Utilisation idéale** : Récupérer facilement un mot de passe oublié.

### 4. [`auto_clicker.py`](https://github.com/IAidenI/WindowsTools/blob/main/auto_clicker.py)
- **Description** : Simule des clics continus de la souris à une position donnée.
- **Fonctionnalités** :
  - Réglage de la vitesse et de la durée des clics.
  - Prend en charge des scénarios automatisés répétitifs.
- **Utilisation idéale** : Automatisation de tâches répétitives.

### 5. [`BackgroundRemover.py`](https://github.com/IAidenI/WindowsTools/blob/main/BackgrundRemover/BackgroundRemover.py)
- **Description** : Supprime le fond d'une image PNG.
- **Fonctionnalités** :
  - Génère des images PNG avec un fond transparent.
- **Utilisation idéale** : Création rapide de visuels pour le web ou le design.

### 6. [`YoutubeDownloader.py`](https://github.com/IAidenI/WindowsTools/blob/main/YoutubeDownloader/YoutubeDownloader.py)
- **Description** : Télécharge des vidéos depuis un lien internet avec une interface graphique.
- **Fonctionnalités** :
  - Téléchargement rapide et efficace.
  - Inspiré de [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- **Utilisation idéale** : Enregistrer des vidéos pour une consultation hors ligne.

---

## Installation

1. **Pré-requis** :
   - [Python](https://www.python.org/) installé sur votre machine.
   - Les bibliothèques nécessaires (peuvent être installées via `pip` et `pip -r requirements.txt` si le fichier existe).

2. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre_nom/WindowsTools.git
   cd WindowsTools
