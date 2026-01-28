# Guide Présentation Python + Marp + GitHub Pages

**Python + 15 min + démo à la fin → Setup clean et fluide**

Configuration concrète, prête à copier, optimisée pour :

* Slides claires
* Code lisible
* Démo qui marche 🧘‍♂️

***

## ✅ Stack recommandée (simple & efficace)

👉 **Marp + GitHub Pages + repo unique**

### Pourquoi ?

* Tu écris vite en Markdown
* Zéro HTML à maintenir
* Export PDF *au cas où*
* Nickel pour 15 min

***

## 📁 Structure finale du repo

```text
mon-projet-python/
├── src/
│   ├── main.py
│   └── utils.py
├── slides/
│   ├── slides.md
│   └── index.html      # généré par Marp
├── demo/
│   └── demo.ipynb      # ou script dédié
├── requirements.txt
├── README.md
└── .gitignore
```

***

## 🧠 Plan de slides (15 min)

⏱️ **Rythme idéal : 1 slide ≈ 1 min**

```text
1. Titre & contexte (1 min)
2. Problème à résoudre (2 min)
3. Solution proposée (2 min)
4. Architecture (2 min)
5. Code clé (3 min)
6. Résultats / output (2 min)
7. Limites & améliorations (1 min)
8. Transition vers la démo (2 min)
```

👉 **La démo n'est pas dans les slides**, juste annoncée.

***

## 📝 Exemple `slides/slides.md`

````markdown
---
marp: true
theme: default
paginate: true
---

# Projet Python
### Démo + explication

---

## Le problème
- Trop lent
- Difficile à maintenir

---

## Architecture

```text
src/
 ├── main.py
 └── utils.py
```

---

## Fonction clé

```python
def process_data(data):
    return [x * 2 for x in data]
```

---

## Ce qu'on va voir maintenant

👉 Démo live du script

````

💡 **Astuce : ne mets jamais trop de code dans les slides.**

***

## 🌍 Mise en ligne avec GitHub Pages

### 1. Génère le HTML

```bash
marp slides/slides.md -o slides/index.html
```

### 2. GitHub → Settings → Pages

* **Branch**: `main`
* **Folder**: `/slides`

### 3. URL publique

```
https://tonpseudo.github.io/mon-projet-python
```

***

## 🧪 Démo live (zéro panique)

### Prépare un script dédié

```bash
python demo/run_demo.py
```

### ✅ Checklist AVANT la présentation

- [ ] Environnement virtuel prêt
- [ ] Données déjà téléchargées
- [ ] Commande copiée dans un fichier texte
- [ ] **Plan B : PDF exporté**

```bash
marp slides/slides.md -o slides.pdf
```

***

## 💎 Bonus pro (si tu veux briller)

### Tag git pour la version présentée

```bash
git tag presentation-v1
git push origin presentation-v1
```

### README avec liens directs

```markdown
# Mon Projet Python

📊 **Slides** : https://tonpseudo.github.io/mon-projet-python
▶️ **Lancer la démo** : `python demo/run_demo.py`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```
```

***

## 🎨 Thèmes Marp recommandés

### Thème par défaut (propre)

```markdown
---
marp: true
theme: default
---
```

### Thème Gaia (moderne)

```markdown
---
marp: true
theme: gaia
class: lead
---
```

### Thème Uncover (élégant)

```markdown
---
marp: true
theme: uncover
---
```

***

## 🚀 Installation Marp CLI

### Via npm

```bash
npm install -g @marp-team/marp-cli
```

### Via Homebrew (macOS)

```bash
brew install marp-cli
```

### Vérification

```bash
marp --version
```

***

## 📋 Template complet `slides.md`

````markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# [Nom du Projet]
## [Sous-titre]

**Présenté par** : [Ton Nom]
**Date** : [Date]

---

## 🎯 Objectif

En une phrase : ce que fait le projet

---

## ❓ Problème

- Point de douleur #1
- Point de douleur #2
- Point de douleur #3

---

## 💡 Solution proposée

**Notre approche** :

1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

---

## 🏗️ Architecture

```text
projet/
├── src/
│   ├── core.py
│   └── utils.py
├── tests/
└── data/
```

---

## 🔑 Code clé #1

```python
def fonction_importante(input_data):
    """
    Description brève
    """
    result = process(input_data)
    return result
```

---

## 🔑 Code clé #2

```python
class MonAlgorithme:
    def __init__(self):
        self.data = []
    
    def run(self):
        return self._compute()
