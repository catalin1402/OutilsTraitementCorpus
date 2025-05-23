# OutilsTraitementCorpus

## TP1
### Partie 1 | étude de cas CoNLL 2003 :
1. Quel type de tâche propose CoNLL 2003 ?
=> CoNLL 2003 permet la reconnaissance d’entités nommées.

2. Quel type de données y a-t-il dans CoNLL 2003 ?
=> Il y a huit fichiers de données qui couvrent l’anglais et l’allemand. Pour chacune des deux langues, il y a un fichier d’entraînement, un fichier de développement, un fichier de test et un grand fichier de données non-annotées. Les données utilisées sont des articles de Reuters pour l’anglais et des articles de Frankfurter Rundshau pour l’allemand.

3. A quel besoin répond CoNLL 2003 ?
=> CoNLL 2003 répond au besoin de réaliser des annotations d’entités nommées dans un texte de manière automatique.

4. Quels types de modèles ont été entraînés sur CoNLL 2003 ?
=> Des modèles d’entropie maximale, des modèles de Markov cachés, des modèles de champ aléatoire conditionnel (Conditional Random Fields) ont été entraînés sur CoNLL 2003. Des modèles basés sur les transformers (comme BERT) ont également été entraînés sur ce corpus.

5. Est un corpus monolingue ou multilingue ?
=> Il s’agit d’un corpus bilingue car il contient des données en anglais et en allemand.

### Partie 2 | projet:
Définissez les besoins de votre projet:
1. Dans quel besoin vous inscrivez vous ?
   => Il s'agit d'une analyse automatisée du contenu médiatique (presse écrite plus particulièrement) pour mieux comprendre les thématiques traitées dans la presse.
2. Quel sujet allez vous traiter ?
   => Le sujet traité est l'identification automatique des thématiques dans un corpus d’articles de presse. Pour ce projet, les thématiques choisies sont "culture" et "sport".
3. Quel type de tâche allez vous réaliser ?
   => Il s'agit d'une tâche de classification supervisée.
4. Quel type de données allez vous exploiter ?
   => Les données exploitées sont des données textuelles (titres et contenu des articles). Le corpus est composé de 20 articles de sport et de 20 articles de culture.
5. Où allez vous récupérer vos données ? sont-elles libres d'accès ?
   => Les données sont récupérées sur des journaux en ligne. Pour chacun des deux thèmes, 5 articles sont selectionnés dans chacune des 4 sources suivantes : Le Monde, Midilibre, Le Parisien, L'Express. Les articles sont libres d’accès (le contenu n'est pas utilisé à des fins commerciales et n'est pas republié tel quel. De plus, les politiques de scraping du fichier robot.txt ont été respectées).
