
marks = {
    "Ayush" : 100 , 
    "manisha" : 70 , 
    "nanu" : 76 , 
    98 : "ayush aryan"
}


print(marks.items())

print(marks.keys())

print(marks.values())


marks.update({'manisha' : 99 , 'rekha':67 })
print(marks)

print( marks.get('nanu'))

print( marks.get('panu'))