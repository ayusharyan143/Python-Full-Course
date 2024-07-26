word = "ayushformgoogle"
print( word[0: : 3])
print( word[0: 7 : 3])
print( word[5: 9 : 1])
print( word[5: 13 : 2])



print( "Length of word: " , len(word))

print("Ends with 'google' : " , word.endswith('google') ) 
print("Ends with 'googlee' : " , word.endswith('googlee') ) 


print("Start with 'ayush' : " , word.startswith('ayush') ) 
print("Start with 'Ayush' : " , word.startswith('Ayush') ) 

print("count number of 'a' : " , word.count('a') ) 
print("count number of 'o' : " , word.count('o') ) 
print("count number of 'g' : " , word.count('g') ) 




print("Staring word capitalize : " , word.capitalize() ) 
print("Start with 'Ayush' : " , word.startswith('Ayush') ) 


print("index of 'ayush' : " , word.find('ayush') ) 
print("index of 'g' : " , word.find('g') ) 