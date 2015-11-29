import random
count = 0.0
inside_circle = 0.0
while True:
    x = random.random()
    y = random.random()
    distance_origin = (x**2 + y**2)**0.5
    count+= 1
    if distance_origin < 1 :
        inside_circle += 1
    ratio = 4 *( inside_circle / count)
    estimate = ratio
    print "{}      ::      {}".format(count,estimate) 


