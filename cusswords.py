from better_profanity import profanity

text = input("Enter your sentence to text: ")
censored = profanity.censor(text)
print(censored)
