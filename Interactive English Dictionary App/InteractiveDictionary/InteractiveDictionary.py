import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
#keyword = "zzzzzzzzzz"

if __name__ == "__main__":
    keyword = "zzzzzzzzzz"
    while(keyword not in data):
        keyword = input("\nEnter a word: ")
        if (keyword in data):
            print(data[keyword])
            break
        elif (keyword.lower() in data):
            print(data[keyword])
            break
        elif (len(get_close_matches(keyword, data.keys(), n=4, cutoff=0.75)) > 0):
            print("That word doesn't exist in the database. Perhaps you meant: ", get_close_matches(keyword, data.keys(), n=4, cutoff=0.75))
        else:
            print("No words like the one you typed exist in the database, check your spelling or try a different word.")

