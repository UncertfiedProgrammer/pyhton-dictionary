meme_dict = {
            "CRINGE": "Something that's weird and embaraassing",
            "LOL": "it stands for 'Laughing out loud' ",
            "LMAO": "stands for 'laughing my ass off' "
            }

word = input("Type an internet slang you don't understand: ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("this word doesn't exist in the dictionary")


print("fish")
