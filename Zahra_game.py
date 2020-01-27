# Personal mini-project
# By Zahra Abbasian Korbekandi (Student # 1032221)

# This project is designed to be a mini-adventure game
# It is a recreation based on a small part of the game 'Amnesia: The dark decent'(2010), developed by Frictional Games


# The texts inside the 'books' in the 'Library' are taken from the following websites:
#https://www.buzzfeed.com/meganb69/13-great-dark-mysterious-poems-d2pe
#https://www.spiegel.de/international/zeitgeist/purification-through-pain-a-fresh-look-at-torture-in-the-middle-ages-a-725629.html
#https://www.iep.utm.edu/machiave/

#The texts in the 'letters' are taken from the website:
#https://amnesia.fandom.com/wiki/Notes_(The_Dark_Descent)


 

#Here are the functions belonging to each room


#Study room
def study_room():
    print("You are suddenly awake and find yourself lying on the ground in a room.")
    time.sleep(2)
    print("There's a desk and some books and papers, some pictures on the walls")
    time.sleep(2)
    print("It looks like a regular study room, but inside a castle.")
    time.sleep(2)
    print("You try to remember how you ended up here...")
    time.sleep(2)
    print("But you can't remember anything.")
    time.sleep(2)
    print("While thinking hard, you find a piece of paper on the desk.")
    time.sleep(2)
    print("You grab the paper which seems to be a letter and read it.")
    time.sleep(5)          #This funsction creates a delay for (5) seconds after print
    print()
    print()
    print()
    print("19th of August, 1839")
    print("I wish I could ask you how much you remember. I don't know if there will be anything left"\
          "after I consume this drink. Don't be afraid Daniel. I can't tell you why, but know this. I choose "\
          "to forget. Try to find comfort and strength in that fact. There is a purpose. You are my final effort"\
          "to put things right. God willing, the name Alexander of Brennenburg still invokes bitter anger in you. "\
          "If not, this will sound horrible. Go to the Inner Sanctum, find Alexander and kill him. His body is old "\
          "and weak, and yours, young and strong. He will be no match for you. One last thing, a shadow is following "\
          "you. It's a living nightmare, breaking down reality. I have tried everything and there is no way to fight back."\
          "You need to escape it as long as you can. Redeem us both Daniel. Descend into the darkness where Alexander waits"\
          "and murder him.")
    print("Your former self,")
    print("Daniel")

    time.sleep(5)
    print()
    print()
    print()
    print("You put the letter down and wonder about it for a bit. Then, you "\
          " decide to get out of this room for a start.")
    time.sleep(3)
    return;



