G = 0.0000000000667408
M = input('what is the mass of the thing producing the gravity? Or type earth for earth. ')
if M == 'earth':
    M = float(5.972 * 10**24)
else:
    M = float(M)
m = float(input('what is the mass of the object? '))
r = float(input('how far is the object from the thing pruducing the gravity? '))
f = (G * M * m)/r ** 2

print ('this is the force on gravity on that planet: %s neutons' % f)

