string=input("enter a string:")
char=0
word=1
space=0
for i in string:
	char=char+1
	if(i==" "):
		word=word+1
		space=space+1
print("No of letters in this string:")
print(char-space)
print("No of words in this string is:")
print(word)
		

