#Versionning des paquets python
On peut installer différent version d'un paquet

exemple:

    - pip install requests==2.1.0
    - pip install requests~=2.2 (installera la version la plus haut dessus de 2 mais pas des version ultérieurs)
    - pip install requests~=2.1.0 (installera la version la plus élevée disponible au-dessus de 2.1.0  , mais pas la version 2.2.0  ni les versions ultérieures.)
    - pip install requests>2.5.0 (install la version la plus élevé au dessus de 2.5)
    - pip install "requests>2.4.0,<2.6.0" (installera la version la plus élevée disponible supérieure à 2.4.0  , mais inférieure à 2.6.0)
    
    
Pour désinstaller un paquet

    - pip uninstall <package> 

#Environnement virtuel

    - python -m venv 'nomEnv' (env par conviction) crée un nouveau environnement
    - source env/bin/activate (active l'environnement)
    - pip freeze
    
   On peut passer d'un env à un autre en aller juste dans le dossier en question et lancer la commande "source env/bin/activate" 
    Il est important de crée un fichier requiremets.txt pour lister les paquets nécessaires au projet
    
    Utiliser
        - pip freeze > requirement.txt (met le contenu de pip freeze dans requirement.txt
        - pip install -r requirements.txt (install tout ce qui y a dans requirements.txt)
        
    Supprimer un environnement virtuelle
        - rm -rf env
   
   
loop:

```
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste):
print("À l'indice {} se trouve {}.".format(i, elt))
```
la fonction enumerate permet de récuper un object des indices et des valeurs

On peut facilement filtrer une liste en utilisant cette syntax

```
nouvelle_squence = [element for element in ancienne_squence if condition]
```

On peut parcourirs des dictionnaires comme les list:
```
fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
# on peut aussi utiliser value ou keys comme fonction
print("La clé {} contient la valeur {}.".format(cle, valeur)) 

```


para non nommé se retrouveront dans liste et para nommée se routreveront dans dic
```
def fonction_inconnue(*en_liste, **en_dictionnaire):

```

##Fichier

On peut ouvrir un fichier en utilisant la méthode open qui n'as pas besoin d'être importé

```python
mon_fichier = open("fichier.txt", "w")
mon_fichier.write("Premier test d'écriture dans un fichier via Python")
mon_fichier.close()
```
On peut utiliser plusieurs méthodes pour manipuler un fichier

r == read
w == write
a == append

On peut utiliser le module pickle pour enregistrer des obj dans des fichiers et des les rechargers par la suite

Python fonctionne de la même manière que js au niveau des références

Pour faire une copie d'un tableau qui ne pointera pas vers le tableau d'origin on peut utilise list() ou dict()

On peut préciser à function qu'on utilise une variable global en ajoutant un mot clef global devant la variable global a utiliser,
Celà nous permettra d'utiliser la variable en lecture et en écriture

exemple:
```python
i = 4
def inc_i():
    global i
i += 1
```

Si on ne précise pas que se sont des variables globals on ne pourrait y acceder qu'en lecture seule


