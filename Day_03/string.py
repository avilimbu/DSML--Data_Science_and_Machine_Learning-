text1 = "wow, a lovely day" #creating a string using double quote
text2 = 'hello' #creating a string using double quote

#creating a string using triple quote
poem = '''In every line of code,a lesson grows, 
Through every bug, a deeper wisdom flows.
Small steps each day become a journey bright,
Turning curiosity into skill and light.'''

#string concatintion
print(text1+", "+text2) #wow, a lovely day, hello

#string Repetation
print(text2 * 3) #hellohellohello (repeates the string 3 times)
 
#indexing
print(text2[1]) #e
print(text2[-1]) #o

#slicing [start: stop: step] || step = no of position to move each time default is 1.
print(text2[0:3]) #hel
print(text2[2:-1]) #ll
print(text2[::-1]) #olleh (reverse the string)

print(text1[2:16:2]) #w  oeyd

#leangth using len()
print(len(poem)) #166 

#string methods
word1="fantastic"
word2="REGULAR"
word = "i am a sutdent"

print(word1.upper()) #FANTASTIC
print(word2.lower()) #regular
print(word.title()) #I Am A Student

#strip() || It removes exta space/character before and after string
dummy = "   i think he is smart  "
print(dummy.strip())  #i think he is smart
sample = "&&&&&&&&brother&sister&&&&"
print(sample.strip("&")) #brother&sister

#replace
templete ="he is a very good student"
print(templete.replace("he","she")) #she is a very good student

#split() || it changes string to list
fruit = "mango, banana, apple"
print(type(fruit))     #<class 'str'>

print(fruit.split())  #['mango,', 'banana,', 'apple']
print(type(fruit.split())) #<class 'list'>

words="ranger/mango/avhi/python/dsml/github" #split() splits in each "/"
print(words.split("/")) #['ranger', 'mango', 'avhi', 'python', 'dsml', 'github']


#join() || It changes list into string
joint = ['ranger', 'mango', 'avhi', 'python', 'dsml', 'github']
print(", ".join(joint))  #ranger, mango, avhi, python, dsml, github

fav = ["P","y","t","h","o","n"]
print("".join(fav)) #Python


