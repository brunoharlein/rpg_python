Au travers de cet exercice, ils apprennent à :
- Utiliser l'héritage
- Utiliser et redéfinir des méthodes spéciales
- Utiliser les attributs et les méthodes de classe
- Utiliser les décorateurs existants
- Organiser leur code
- Prendre en compte l'utilisateur final dans la production de l'application

## Consignes

Spécifications fonctionnelles :
- Le joueur peut choisir le type de personnage qu'il souhaite incarner
- Trois classes sont disponibles pour le joueur (guerrier, archer, magicien)
- Le joueur peut nommer son personnage comme il le désire au début du jeu
- Trois classes sont disponibles pour les ennemis (orc, loup, zombie)
- Les personnages ont tous au minimum les caractéristiques suivantes (vie, attaque, défense, agilité, nom)
- Le magicien dispose en plus de mana représentant sa force magique
- Un personnage peut en attaquer un autre, la cible perd alors de la vie en proportion de sa valeur de défense et de la valeur d'attaque de l'assaillant
- Le magicien peut se soigner. Ce sort consomme du mana mais lui redonne de la vie. S'il n'a pas assez de mana, il ne peut pas le lancer
- Un combat est simulé entre le personnage du joueur et un ennemi de votre choix jusqu'à ce que l'un ou l'autre des personnages soit mort. Assurez de tester que la méthode soin du magicien soit fonctionnelle


## Pour aller plus loin

Vous pouvez par la suite essayer de transformer votre application en un jeu partiellement fonctionnel. Vous pouvez par exemple rajouter les fonctionnalités suivantes :
- Un narrateur qui raconte une histoire pour donner de la profondeur à votre jeu
- Des temps de pause et de transition pour donner du rythme à votre histoire
- Une console interactive pour les combats, autrement dit, le joueur peut choisir lui-même l'action à exécuter (attaquer, se soigner...) et le combat ne se poursuit pas tant qu'il n'a pas choisi
- Rajouter une méthode fuite qui offre aux personnages une faible chance de quitter le combat sans se battre
- Afficher en temps réel les informations de chaque protagoniste du combat (sa vie et éventuellement son mana si c'est un magicien)
- S'assurer que l'utilisateur ne puisse pas rentrer de commandes non-prévues ou lancer une action qui n'appartient pas à sa classe. Par exemple un archer ne peut pas lancer un sort de soin.



Through this exercise, they learn to:
- Use inheritance
- Use and redefine special methods
- Use attributes and class methods
- Use existing decorators
- Organize their code
- Take into account the end user in the production of the application

## Instructions

Functional Specifications :
- The player can choose the type of character he wishes to embody
- Three classes are available for the player (warrior, archer, magician)
- The player can name his character as he wishes at the start of the game
- Three classes are available for enemies (orc, wolf, zombie)
- The characters all have at least the following characteristics (life, attack, defense, agility, name)
- The magician has more mana representing his magic force
- A character can attack another, the target then loses life in proportion to its defense value and the attacker's attack value
- The magician can heal himself. This spell consumes mana but gives it new life. If he doesn't have enough mana, he can't cast it
- A fight is simulated between the player character and an enemy of your choice until one or the other of the characters is dead. Make sure to test that the magician's care method is functional


## For further

You can then try to turn your application into a partially functional game. You can for example add the following features:
- A narrator who tells a story to give depth to your game
- Break and transition times to give rhythm to your story
- An interactive console for fighting, in other words, the player can choose himself the action to perform (attack, heal ...) and the fight does not continue until he has chosen
- Add a leak method that gives characters a low chance of leaving the fight without fighting
- Display in real time the information of each protagonist of the fight (his life and possibly his mana if he is a magician)
- Ensure that the user cannot enter unexpected commands or initiate an action that does not belong to his class. For example, an archer cannot cast a healing spell.