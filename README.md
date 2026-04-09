# CC2-Hadoop

### 🎬 Analyse des Tags MovieLens avec Hadoop

6
📌 Présentation

Ce projet consiste à analyser le fichier tags.csv du dataset MovieLens (25M) à l’aide de Hadoop et du modèle MapReduce.

L’objectif est de comprendre comment les utilisateurs décrivent les films à travers des tags.

### ⚙️ Technologies utilisées

Python 🐍
Hadoop (HDFS + MapReduce)
MRJob
Dataset MovieLens
### 📊 Résultats obtenus

Les traitements réalisés permettent de répondre à plusieurs questions :

🎥 Combien de tags possède chaque film
👤 Combien de tags chaque utilisateur ajoute
🏷️ Fréquence d’utilisation des tags
🔗 Nombre de tags par utilisateur et par film
📁 Fichiers de résultats

Les résultats sont disponibles dans le repository :

output_tags_movie.txt
output_tags_user.txt
output_tags_count.txt
output_tags_user_movie.txt

👉 Chaque fichier correspond à une analyse MapReduce.

💡 Exemple de résultat
"1"     697
"10"    137
"100"   18

➡️ Certains films sont beaucoup plus annotés que d'autres.

### 🧠 Ce que j’ai appris

Utiliser Hadoop pour traiter des données massives
Comprendre le fonctionnement de HDFS
Implémenter des jobs MapReduce en Python
Manipuler un dataset réel à grande échelle