#Library 
def library():
    print("You open the library door and peak inside.")
    time.sleep(3)
    print("As expected, the room is full of shelves and books.")
    time.sleep(3)
    print("You wander around the shelves. There doesn't seem to be anything interesting.")
    time.sleep(3)
    print("However, there's a table in the middle of the room with a few books on it.")
    time.sleep(3)
    print("The books are about 'Literature'(l), 'History'(h), 'Chemistry'(c) and 'Philosophy'(p).")
    time.sleep(5)
    book_read = ""                         #first difeining the variable by an empty string
    book_list = ["c","h","l","p",""]       #The list of values that can be chosen to read the books
    while (book_read in book_list):        #as long as the player is interested in reading, empty string for when not entering anything
        book_read = input("Which book do you want to skim through?(l/h/c/p or none?): ").lower().strip()  #to make lower case and strip for only the characters
        
        if (book_read == "c"):             #When player chooses to read the chemistry book
            time.sleep(3)
            print()
            print()
            print()
            print("... To make a strong acid, four different chemicals should be provided."\
                  "First, have a pot with only Aqua Regia, which is the base chemical for this"\
                  " purpose. Then, add the same amount of Cuprite to it. The third chemical is Calamine"\
                  " that should be added to the mixture. Finally, combine the Opriment very slowly"\
                  " to the mixture. The acid will get ready after a few minutes....")
            time.sleep(5)
            print()
            print()
            print()
        elif (book_read == "h"):          #when player chooses the history book
            time.sleep(3)
            print()
            print()
            print()
            print("...Nevertheless, in his newly published book Schild recommends a reappraisal of"\
                  " the administration of justice in the supposedly Dark Ages. 'All brutality aside,"\
                  " the criminal law of the day was also concerned with the salvation of the convicted criminal.")
            print("But the executioners of the Middle Ages were not driven by such sadistic impulses."\
                  " Instead, for the general good, they sought to pacify the 'offended God'.")
            print("'The Christian authorities also subjected wrongdoers to gruesome punishments so that"\
                  " they could attain eternal life,' says Schild. The prevailing view at the time was only"\
                  " when the refractory body had been softened up would the soul be liberated and ready for God....")
            time.sleep(5)
            print()
            print()
            print()
        elif (book_read == "l"):          #when player chooses the literature book
            time.sleep(3)
            print()
            print()
            print()
            print("...'Better to reign in Hell, then serve in Heav'n...'")
            print("This work of genius manages to combine sublime language and imagery, a wealth of classical"\
                  " mythology, a gripping plot and characters that are both well-developed and "\
                  " memorable all into one, brilliant piece.")
            print("It’s the story of man’s expulsion from the Garden of Eden, but really, the star"\
                  " of the piece is Satan. Far from being simple, mindless evil, Satan is an immensely complex"\
                  " character with real motivation for his actions.")
            print("'Paradise Lost' is certainly not the easiest read in the world if you’re not fully versed in Greek mythology....")
            time.sleep(5)
            print()
            print()
            print()
        elif (book_read == "p"):           #when player chooses the philosophy book
            time.sleep(3)
            print()
            print()
            print()
            print("...Because cruelty and deception play such important roles in his ethics, it is not unusual for related"\
                  " issues—such as murder and betrayal—to rear their heads with regularity. If Machiavelli possessed a sense"\
                  " of moral squeamishness, it is not something that one easily detects in his works. However, it should be noted"\
                  " that recent work has suggested that many, if not all, of Machiavelli’s shocking moral claims are ironic. "\
                  " If this hypothesis is true, then his moral position would be much more complicated than it appears to be. "\
                  " Does Machiavelli ultimately ask us to rise above considerations of utility? Does he, of all people, ask us"\
                  " to rise above what we have come to see as Machiavellianism?...")
            time.sleep(5)
            print()
            print()
            print()
        else:                           #when the players types in anything else the loop for asking which book to read ends
            print ("Of course you're not in the mood for reading!")
            time.sleep(3)
    print("You are done with this room for now, you open the door to go to the hall.")
    time.sleep(3)
    return                          #the library function does not need to return any variables




#Archives 

def archives():
    global got_key                  #global is the opposite of local, which makes the function to use the global value of the variable
    global is_having_key            #This is a way to pass the variables in between the functions
    global been_here_before
    
    print("Again, another room with a desk, some books and papers.")
    time.sleep(3)
    if (been_here_before == False):
        
        if(got_key == True):             #when player has been here and has grabbed the key 
            print("There's not much to do here.")
            time.sleep(3)
            print("You already have taken the key from the drawer.")
            time.sleep(3)

        elif (got_key == False):         #when player did not grab the key or visits for the first time
            print("As usual, you would think there is probably something important on the desk.")
            time.sleep(3)
            print("So you go toward it. You were right! there's a paper.")
            time.sleep(3)
            print("It seems to be another letter for you. So you just read it.")
            time.sleep(3)
            print("But not out loud!...")
            time.sleep(5)
            
            print()
            print()
            print()
            print("Daniel, you have gone too far. I have to stop you. I can't let you proceed any further."\
              "I'm sorry, my friend.")
            print()
            print()
            print()
            time.sleep(5)
            print("You wonder, What that could mean...")
            time.sleep(3)
            print("You look at the desk again. It has a few drawers.")
            time.sleep(3)
            search_desk = ()
            search_desk = input("Do you want to look inside the drawers? (y/n): ")
            if (search_desk == "y"):
        
                print("There are just more and more papers inside them.")
                time.sleep(3)
                print("Wait! You find a key in the last drawer.")
                time.sleep(3)
        
                is_having_key = input("Do you want to grab the key? (y/n): ").lower().strip()
                if (is_having_key == "y"):    #when the player grabs the key the variable turns to True 
                    got_key = True
                else:
                    got_key = False           #player does not grab the key
        been_here_before = True
        
    elif (been_here_before == True):
        if(got_key == True):             #when player has been here and has grabbed the key 
            print("There's not much to do here.")
            time.sleep(3)
            print("You already have taken the key from the drawer.")
            time.sleep(3)

        elif (got_key == False):         #when player did not grab the key or visits for the first time
            
            print("You go toward the desk in the middle of the room.")
            time.sleep(3)
            search_desk = ()
            search_desk = input("Do you want to look inside the drawers? (y/n): ")
            if (search_desk == "y"):
        
                print("There are just more and more papers inside them.")
                time.sleep(3)
                print("Wait! You find a key in the last drawer.")
                time.sleep(3)
        
                is_having_key = input("Do you want to grab the key? (y/n): ").lower().strip()
                if (is_having_key == "y"):    #when the player grabs the key the variable turns to True 
                    got_key = True
                else:
                    got_key = False           #player does not grab the key

        
    
    print("You have finished with this room and want to go ahead and exit to the hall.")
    time.sleep(3)
    
    return got_key   #This function should return the value of the variable 'got_key' to use later by other functions







