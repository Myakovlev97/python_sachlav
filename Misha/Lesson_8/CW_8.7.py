a = input("Enter a sentence: ")
if a[-1] == "?":
    type_of_sentence = "Question"
else:
    type_of_sentence = "Regular"
print(type_of_sentence)