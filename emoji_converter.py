message = input("Enter any message with :) (or) :( : ")
words = message.split(' ')
emoji ={
    ":)": "😊",
    ":(": "😞"
}
output =""
for word in words:
    output += emoji.get(word, word) + " "
print(output)