#Exit door in the hall
#visiting for the first time
def exit_door_1():
    global door_covered
    
    #print("You walk the dark path down the hall and find a big wooden door, which probably leads outside.")
    #time.sleep(3)
    
    open_exit_door = input("Do you want to open the door? (y/n) ").lower().strip()   #asking if player wants to open the door
    
    if (open_exit_door == "y"):          #when the player tries to open the door
        time.sleep(3)
        print("You touch the handle but as soon as you try to turn it...")
        time.sleep(3)
        print("The door gets covered by a red organic matter all over it.")
        time.sleep(3)
        print("It somehow seems like a live fleshy thing blocking your way to go ahead.")
        time.sleep(3)
        print("The handle is completely out of reach.")
        time.sleep(3)
        print("You touch that red matter... Ouch! It hurts!")
        time.sleep(3)
        print("you have to find a way to desolve it.")
        time.sleep(3)
        
        door_covered = True        #the variable defining if the player has tried to open the door

    else:                    #the player does not want to open the door
        print("So you want to stay here for longer?!")
        time.sleep(3)
        door_covered = False
        
    print("You look around and see two other rooms on your sides.")
    time.sleep(3)
    print("The signs on them read 'Laboratory' and 'Wine Cellar'")
        
    time.sleep(3)
   
    
    return door_covered   #This function should return the value of this variable to use later in other functions
    







#Laboratory


def lab():
    global is_having_chemicals
    global acid_list
    
    print("There are a few tables around with some pots and containers on them.")
    time.sleep(3)
    print("The containers look empty and clean. There are also a few small equipments.")
    time.sleep(3)
    
    if (is_having_chemicals == True):        #checking if the player has the chemicals
        if (acid_list == ["","","",""]):     #when acid_list is empty means player does not have the acid yet
            print("You've got all the six chemicals: Opriment, Aqua Fortis, Cuprite, Aqua Regia, Agrippa, Calamine.")
            time.sleep(3)
            print("Now, by using the pots and equipments here you can combine them in their specific order so you will make an acid.")
            time.sleep(5)
        
            #now, asking player to make the acid by choosing the chemicals in an order
            acid_list[0] = input ("Which chemical do you use first?: ").lower().strip()  #replaces the first item in the list above
            acid_list[1] = input("What is the second ingredient?: ").lower().strip()     #replaces the second item
            acid_list[2] = input("What do you add then?: ").lower().strip()              #replaces the third item
            acid_list[3] = input("What is the last chemical to be added?: ").lower().strip()   #replaces the fourth item

            print("Great! You now have an acid.")
            time.sleep(3)
            print("But it will prove useful later.")
            time.sleep(3)

        elif (acid_list != ["","","",""]):           #when acid_list is not empty means that player has made an acid
            print("You have already made an acid.")
       
        
            
    elif(is_having_chemicals == False):   #when the player does not have the chemicals yet
  
        print("It doesn't seem you can do much here.")
        time.sleep(3)
 
        acid_list = ["","","",""]        #maintaining the acid_list as empty

    

    print("You can get out of here and return to the hall.")
    time.sleep(3)

    return acid_list  #this function should return the value of the variable 'acid_list' to use later



