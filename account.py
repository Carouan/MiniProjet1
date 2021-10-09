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

def account_managment (name)

player_exists(name)

add_new_player(name)

set_player_money(name,money)
