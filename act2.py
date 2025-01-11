class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word+' ('+self. meaning+' )'
flash = []
print("welcome to flashcard app")
while(True):
    word = input("enter name")    
    meaning = input("enter the meaning of the word:")
    flash.append(flashcard(word, meaning))
    option = int (input("enter 0, if u wana 2 add another flahscard or else enther 1: "))

    if (option):
            break
    
print("\nYour flashcards")
for i in flash:
    print(">" , i)