#wine_cellar

def wine_cellar():
    global is_having_chemicals
    global cellar_door_opened
    global got_key
    
    if (cellar_door_opened == True):    #when player has already opened the cellar door with the key
        
        print("There's a staircase in front of you leading downstairs.")
        time.sleep(3)
        print("you go down and reach a quite large space with lots of giant wine barrels around.")
        time.sleep(3)
        print("You look around and see two rooms in front of you. One of them has a red door and the other green.")
        time.sleep(3)
        
        if (is_having_chemicals == False):          #when player does not have the chemicals yet
            is_having_chemicals = explore_cellar()   #then player will be led into the rooms, hence get the chemicals
            if (is_having_chemicals == True):        #when player grabs the chemicals
                game_end = monster()                 #in this case the monster attacks
            elif (is_having_chemicals == False):     #when player does not grab the chemicals
                print("You are then finished with the cellar. You go up the stairs and enter the hall.")   #in this case, player just goes out the cellar
                time.sleep(3)
        elif (is_having_chemicals == True):          #when player has already grabbed the chemicals from before
            print("There's no need to explore the rooms.")
            print("You have already collected the chemicals.")
        
            
    elif (cellar_door_opened == False):   #when player has not opened the cellar door yet
        if (got_key == True):             #checking if player has the key
            print("You try to open the door but it's apparently locked.")
            time.sleep(3)
            print("You just try the key you collected from Archives on it.")
            time.sleep(3)
            print("The Door opens!")
            time.sleep(3)
            print("There's a staircase in front of you leading downstairs.")
            time.sleep(3)
            print("you go down and reach a quite large space with lots of giant wine barrels around.")
            time.sleep(3)
            print("You look around and see two rooms in front of you. One of them has a red door and the other green.")
            time.sleep(3)
            cellar_door_opened = True       #The value of this variable must change now

            is_having_chemicals = explore_cellar()
        

            if (is_having_chemicals == True):     #when player grabs the chemicals the monster attacks
                game_end = monster()
            elif (is_having_chemicals == False):   #or player just goes out the cellar
                print("You are then finished with the cellar. You go up the stairs and enter the hall.") 
                time.sleep(3)
 

        elif (got_key == False):          #when player does not have the key
            print("You try to open the door but it's apparently locked.")
            time.sleep(3)
            print("You have to find a way to open the cellar door.")
            time.sleep(3)
            is_having_chemicals = False     #player did not grab the chemicals
            cellar_door_opened = False      #player did not open the cellar door

    

    return is_having_chemicals   #this function also should return the value of this variable to be used later





    