```

---

## 📊 Résultats

| Métrique | Avant | Après |
|----------|-------|-------|
| Temps    | 10s   | 2s    |
| Précision| 75%   | 92%   |

---

## ⚠️ Limites & Améliorations

**Limites actuelles** :
- [Limite 1]
- [Limite 2]

**Améliorations futures** :
- [Amélioration 1]
- [Amélioration 2]

---

## 🎬 Démo

👉 **Passons à la démo live !**

```bash
python demo/run_demo.py
```

---

## 📚 Ressources

- **GitHub** : [lien]
- **Slides** : [lien]
- **Documentation** : [lien]

---

## Questions ?

Merci ! 🙏

````

***

## 🛡️ Checklist anti-fail pour la démo

### Avant le jour J

- [ ] Teste la démo 3 fois minimum
- [ ] Prépare des données de test légères
- [ ] Note les commandes dans un fichier texte
- [ ] Vérifie les dépendances (`pip freeze > requirements.txt`)
- [ ] Exporte le PDF de backup

### Le jour J

- [ ] Ouvre le terminal dans le bon dossier
- [ ] Active l'environnement virtuel
- [ ] Prépare le script de démo ouvert dans l'éditeur
- [ ] Teste une dernière fois 5 min avant
- [ ] Garde le PDF ouvert en plan B

***

## 🎯 Commandes essentielles Marp

### Générer HTML

```bash
marp slides/slides.md -o slides/index.html
```

### Générer PDF

```bash
marp slides/slides.md -o slides.pdf
```

### Watch mode (auto-refresh)

```bash
marp -w slides/slides.md
```

### Serveur local pour preview

```bash
marp -s slides/
```

***

## 🔥 Tips pour briller en démo

### 1. Prépare un script `demo/run_demo.py`

```python
"""
Démo du projet - Version présentation
"""

def main():
    print("🚀 Démarrage de la démo...")
    
    # Import local
    from src.main import process_data
    
    # Données de test légères
    test_data = [1, 2, 3, 4, 5]
    
    print(f"📥 Input : {test_data}")
    
    # Traitement
    result = process_data(test_data)
    
    print(f"📤 Output : {result}")
    print("✅ Démo terminée !")

if __name__ == "__main__":
    main()
```

### 2. Garde un fichier `DEMO_COMMANDS.txt`

```text
# Commandes démo (copier-coller)

# 1. Activer l'environnement
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 2. Lancer la démo
python demo/run_demo.py

# 3. Alternative si problème
python src/main.py --demo
```

### 3. Prépare des screenshots

Si la démo plante :

* Capture d'écran des résultats
* Intègre dans les slides (dernière slide cachée)

***

## 📦 Exemple complet de `README.md`

```markdown
# Mon Projet Python

Description courte du projet.

## 📊 Présentation

- **Slides en ligne** : https://username.github.io/mon-projet
- **PDF** : [slides/slides.pdf](slides/slides.pdf)

## 🚀 Installation

```bash
# Cloner le repo
git clone https://github.com/username/mon-projet.git
cd mon-projet

# Créer environnement virtuel
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Installer dépendances
pip install -r requirements.txt
```

## ▶️ Usage

### Démo rapide

```bash
python demo/run_demo.py
```

### Utilisation normale

```bash
python src/main.py --input data/sample.csv
```

## 🧪 Tests

```bash
pytest tests/
```

## 📁 Structure

```text
mon-projet/
├── src/           # Code source
├── demo/          # Scripts de démo
├── slides/        # Présentation Marp
├── tests/         # Tests unitaires
└── data/          # Données d'exemple
```

## 🤝 Contribuer

Les contributions sont bienvenues !

## 📄 Licence

MIT
```

***

## 🎬 Checklist finale (jour J)

### 30 min avant

- [ ] Ordinateur chargé (100%)
- [ ] Connexion internet testée (si besoin GitHub Pages)
- [ ] Terminal ouvert dans le bon dossier
- [ ] Environnement virtuel activé
- [ ] Démo testée une dernière fois

### 5 min avant

- [ ] Slides ouvertes (navigateur)
- [ ] PDF de backup ouvert (plan B)
- [ ] Script de démo ouvert dans VSCode
- [ ] Terminal prêt avec commande copiée
- [ ] DEMO_COMMANDS.txt visible

### Pendant la présentation

- [ ] Respire 🧘‍♂️
- [ ] Si la démo plante → montre le screenshot
- [ ] Garde le sourire
- [ ] Explique ce qui devrait se passer

***

**Prêt à tout déchirer ! 🚀**
