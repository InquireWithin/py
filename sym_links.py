#!/usr/bin/python3
#Luke Bettner 3/3/22

#Script designed to create shortcuts with symlink, based around the home directory
#this script is assumed to be ran without sudo or root perms


#NOTE: this script can be ran from anywhere, it was added to the path via export
import os
import subprocess
link_count = 0; #needed for report
link_paths = set() #full filepaths of links original files, more useful than expected
link_names = list() #link_paths and names should just be a dictionary. i dont know why i didnt do that originally
#This will create a symlink that will be located in the User's ~/Desktop with an equal filename to the file being linked to. hard links not used.
#Desktop is the sole directory for these shortcuts.
def create_shortcut(filename):
	

	#the premise of this function of script is that it will find a specific file by name somewhere on the home directory and make a link to it
	#in the user's Desktop

	#a very rough way to find a target file and avoid duplicates
	#quicker way to specify the path to results.txt
	fl = home_dir + "/results.txt"

	os.chdir(home_dir)
	#if no results.txt, create one
	if not os.path.exists(home_dir+"/results.txt"):
		#results.txt will be a file that stores any and all iterations in this script. I prefer this over output parsing.
		os.system("touch results.txt")
	#find, within the user's home directory, only files that correspond with the user selected filename
	#results are output to results.txt in home_dir (~)
	os.system("find ~ -type f -iname " +filename + " > "+fl)
	line_count = 0
	#iterate over the results of the find command and let the user select if they wish to create a link
	#this option will also display full filepath from link_paths
	has_link = False #an indicator of link creation success
	with open(fl) as f:
	
		for l in f:
			line_count-=-1
			#go back to menu if the file couldnt be found. we know the file couldnt be found if theres nothing in the results.txt file.
			if (l == "" or l == None or l == False and line_count == 1):
				#file is empty
				print("No results found for selected filename.")
				menu()

			#FOR DUPLICATES: always choose the first option that isnt denied by the user AND not a duplicate in link_paths
			if filename in link_paths: 
				continue
			#confirmation for user
			print("Would you like to link to file: "+l + " \n(y/n)")
			select = input().lower()
			if select != "y" and select != "n":
				print("Invalid option, assuming no.")
				create_shortcut(filename)
			if select == 'n': #go to next file found (allows user to cycle through duplicates)
				continue
			if select == 'y': #create shortcut from this filepath the user has selected
				cwd = os.getcwd() #notify user of cwd
				print("Current working dir: "+ cwd)
				print("\n")
				link_paths.add(l)
				#ln -s source dest
				os.chdir(dest) #chdir to the place i want the link to be (~/Desktop)
				# -s indicates symbolic link, v for verbose, f for force (delete currently existing files with the same name)
				os.system("ln -svf " + l) #create symbolic link IN DEST (~/Desktop) to the found path.
				has_link = not has_link
				link_names.append(filename) #by doing this i can track the # of links by increasing the length
				break #orig break
			#this is here in case the script cant properly determine if a file is empty or not
			print("No file with the specific filename was found, all have been linked, or user rejected all non-suplicate results")
			print("\n")
	menu()

def remove_shortcut(filename):
	#this is what should be static given filename as a param:
	# the filename of the link and the actual file should ve the same
	#look for the link in dest, a variable name given to ~/Desktop, all links should be there
	#the name of the link, and therefore variable filename, should be recorded in link_paths set
	#if not, return to menu

	if os.path.exists(dest + "/"+filename):
		os.chdir(dest)
		cwd = os.getcwd()
		print("Current working dir: "+ cwd)
		print("\n")
		#remove with a confirmation the filename corresponding with the link
		os.system("rm -i "+filename)
		for i in range(len(link_names)):
			if link_names[i] == filename:
				del link_names[i]
		
	else: #the requested link to be removed cant be, likely due to it not existing.
		print("The selected filename was never linked, not currently linked, or does not exist.")
		print("Current working dir: "+ cwd)
		print("\n")
	
	menu()



def run_report():

	
	#find command has an option to display all current links

	os.chdir(dest) #go to where all the links are stored
	cwd = os.getcwd()
	print("Current working dir: "+ cwd)
	print("\n")
	print("Listing all symbolic links:\t Number of active links: "+ str(len(link_names)))
	#find all files in currently directory that are links and print them.
	os.system("find . -type l")
	print("\n")
	#back to menu options
	menu()

#responsible for handling the rather minimal user interaction and redirecting to one of 3 functions depending on user's answer
#this function is to be reverted to when another function completes or is unable to complete the request
#this is essentially the fallback function when crap hits the fan. Also the core function that handles the rest of the scripts functionality.
def menu():
	
	
	
	#user has one of three options: create shortcut in home dir, remove sortcut from home dir, run shortcut report
	print("Enter a number for the preferred shortcutting option: \na: Create shortcut in home directory\nb: Remove shortcut from home directory \nc: Run shortcut report \nquit: exit the script")

	selection = input().lower()
	
	#invalid input check

	if selection!= 'a' and selection != 'b' and selection != 'c' and selection != "quit":
		subprocess.Popen("clear",shell=True)
		print("user selection: "+ selection)
		print("Invalid input, insert a letter: a, b, or c")
		menu() #try again
	#enter file name to create a shortcut

	if selection == 'a':
		subprocess.Popen("clear",shell=True)
		print("Selected option " + selection + ": \nEnter name of file to create a shortcut to")
		filename = input()
		create_shortcut(filename)
	#call the function remove_shortcut to facilitate removing a link
	if selection == 'b':
		subprocess.Popen("clear",shell=True)
		print("Selected option " + selection + ": \nEnter name of file to remove the shortcut to")
		filename = input()
		remove_shortcut(filename)
	#show all current symbolic links
	if selection == 'c':
		subprocess.Popen("clear",shell=True)
		run_report()
	#return to main to allow user to exit the script
	if selection == "quit":
		return
		


#handles a couple variables and directs to the menu func, the real core function.
#main is reverted to when user quits the script.
def main():
	subprocess.Popen("clear",shell=True)
	global home_dir
	home_dir = os.path.expanduser('~')
	global dest
	dest = home_dir+ "/Desktop" 
	
	#go to function responsible for handling menu
	menu()




	



if __name__ == '__main__':
	main()

