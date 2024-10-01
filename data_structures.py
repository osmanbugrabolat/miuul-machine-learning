# --> DATA STRUCTURES <-- #


x = 1 #(int)
print(type(x))

y = 1.1 #(float)
print(type(y))

z = 2j + 1 #(complex)
print(type(z))

k = "hello" #(string)
print(type(k))

l = True #(boolean)
print(type(l))

m = ["a" , "b" , "c"] #(list)
print(type(m))

n = {"name":"bugra", "age": 25, "degree": "university"} #(dictionary)
print(type(n))

o = ("a", "b", "c") #(tuple)
print(type(o))

p = {"a", "b", "c"} #(set)
print(type(p))



#String Slices

exp = "Hello My AI World!"
print(exp[3])
print(exp[0:4])


print("My" in exp)


#String Methods

dir(str)

dir(int)

name = "Osman Buğra BOLAT"

uzunluk = len(name)

print(uzunluk)

print(len("abcdefghıjklmnoprst"))

print(name.upper())
print(name.lower())


name = name.replace("BOLAT","Bolat")
print(name)


print(name.split()) # default olarak boşluktan böler


print("osman".capitalize()) # ilk harf büyük


#LIST

#Değiştirelebilir, indexlidir, kapsayıcıdır

notes = [1, 2, 3, "f", "b", [4,5,6,7,"FB"], True, False]

print(notes[5])

notes[0] = 99

print(notes)


#List Methods
print(dir(notes))

liste = [1,2,3,4,5]
liste.append(99)
print(liste)

liste.pop(5)  #indexe göre siler
print(liste)

liste.insert(0,0) # indexe göre ekler
print(liste)


#DICTONARY

#Değiştirilebilir, kapsayıcıdır, sırasız (key-value)

dict = {"01": "Adana", "60": "Tokat", "06" :"Ankara" }

print(dict["01"])

dict["01"] = "adana"

print(dict.values())


#TUPLES

#DeğiştirileMEZ, sıralıdır, kapsayıcıdır

tup = (1,2,3,"a", True, (4,5,6))


#SETS

#Değiştirelebilir ,sırasız , eşsiz(her obje tek), kapsayıcıdır

set1 = set([1,2,3])
set2 = set([1,3,5])

print(set1.difference(set2))

print(set1.symmetric_difference(set2))


print(set1.intersection(set2))