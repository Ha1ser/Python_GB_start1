str1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
str1 = str1.upper().replace('.', " ").replace("'", " ").split()
print(set(str1))
print(len(set(str1)))