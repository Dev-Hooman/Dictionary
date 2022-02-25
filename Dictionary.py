import json
from difflib import get_close_matches
#color libs
import colorama
from colorama import init, Fore, Back, Style

data = json.load(open("binData.json"))

def dictionary(word):

    if(word in data):
        return data[word]

    elif(word.upper() in data):
        return data[word.upper()]

    elif(word.title() in data):
        return data[word.title()]

    elif(len(get_close_matches(word, data.keys())[0]) > 0):   #this fn is used to check incorrect words possibilites
        yesNo = input( "Did you mean %s ?" %get_close_matches(word, data.keys() )[0] +"\nPress (Y) if yes, or (N) if no, (E) to exit = ")
        searchedWord = get_close_matches(word, data.keys())[0]

        if(yesNo == "Y" or yesNo == "y"):
            return data[searchedWord]

        elif(yesNo == "N" or yesNo == "n"):
            return "Sorry unable to find Searched word, Re-Check it: "

        elif(yesNo == "E" or yesNo == "e"):
            return "***Good Bye***"
            exit()

    else:
        return "This word does not exist in Dictionary "

def datainput():
    w = input("ENTER A WORD TO SEARCH MEANING: ")
    wordstored = w.lower()
    output = dictionary(wordstored)

    if(type(output) == list):
        for item in output:
            print("#> ",item,)
    else:
        print(output)



def main():

    init(autoreset=True)

    print(Style.BRIGHT+Back.YELLOW+Fore.WHITE + 'Welcome to dictionary V_1.0, Developed by Dev-Hooman \n')
    print(Fore.RED + "NOTE: This product is still in developement... Enjoy\n")
    while(True):
        datainput()
        input("\nPress Enter to continue... :) \n")

if __name__ == '__main__':
    main()
