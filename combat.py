""""
Règles de combat
1 seule attaque

water > fire
fire > plant
plant > water




    def  bestvariety (crea1, crea2)

get_creature1_variety





        if crea1 > crea2
            tempcrea1_strength = crea1_strength *2
            crea1_stregth *2
        elif crea2 > crea1
            tempcrea2_strength = crea2_strength *2
        else
            tempcrea1_strength = crea1_strength
            tempcrea2_strength = crea2_strength


creature1_life = creature1_life - creature2_strength
creature2_life = creature2_life - creature1_strength

    if creature1_life = 0 :
        print ("Creature 1 died \nCréature 2 won the fight")
    elif creature2_life = 0 :
        print ("Creature 2 died \nCréature 1 won the fight")
    elif creature1_life > creature2_life :
        print ("Créature 1 won the fight ")
    elif creature2_life > creature1_life :
        print ("Créature 2 won the fight ")
    else
        print ("Draw")

Returns : ()

-------------------

Spec function combat
 def combat (creaturename1, creaturename2)

 Parameters
   creaturename1, creaturename2 : creatures name (Str)

 Raises
   Value error : - creature didnt exists
                 - missing a creature

 Returns
   Result : -
            -
            -
"""
