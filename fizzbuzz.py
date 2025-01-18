x = ""

for i in range (100):
    
    
    if i%3 == 0:
        x += ("fizz")

    if i%5 == 0:
        x += ("buzz")

    else:
        x=i
    
    print (x)
    x = ""
