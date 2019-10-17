
player = { 
    "name": "random name", 
}    

def helloWorld():
	
	pcmd = raw_input("Your options: [ slack, github, canvas ]")

	if (pcmd == "slack"):
		print " "
		print "Could have been. But nope, not here."
		print " "
		helloWorld()

	elif (pcmd == "github"):
		print " "
		print "Yep. You better learn how to use that."
	
	elif (pcmd == "canvas"):
		print " "
		print "Nah. I think canvas is not that popular. Let's try again."
		print " "
		helloWorld()

	else:
		print " "
		print "Dude. Look at your options and remember I don't like spelling mistakes."
		print " "
		helloWorld()

def researchMethods():

	pcmd = raw_input("Your options: [ slack, google drive, canvas, our facebook group, rafa ]")

	if (pcmd == "slack"):
		print " "
		print "Nope. You have some info there but still not all you need."
		print " "
		researchMethods()

	elif (pcmd == "google drive"):
		print " "
		print "YAY. It seems that all you need is in google drive."
	
	elif (pcmd == "canvas"):
		print " "
		print "Nah. I think canvas is not that popular. Let's try again."
		print " "
		researchMethods()

	elif (pcmd == "our facebook group"):
		print " "
		print "Jeez. We don't have a facebook group for research methods. You are really lost!"
		print " "
		researchMethods()

	elif (pcmd == "rafa"):
		print " "
		print "good job - looks like you're so up to date with things!"
		print "Rafa can definitely help you out with details."

	else:
		print " "
		print "Dude. Look at your options and remember that I am case sensitive."
		print " "
		researchMethods()

def serviceDesign():

	pcmd = raw_input("Your options: [ slack, george michael, canvas ] ")

	if (pcmd == "slack"):
		print " "
		print "Duh, not all your homework is on slack!!! Try again."
		print " "
		serviceDesign()

	elif (pcmd == "george michael"):
		print " "
		print "Lol. He's a cat. Do you understand meow?"
		print " "
		print '                                     ,'
		print '              ,-.       _,---._ __  / \ '
		print '             /  )    .-\'       `./ /   \ '
		print '            (  (   ,\'            `/    /|'
		print '             \  `-"             \'\   / |'
		print '              `.              ,  \ \ /  |'
		print '               /`.          ,\'-`----Y   |'
		print '              (            ;        |   \''
		print '              |  ,-.    ,-\'         |  /'
		print '              |  | (   |        hjw | /'
		print '              )  |  \  `.___________|/'
		print '              `--\'   `--\''
		print " "
		print " "
		serviceDesign()

	elif (pcmd == "canvas"):
		print " "
		print "WOAH, YOU FOUND IT!"
		print " "
		print "You're getting so close to finding all your assignments."
		print "Keep at it!"

	else:
		print " "
		print "Dude. Look at your options and remember that I am case sensitive."
		print " "
		serviceDesign()

def phyCom():

	pcmd = raw_input("Your options: [ canvas, vfl lab ] ")

	if (pcmd == "canvas"):
		print " "
		print "Damn, you found it - you have really good instincts!"

	elif (pcmd == "vfl lab"):	
		print " "
		print "SURPRISE! You found some free wires and cool things BUT not your homework."
		print "You'll have to start looking again."
		print " "
		phyCom()

	else:
		print " "
		print "Dude. There are only 2 options, choose from them."
		print " "
		phyCom()

def productService():

	pcmd = raw_input("Your options: [ canvas, slack , google drive , poonam ] ")

	if (pcmd == "canvas"):
		print " "
		print "Ouch! It seems like you are as lost as I am."
		print " "
		productService()

	elif (pcmd == "slack"):
		print " "
		print "Super!! Looks like your homework is here!"

	elif (pcmd == "google drive"):
		print " "
		print "Ouch! It seems like you are as lost as I am."
		print " "
		productService()


	elif (pcmd == "poonam"):
		print " "
		print "You're absoltuely right!!"
		print "It seems like Poonam will have all the details you need!"

	else:
		print " "
		print "Dude. You have clear options to choose!"
		print " "
		productService()

def stressSituation():
	
	print " "
	print "Are you stressed with all your homework?"
	
	pcmd = raw_input("Your options: [ yes, no ] ")

	if (pcmd == "yes"):
		print " "
		print "I feel you. You're not alone!!"

	elif (pcmd == "no"):
		print " "
		print "Sure. Keep lying to yourself!"

	else:
		print "Dude, type it right!!"
		stressSituation()

