G = 0.0000000000667408
solve_for = input('solve for? M,m,r or f ')

if solve_for != 'M':
    M = input('what is the mass of the thing producing the gravity? Or type earth for earth. ')
    if M == 'earth':
        M = float(5.972 * 10**24)
    else:
        M = float(M)
if solve_for != 'm':
    m = float(input('what is the mass of the object? '))
if solve_for != 'r':
    r = float(input('how far is the object from the thing pruducing the gravity? Radius of earth is 6,371,000 m. '))
if solve_for != 'f':
    f = float(input('what is the force on the object? '))

if solve_for == 'M':
    answer = (f*r**2)/(G*m)
if solve_for == 'm':
    answer = (f*r**2)/(G*M)
if solve_for == 'r':
    answer = ((G*M*m)/f)**(1/2)
if solve_for == 'f':
    answer = (G*M*m)/r**2

print ('Answer: %s' % answer)

