size(500,500)
background('#004477')

hello = 'hello world'
whatsup = 'what\'s up!' # \ escape characters 
question = 'is your name really "world?"'
all = hello + ' ' + whatsup + ' ' + question #to put empty spaces
print(all)

print(len(all)) #tells you how many characters long 
print(all[0]) #tells you the character in that position
print(all[4:]) #tells you the character and all the characters after the position
print(all.upper()) #changes all the print in uppercase

fill('#ffffff') 
textSize(20)
text(all, 10,50) #textts need 3 arguements 