def introduction():
	
	print " "
	print " "
	print "--------------------------------------------------------------------- "
	print ' _    _ _                   _                              '
	print '| |  | | |                 ( )                             '
	print '| |  | | |__   ___ _ __ ___|/ ___                          '
	print '| |/\| | \'_ \ / _ \ \'__/ _ \ / __|                         '
	print '\  /\  / | | |  __/ | |  __/ \__ \                         '
	print ' \/  \/|_| |_|\___|_|  \___| |___/                         '
	print '                                                           '
	print '                                                           '
	print '                                                           '
	print '                                                           '
	print ' _   _  ___  _   _ _ __                                    '
	print '| | | |/ _ \| | | | \'__|                                   '
	print '| |_| | (_) | |_| | |                                      '
	print ' \__, |\___/ \__,_|_|                                      '
	print '  __/ |                                                    '
	print ' |___/                                                     '
	print ' _                                             _      ___  '
	print '| |                                           | |    |__ \ '
	print '| |__   ___  _ __ ___   _____      _____  _ __| | __    ) |'
	print '| \'_ \ / _ \| \'_ ` _ \ / _ \ \ /\ / / _ \| \'__| |/ /   / / '
	print '| | | | (_) | | | | | |  __/\ V  V / (_) | |  |   <   |_|  '
	print '|_| |_|\___/|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\  (_)  '
                                                           
                                                           
	print " "
	print "--------------------------------------------------------------------- "
	print " "
	print "Hi there! It seems like you are part of the SVA MFA IxD class of 2021."
	
	player["name"] = raw_input("what's your name? ")
	
	print " "
	print player["name"] + ", it's almost weekend."
	print "It means that instead of having a bunch of fun,"
	print "you'll start finding your assignments for next week! :/ "
	print " "
	
	raw_input("[ press enter ]")

def main():
	
	introduction()
	
	stressSituation()
	
	print " "
	
	raw_input("[ press enter ]")

	print " "
	print "On monday you'll have the Product/Service class."
	print "You have a lot of things to do for your sponsored project."
	print "Where would you find information about your assignments for this class?"
	
	productService()

	print " "

	raw_input("[ press enter ]")

	print " "
	print "Let's start looking at what is due on tuesday: Physical Computing."
	print "It seems like you need to do a bunch of tutorials and make some cool toy."
	print "Where would you go to find your next Physical Computing assignment?"
	
	phyCom()

	print " "

	raw_input("[ press enter ]")

	print " "
	print "Let's look at the next assignment due on Tuesday: Service Design."
	print "You need to get back to your journal again! But where's the assignment?"
		
	serviceDesign()

	print " "

	raw_input("[ press enter ]")

	print " "
	print "You have to prepare for your Research Design class interview."
	print "Where are the specifications about your assignment?"

	researchMethods()

	print " "

	raw_input("[ press enter ]")

	print " "
	print "Now you have to prepare for the Hello World class"
	print "Where are is your homework instructions?"

	helloWorld()

	print " "

	raw_input("[ press enter ]")

	print " "
	print "--------------------------------------------------------------------- "
	print " "
	print player["name"] + ", YOU DID IT! KNOW YOU CAN ENJOY YOUR NEXT 96 HOURS DOING ALL YOUR HOMEWORK. GOOD LUCK"
	print " "
	print '                         Z             '
	print '                       Z                   '
	print '        .,.,        z           '
	print '      (((((())    z             '
	print '     (((\'_  _`) \'               '
	print '     ((G   \ |)                 '
	print '    (((`   " ,                  '
	print '     .((\.:~:          .--------------.    '
	print '     __.| `"\'.__      | \              |     '
	print '  .~~   `---\'   ~.    |  .             :     '
	print ' /                `   |   `-.__________)     '
	print '|             ~       |  :             :   '
	print '|                     |  :  |              '
	print '|    _                |     |   [ ##   :   '
	print ' \    ~~-.            |  ,   oo_______.\'   '
	print '  `_   ( \) _____/~~~~ `--___              '
	print '  | ~`-)  ) `-.   `---   ( - a:f -         '
	print '  |   \'///`  | `-.                         '
	print '  |     | |  |    `-.                      '
	print '  |     | |  |       `-.                   '
	print '  |     | |\ |                             '
	print '  |     | | \|                             '
	print '   `-.  | |  |                             '
	print '      `-| \''


main() # this is the first thing that happens