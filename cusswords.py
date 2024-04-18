from better_profanity import profanity
from text import readline

text = input("Enter your sentence to text: ")
censored = profanity.censor(text)
print(censored)
#better done, we create a function that takes a filename as parameter and indicates the lines in a file that contain cuss words
def check_cusswords(fileneme):
    with open(fileneme, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if profanity.contains_profanity(line):
                # print(f"Line {line_number}: {line.strip()} contains profanity")
                print(f"Line {line_number} contains profanity")
            else:
                print(f"Line {line_number}: {line.strip()} does not contain profanity")
            
if __name__ == '__main__':
    check_cusswords("text.txt")
