n = int(input('Qual termo deseja encontrar : '))

u = 1

p = 1

if (n==1) or (n==2):

        print('1')

else:

        for count in range(2,n):

                termo = u + p

                p = u

                u = termo

                count += 1

        print(termo)