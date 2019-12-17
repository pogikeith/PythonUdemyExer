str='python'

print(len(str))

str='PYTHON'

print(str.lower())

str='python'

print(str.upper())

str='I like Python'

print(str.replace("like", "love"))

str='I like Python like'

print(str.replace("like", "love", 1))

str='Python, Java, PHP'

a,b,c=str.split(",")

print(a)
print(b)
print(c)

str='Python, Java, PHP'

a,b,c=str.split(" ")

print(a)
print(b)
print(c)

str="p"

if str.isalpha():
    print("this is a alphabet.")
else:
    print("not")

# a=5
# if str(a).isdigit():
#     print("this is digit.")
# else:
#     print("not")

a='gh'
if a.isspace():
    print("this is a space.")
else:
    print("not")