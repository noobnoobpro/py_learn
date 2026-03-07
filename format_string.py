
a=1
txt=f"this is a format {a} string"
print(txt)
txt=f"this is a format {a:.3f} string"
print(txt)

cost=16 #euro
txt= 'more than 10'if cost>10 else 'less than 10'
print(txt)

# above can be replaced with format string by using
txt =f"it is very {'expensive'if cost>10 else 'cheap'}"
print(txt)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
