Text = "Python's simplicity, readability, and vast libraries make it a popular language for data science, web development, and automation."
print("character=",len(Text))
words = Text.split()
for word in words:
    if len(word) > 7:
        print(word)
def Texte():
    Text = "Python's simplicity, readability, and vast libraries make it a popular language for data science, web development, and automation."
    return Text.upper()
print(Texte())




