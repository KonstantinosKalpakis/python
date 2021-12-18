n = [1,2,3,4,5,6,7,8,9,10,15,16,20,30]

for i in n:
    print('Weird') if (i % 2 == 1) or ((i%2 == 0) and i > 20) else print('Not Weird')
