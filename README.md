# Cellular Automations 
Some of the most known celular automatons, you can also create your own game of life on the folder “your own cellular automata”  
## How it works (french, english translation may come in the future):
Sur la majorité des automates, je ne garde en mémoire seulement les positions où il y'a une case dans un dictionnaire ou une liste, afin d'éviter de devoir créer une liste très grande ne contenant majoritairement du vide.  
Cepandant, [your own rules](./'your own rules') stoque différement les cases : la grille est en fait un très grand nombre entier, où l'on s'interesse à la représentation binaire de ce nombre.  
### Exemple :
Prenons la grille :
`
001
011
101
`
on aligne ensuite chaque ligne: 
'001 011 101'
On obtient alors un nombre binaire, qui vaut en base 10 : 93  
Cette solution n'est peut être pas la meilleure au niveau spatial (je force la manipulation d'un très très grand nombre) mais au niveau temporel, je n'utilise qu'une seule entité auquelle je ne performe que de très simples actions (changer la valeur à l'indice n) sans utiliser de liste
