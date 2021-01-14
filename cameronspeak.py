import random

vocab = ["dick","dick","dick","dick","mc","suck","wholesome","white","deez","nutz","Joe","chungus","small","big"]
phrase = ""
for word in range(random.randint(1,20)):
    phrase+=random.choice(vocab)
    phrase+=" "
print(phrase)
