def fizzbizz(n):
    for i in range(1,n):
        if i % 15 == 0:
            print 'fizzbizz'
        elif i % 5 == 0:
            print 'bizz'
        elif i % 3 == 0:
            print 'fizz'
        else:
            print i

print fizzbizz(25)
