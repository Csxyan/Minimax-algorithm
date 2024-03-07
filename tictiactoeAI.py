import numpy as np
from numpy import Infinity

# Variables

Player, AI = 1, 2
PlayerTurn, AITurn = True, False


def endAsPlayerWin(): 
   
   #Cette fonction termine la partie avec le joueur comme gagant.

   print("Vous avez gagné !")
   exit()

def endAsAIWin(): 
   
   #Cette fonction termine la partie avec l'IA comme gagante.
   
   print("Vous avez perdu, Victoire de l'IA !")
   exit()

def draw(): 
   
   # Cette fonction termine la partie avec une égalité

   print("Egalite !")
   exit()

def show(): 
   
   # Cette fonction affiche la matrice du jeu.

   print(gametab)

def isMovesLeft(board) :  

    # Cette fonction permet vérifié qu'il reste des coups à jouer.
  
    for i in range(3) : 
        for j in range(3) : 
            if (board[i][j] == 0) : 
                return True 
    return False
  
def evaluate(tab) :  

    # Cette fonction va permettre entre autre d'attribué un score à une situation du jeu,
    # +10 si l'IA gagne
    # -10 si le Joueur gagne
    # Cela permettra à minimax de connaitre les sitations favorable à l'IA
    
    # Lignes
    for row in range(3) :      
        if (tab[row][0] == tab[row][1] and tab[row][1] == tab[row][2]) :         
            if (tab[row][0] == AI) : 
                return 10
            elif (tab[row][0] == Player) : 
                return -10
    
    # Colonnes
    for col in range(3) : 
       
        if (tab[0][col] == tab[1][col] and tab[1][col] == tab[2][col]) : 
          
            if (tab[0][col] == AI) :  
                return 10
            elif (tab[0][col] == Player) : 
                return -10
  
    # Diagonales
    if (tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2]) : 
      
        if (tab[0][0] == AI) : 
            return 10
        elif (tab[0][0] == Player) : 
            return -10
    if (tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0]) : 
      
        if (tab[0][2] == AI) : 
            return 10
        elif (tab[0][2] == Player) : 
            return -10

    return 0
  

def minimax(board, depth, isMax) :  

    # La foncion minimax est une fonction qui apporte la notion de récursivité

    # Dans un premier temps, on compare le score actuel du jeu avec les conditions de victoire.
    # Cela permettra de mettre fin à la récursivité de minimax 
    # (Si un joueur gagne, cela représente la fin, sinon minimax jouerait jusqu'à que la matrcice soit remplie sans prendre en compte la victoire)

    score = evaluate(board) 
   
    if (score == 10) :  
        return score - depth
  
    if (score == -10) :     
        return score + depth

    if (isMovesLeft(board) == False) : 
        return 0
    
    # 2 possiblités, Etre le maximiseur et chercher les situations qui renvoie le meilleur score
    # Etre le minimiseur et chercher les sitations qui renvoie le score le plus faible
  
    if (isMax) :      
        best = -Infinity 

        # Dans le jeu donné, a chaque case non jouée soit vide
        # Minimax va jouer la case et constaté l'état en simulant toute une partie avec toutes les possibilités pour les 2 joueurs
        # Et cela pour toutes les cases restantes du jeu,

        # Enfin une fois arrivé à une situation de fin, soit un joueur gagne, il renverra le score 
        # avec comme malus la profondeur de jeu parcouru
        # ainsi Minimax ne veut pas seulement gagner ou éviter de perdre
        # Il veut le faire le plus vite possible
    
        for i in range(3) :          
            for j in range(3) :  
                if (board[i][j]==0) :  
                    board[i][j] = AI
                    best = max( best, minimax(board, depth + 1, False))  
                    board[i][j] = 0

        return best 
  
    else : 
        best = Infinity 
        for i in range(3) :          
            for j in range(3) : 
                
                if (board[i][j] == 0) :  
                    board[i][j] = Player
                    best = min(best, minimax(board, depth + 1, True))  
                    board[i][j] = 0


        return best 

