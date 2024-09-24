
action = ""
action_status= ""
current="0"
def get_input (prompt,resp1,resp2):
    while True:
        action=input(prompt).strip().lower()
        if action == resp1 or action== resp2 :
            return action
        if action != resp1 and action != resp2:
            print ("thats not a valid choice")





def one():
    

    while True  :
        print ('You wake up and find yourself stranded in the middle of an unknown forest.')
        action=get_input ("You seem to think that you might know the way back towards civilazation, but you arent completly sure.Do you want to head back towards the way you think is the exit, or do you want to continue deeper into the woods (type deeper or exit) : ",resp1="deeper", resp2="exit")
        if action == "deeper" :
            two()
                
        if action == "exit" :
            print ("You walk in the direction you think is the exit and stumble across a random shed")
            three()





def two():
    while True:
        print("after going deeper into the woods you find a worn down abandonded shack ")
        action= get_input("Your gut feeling is saying not to enter this shack but the risk taker inside you is saying to enter what do you do (type enter or continue ) : ","enter" , "continue")
        if action == "enter" :
            print ("while walking towards the shack you get a weird feeling just before you open the door")
            four()
        if action == "continue":
            print ("you decide to continue walking past the shack to your own relief.")
            five()
        



def three():
    while True:
        action=get_input ("do you want to investigate the shed or continue past (type investigate or continue) : ", "investigate","continue")
        if action == "continue":
            print (" you decided to continue past the shed ")
            six()
        if action == "investigate":
            print ("you walk up to the door and place your hand on the door knob to open it ")
            seven()
            





def four():
    while True:
        action=get_input ("do you want to open the door? (yes or no)","yes","no")
        if action == "yes":
            print ("you open the door and then *BOOM* everything goes black")
            nine()
        if action == "no":
            print ("you decide not to go in ")
            two()


def five():
    while True:
        action=get_input("nothing seems out of the normal but youre begining to feel tired do you continue or do you give up (continue or quit):","continue","quit")
        if action == "continue":
            print ("you decided to attempt to continue ")
            eight()
        if action == "quit":
            nine()

def six():
    while True:
        print("after continuing past the shed you stumnble into an unknown neighborhood but at least you are out of the woods")
        break
    





def seven():
    while True:
        print("you open the door and hear a click you look down and its a land mine")
        break



def eight():
    while True:
        print("you have made it back to town!!!!")
        break




def nine():
    while True:
        print("you have died")
        break







one()

