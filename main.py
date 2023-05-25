from functions import clean, wait
while True:
    clean()
    print('(0) Leave')
    print('(1) Add student')
    print('(2) Show List')
    print('(3) Delete all registries')
    option = input()
    if option == '0':
        break
    elif option == '1':
        name = input('Name: ')
        email = input('E-mail: ')
        file = open('p1.crs','a') #w write #r read #a append
        file.write(name+' | '+email+'\n')
        file.close()
        print('Data Saved')
        wait(5)
    elif option == '2':
        try:
            file = open('p1.crs', 'r')
            data = file.read()
            print(data)
            file.close()
            wait(5)
        except:
            print('Database not found')
            print('We are creating one for you!')
            file = open('p1.crs', 'w')
            file.close()
            wait(2)
    else:
        print("Invalid Option!")
        wait(2)