def findBestMove(board) :  

    # Cette fonction a pour but d'utiliser minimax détaillé plus tôt pour determiné avec un jeu actuel donné 
    # le meilleur coup possible à jouer dans l'optique de gagner puis éviter de perdre.

    # Le principe est simple
    # A chaque coup, on récupère le score, si le score est plus élevé que le précédent ou le garde, lui et ses coordonées.
    # Ici en tant que Maximiseur

    bestVal = -Infinity
    bestMove = (-1, -1)  

    for i in range(3) :      
        for j in range(3) : 
           
            if (board[i][j] == 0) :  
                board[i][j] = AI
                moveVal = minimax(board, 0, False)   
                board[i][j] = 0
   
                if (moveVal > bestVal) :                 
                    bestMove = (i, j) 
                    bestVal = moveVal 
  
    return bestMove 

def Playerturn(): 
   
   # Cette fonction demande au Joueur de choisir un case puis envoie ses coordonées à la fonction IfIsAvailablePlay

   global PlayerTurn
   global AITurn
   if PlayerTurn == True:
       ligneJA = int(input("Veuillez choisir une ligne. \n"))
       columJA = int(input("Veuillez choisir une colonne \n"))
       IfIsAvailablePlay(ligneJA,columJA)
       AITurn = True
       PlayerTurn = False
       show()
       veriftab()
   else :
       AIturn()


def AIturn(): 
   
   # Cette fonction demande à l'IA de determiner le meilleur coup à joueur grace à la fonction findBestAIMove et 
   # envoie ses coordonées à IfIsAvailablePlay
   
   global AITurn
   global PlayerTurn
   if AITurn == True:
        posx, posy = findBestMove(gametab)
        IfIsAvailablePlay(posx,posy)
        PlayerTurn = True
        AITurn = False
        show()
        veriftab()
   else :
       Playerturn()


def nextround():
   
    # Cette fonction passe au tour suivant
   
   print("Tour suivant !")
   AIturn()
   Playerturn()


def init_game(): 
    
   # Cette fonction initialise le jeu en créant la matrice de jeu ( en GLOBAL !!)
   
   global gametab
   gametab = np.zeros([3, 3])
   print(gametab)


def veriftab(): 
       
       
# Cette fonction determine toutes les possibilités où un joueur remporte la partie et si ce n'est pas le cas passe au tour suivant


# Axis : 1 = Lignes ; 0 = colonnes


       #Lignes
       if np.any(np.all(gametab == [AI, AI, AI], axis=1)):
           endAsPlayerWin()
       elif np.any(np.all(gametab == [Player, Player, Player], axis=1)):
           endAsAIWin()


       #Colonnes
       elif np.any(np.all(gametab == [AI, AI, AI], axis=0)):
           endAsPlayerWin()
       elif np.any(np.all(gametab == [Player, Player, Player], axis=0)):
           endAsAIWin()


       #diagonales
       elif np.any(np.all(gametab.diagonal() == [AI, AI, AI])):
           endAsPlayerWin()
       elif np.any(np.all(gametab.diagonal() == [Player, Player, Player])):
           endAsAIWin()
       elif np.any(np.all(np.fliplr(gametab).diagonal() == [AI, AI, AI])):
           endAsPlayerWin()
       elif np.any(np.all(np.fliplr(gametab).diagonal() == [Player, Player, Player])):
           endAsAIWin()


       #Matrice remplie
       elif not isMovesLeft(gametab):
           draw()


       #Tour suivant
       else:
           nextround()


def IfIsAvailablePlay(posx,posy):
   
   # Cette fonction vérifie si une case est disponible et si oui la joue sinon renvoie un message d'erreur 

   # Pour l'IA pas besoin de vérifier si la case est déjà prise car cela est déjà pris en compte

   global PlayerTurn
   global AITurn


   if np.any(gametab[posx,posy] == 0) and PlayerTurn == True :
       gametab[posx, posy] = Player
   elif not np.any(gametab[posx,posy] == 0) and PlayerTurn == True :
       print("Case prise !")
       PlayerTurn = True
       AITurn = False
       Playerturn()


   if np.any(gametab[posx,posy] == 0) and AITurn  == True:
       gametab[posx, posy] = AI


def game(): 
   
   # Cette fonction qui pourrait être nommé main est la fonction centrale qui fait le lien
   # Elle lance le jeu

   init_game()
   Playerturn()
   AIturn()

game()



