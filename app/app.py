import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

if __name__ == "__main__":
    while True:
        word = input("Enter a word: ")
        print("\n")
        word = word.lower()
        if word in data:
            output = (data[word])
            print(word)
            for definition in output:
                print("-", definition, "\n")
        else:
            similar_words = get_close_matches(word, data.keys(), n=4, cutoff=0.75)
            if len(similar_words) > 0:
                print("That word doesn't exist, perhaps you meant one of the following?: ", end="")
                for word in similar_words:
                    print(f"'{word}'", end=" ")
            else: 
                print("No words like the one you typed exist in the database, check your spelling or try a different word.")
        print("\n" + "Hit 'Ctrl+C' to exit.")