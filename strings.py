a = 25
b = 2 

#Method 1
text = "I'm {} age and have exp of {}"
print(text.format(a,b))

#Method 2
text = "I'm {0} age and have exp of {1}"
print(text.format(a,b))

#Method 3
text = f"I'm {a} age and have exp of {b}"
print(text)


