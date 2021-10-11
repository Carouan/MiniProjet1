"""
Spec function account creation
 def account_creation (name(String))
  # Check if player exists else create it.
 Parameters
   name : player name (Str)
 Raises
   Value error : Player already exists
 Returns
   Result : New account created (name: name of new player (String) money: money of the new player (Int))


Evitez les raises et try/except.
Soit vous conditionnez l'appel à la fonction pour être certains que l'utilisateur n'existe pas encore,
soit vous ignorez la création lorsque l'utilisateur est déjà présent.

Est-ce réellement utile de renvoyer 'name' ?
Car vous semblez déjà avoir cette information avant d'appeler la fonction (vu que vous le passez en paramètre).


"""
import gaming_tools

def player_managment(name):

    if gaming_tools.player_exists(name) :
        playermoney = gaming_tools.get_player_money(name)
        txt = "Player "+ name + " already exists and has {} \n"
        print(txt.format(playermoney))
        #print ("Would you like to create a new player ?")




    else :
        gaming_tools.add_new_player(name)
        gaming_tools.set_player_money(name,225)
        print ("Player "+ name + " is created with 225 credits \n")
