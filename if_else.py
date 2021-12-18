n = [1,2,3,4,5,6,7,8,9,10,15,16,20,30]

for i in n:
    if i % 2 == 1:
        print('Weird')
    elif i % 2 == 0 and (2 <= i <= 5):
        print('Not Weird')
    elif i % 2 == 0 and (6 <= i <= 20):
        print ('Weird')
    elif i % 2 == 0:
        print ('Not Weird')
    
        