# exploring inside the wine cellar
def explore_cellar():
    global is_having_chemicals
    
    choice_in = ()
    choice_list = ["r","g"]   #The list of values for choosing a path

    while (choice_in not in choice_list):   #this loop keeps prompting player to choose a path

        choice_in = input("Which room do you want to go to? Red room(r) or Green room(g): ").lower().strip()   
        if (choice_in == "r"):             #player chooses the red room
            print("There are more barrels, some wine bottles and a big cabinet with closed doors.")
            time.sleep(3)

            print("Apparently, there is nothing interesting here.")
            time.sleep(3)
                
            print("You get out of the current room.")
            time.sleep(3)
                
        
            choice_inside = input("Would you like to explore the green room?(y/n): ").lower().strip()  #askes to check the other room as well
            if (choice_inside == "y"):           #player agrees to check the green room
                print("There are a few barrels, a lot of wine bottles, and a small table with a wooden box under it.")
                time.sleep(3)
                if (is_having_chemicals == False):    #checkes if player has not collected chemicals before
                    print("You open the box and find six liquids in glass bottles, each having a label with different names.")
                    print("They seem to be some chemicals.")
                    time.sleep(3)
        
                    get_chemicals = input("Would you like to grab them?(y/n): ")   #prompts player to grab the chemicals
                    if (get_chemicals == "y"):      #as above
                        is_having_chemicals = True   #as above
                    else:
                        is_having_chemicals = False
                            
                elif (is_having_chemicals == True):              #when player has already collected the chemicals
                    print("You have already collected ....")
                    time.sleep(3)
                    print("So, you get out of the current room.")
                    time.sleep(3)
                        
            else:                            #when player does not want to check the green room
                print("You are finished with here. Unless you want to drink some wine!")
                    
                    
            
        elif (choice_in == "g"):                #when player chooses to visit the green room first
            print("There are a few barrels, a lot of wine bottles, and a small table with a wooden box under it.")
            time.sleep(3)
            if (is_having_chemicals == False):   #checks if player has not collected the chemicals
                print("You open the box and find six liquids in glass bottles, each having a label with different names.")
                print("They seem to be some chemicals.")
                time.sleep(3)
        
                get_chemicals = input("Would you like to grab them?(y/n): ").lower().strip()
                if (get_chemicals == "y"):       #as above
                    is_having_chemicals = True   #as above
                else:                            #as above
                    is_having_chemicals = False
                    
                print("You get out of the current room.")
                time.sleep(3)
                    
            elif (is_having_chemicals == True):   #when player has collected the chemicals
                print("You have already collected the chemicals")
                time.sleep(3)
                print("So, you get out of the current room.")
                time.sleep(3)
                    
            choice_inside = input("Would you like to explore the red room?(y/n): ").lower().strip()   #asks if player wants to check the other room
            if (choice_inside == "y"):            #when player agrees to go in the red room
                print("There are more barrels, some wine bottles and a big cabinet with closed doors.")
                time.sleep(3)
                    
                print("You get out of the current room.")
                time.sleep(3)
            else:                                 #when player does not want to go in the red room
                print("You are finished with here. Unless, you want to drink some wine!")
                
    return is_having_chemicals




# when the monster appears, in wine cellar

def monster():
    print("You are ready to go up the stairs, but suddenly you hear a growl...")
    time.sleep(3)
    print("The cellar door bashes open and you get to see a horrific body of a MONSTER...")
    time.sleep(4)
    print("Quick! you have to run away. It is coming for you!")
    time.sleep(3)
    print("You don't have a weapon of any kind, and there's not much time to find one here.")
    time.sleep(3)
    print("So you must quickly hide somewhere...")
    time.sleep(3)
    print("But apparently, it'd be much better to hide in one of the rooms in the cellar.")
    time.sleep(3)
    choice_in = input("Which room would you like to run into? Red room(r) or Green room(g): ").lower().strip()  #another choice for entering which room
    
    if (choice_in == "r"):  #when player chooses the red room
        print("You enter the room and quickly close the door behind you.")
        time.sleep(3)
        print("The cabinet at the back grabs your attention.")
        time.sleep(3)
        print("You run toward it and open the doors. Luckily, there's enough room inside to hide.")
        time.sleep(3)
        print("The growl and the footsteps of the monster can be heard. It is so close...")
        time.sleep(3)
        print("You hide inside and close the cabinet doors... and just wait...")
        time.sleep(3)
        print("You can hear the monster breaking the door and coming inside.")
        time.sleep(3)
        print(".........")
        time.sleep(10)
        print("There's no sound of it anymore. You probably can come out safely.")
        time.sleep(3)
        print("You carefully go up the stairs to exit the wine cellar.")
        time.sleep(3)
        game_end = False
        
    elif (choice_in == "g"):   #when player chooses the green room
        print("You enter the room and quickly close the door behind you.")
        time.sleep(3)
        print("You think for a second if you want to hide behind the pile of barrels or just"\
            " in a dark corner.")
        time.sleep(3)
        print("It seems better to hide in the dark corner.")
        time.sleep(3)
        print("You can hear the monster breaking the door and coming inside.")
        time.sleep(3)
        print("It looks around for you. You can hear it slowly approaching you...")
        time.sleep(3)
        print("There are no sounds to be heard for a few seconds...")
        time.sleep(5)
        print("Suddenly there's a loud scraching growl just above your head...")
        time.sleep(3)
        print("you catiausly look up...")
        time.sleep(3)
        print("The monster has found you and its hideous arm up above, aiming to come down"\
            " heavily on your head.")
        time.sleep(5)
        print(".....")
        time.sleep(3)
        print("The last thing you remember is that you're lying on the ground, blood everywhere...")
        time.sleep(5)
        print("GAME OVER")
        time.sleep(15)
        game_end = True  #the game ends here
        quit()           #the game is finished and the program ends running
        
    return game_end
                





    


