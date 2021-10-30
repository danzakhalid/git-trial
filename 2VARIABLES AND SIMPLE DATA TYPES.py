 # Create an empty list
l = []  
# 31 because the end of the range is exclusive
for i in range(3, 31):
    # if equal to zero it is a multiple of 3
    if i % 3 == 0:  
        # add it to the list
        l.append(i)   
l = [i for i in range(3, 31) if i % 3 == 0]
squares = []
for value in range(1,11, 1):
 squares.append(value**3)
print(squares)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])





