# The open function allows me to open a file. So I can open a text file, a JSON file, really any type of file I want.
# And the mode here, which is what I've placed second, is the way in which we're kind of reading it in. 
# So I'm going to read it in, in read mode, which is our mode.
with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)