#Exit door in the hall
#visiting for the second time or more


def exit_door_2():
    global game_end
    global door_covered
    global acid_list

    if (door_covered == True):             #checks if player has opened the door and seen the red matter on door
        if (acid_list != ["","","",""]):   #checks if player has made an acid in the lab
            game_end = try_acid()           
        elif (acid_list == ["","","",""]):
            print("The door is still covered by that red matter.")
            print("You have to find a way to dissolve it.")
            

    elif (door_covered == False):          
        
        print("You touch the handle but as soon as you try to turn it, the door gets covered by a"\
              " red organic matter all over it.")
        time.sleep(3)
        print("It somehow seems like a live fleshy thing blocking your way to go ahead. The handle is"\
            " completely out of reach and you don't want to touch that red matter at all, becauce it hurts.")
        time.sleep(3)
        if (acid_list != ["","","",""]):
            game_end = try_acid()
        elif (acid_list == ["","","",""]):
            print("You have to find a way to dissolve it.")
            
        
    return game_end   #this function normally should return the value for when the game has ended or not






# opening exit door by the acid and monster attack
def try_acid():
    global acid_list
    global game_end
    
    
    print("Suddenly, you hear a loud growl from the other end of the hall.")
    time.sleep(3)
    print("The monster is back and apparently has spotted you already.")
    time.sleep(3)
    print("But you get the hold of yourself and pour the acid you have made on the red matter covering the door.")
    time.sleep(5)
    print(".....")
    time.sleep(5)
      
    
    if (acid_list == ["aqua regia","cuprite","calamine","opriment"]):  #checks if the made acid is the correct one
            
        print("The acid dissolves the red matter and the exit door is completely free.")
        time.sleep(3)
        print("You are now able to open the door. You get it quickly and close it behind you.")
        time.sleep(3)
        print("Well done! You completed this game successfully!")
        time.sleep(15)
        game_end = True   #game ends
        quit()            #the program ends running here
        
    else:                 #when player has the wrong acid
        print("You pour the acid on the door, but it doesn't seem to be working.")
        time.sleep(3)
        print("It might not even be an acid!")
        time.sleep(3)
        print("Oh, NO! The monster is getting closer and cloder.")
        time.sleep(3)
        print("The sound of the footsteps and growls stops for a moment.")
        time.sleep(3)
        print("You slowly and fearfully turn your head and look back.")
        time.sleep(3)
        print("There's the hideous disfigured beast right behind you! It hits your head hard.")
        time.sleep(3)
        print("The last thing you remember is you are lying on the ground,... blood everywhere...")
        time.sleep(15)
        game_end = True    #game ends 
        quit()              #program ends running here
    
   
        
    return game_end

        



        
#choosing a direction
#asks player where to go next each time they come back to the hall
def direction():
    choice = ()  #defining the choice by an empty string, also makes the variable empty each time this function is called
    global is_having_chemicals
    global got_key
    
    direction_list = ["li","la","ar","e","c"]   #There are 5 choices, each belonging to a room
    
    while (choice not in direction_list):      #the loop is to keep prompting player to choose a path
        choice = input("Which way do you want to explore next? Library(li), Archives(ar),"\
                       "Laboratory(la), Wine Cellar(c), Exit door(e): ").lower().strip()
        
        if (choice == "li"):                   #when library is chosen
            library()
        elif (choice == "ar"):                 #when archives is chosen
            got_key = archives()
        elif (choice == "la"):                 #when laboratory is chosen
            acid_list = lab()
        elif (choice == "c"):                  #when wine cellar is chosen
            is_having_chemicals = wine_cellar()     
        elif (choice == "e"):                  #when exit door is chosen
            game_end = exit_door_2()       
          
    return




#main body of the game


import time   #time should be imported to make delays

#defining the used variables in functions in the main body first
game_end = False   
is_having_key = ""
got_key = False
is_having_chemicals = False
cellar_door_opened = False
been_here_before = False
open_exit_door = ""
acid_list = ["","","",""]


time.sleep(5)
print("Welcome!")
time.sleep(3)
print()
print("This is a short game based on Amnesia: The Dark Decent")
time.sleep(3)
print()
print("By Zahra A. K.")
time.sleep(5)
print()
print()
print()
print()
print()

study_room()    #game starts here
print("you get out of the study room and you see two rooms on your right and left.")
time.sleep(3)
print("The signs on the doors read 'Library' and 'Archives'.")
time.sleep(3)


choice = ()   #as above
while (choice not in ["li","ar"]):   #loop to keep prompting player to choose a path, only two at this step
    choice = input("Which way do you want to go? Library(li) or Archives(ar): ").lower().strip()
    if (choice == "li"):             #when player chooses the library first
        library()
        #print("The other room 'Archives' is left to be explored.")   #it automatically goes forward to the archives
        #time.sleep(3)
        #got_key = archives()         #this variable changes in value by this function
        
        

    elif (choice == "ar"):           #when player chooses to visit archives first
        got_key = archives()         #as above
        
        #print("The other room 'Library' is left to be explored.")   #it automatically goes forward to the library
        #time.sleep(3)
        #library()
        
   
    else:                            #when player does not enter any of the correct paths
        print("You cannot not go anywhere!")


print("Something at the other end of the hall grabs your attention.")
time.sleep(3)
print("It's quite a big door, which probably leads outside here.")
time.sleep(3)

choice = ()
while (choice not in ["li","ar","e"]):
    choice = input("Where do you want to explore next? Archives(ar), Library(li), or the Exit door(e): ")
    if (choice == "e"):
        time.sleep(3)
        print("You make your way through the darkness and reach the other end of the hall.")
        time.sleep(3)
        door_covered = exit_door_1()         #this variable chenges in value by this function, if player touches the exit door or not
    elif (choice == "ar"):
        got_key = archives()
        print("You're back in the dark hall.")
        time.sleep(2)
        print("You make your way through the darkness and reach the other end.")
        time.sleep(3)
        door_covered = exit_door_1()  
    elif (choice == "li"):
        library()
        print("You're back in the dark hall.")
        time.sleep(2)
        print("You make your way through the darkness and reach the other end.")
        time.sleep(3)
        door_covered = exit_door_1() 
        



#choice = ()
#while (choice not in ["c","la"]):   #loop to keep prompting player to choose a path, only two at this step
    #choice = input("Which way would you like to go? cellar(c) or laboratory(la): ").lower().strip()
    #if (choice =="la"):             #when player chooses to visit the laboratory first
        #acid_list = lab()           #player does not have any chemicals or acid yet, so no variable needs to be returned
        #print("Now, the cellar is left to be explored.")   #it automatically goes forward to the wine cellar
        #time.sleep(5)
        
        #is_having_chemicals = wine_cellar()   #this variable changes its value by this function
        
        
    
    #elif (choice == "c"):            #when player chooses to visit the wine cellar first
        #is_having_chemicals = wine_cellar()   
        #if (game_end == False):
            #print("Now, the laboratory is left to be explored.")   #it automatically goes forward to the laboratory
            #time.sleep(5)
            #acid_list = lab()

        

while (game_end == False):           #loop to keep asking player where to go next as long as the game is not ended
    direction()
    



    
        
    

  
