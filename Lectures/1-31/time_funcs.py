#Timing a function
import time

def time_func(func, arg):
    'returns time to run func(arg)'
    start = time.time()
    func(arg)
    end = time.time()

    return end-start

def create_list_a(n):
    "creates a list of the first n positive integers"
    L = []                 #l
    for i in range(n):     #l*n times:
        L.append(i+1)      #       1

    return L               #1
                           #--------
                           #1 + 1*n*(1) + 1
                           #n + 2

    L = []                 #c23
    for i in range(n):     #c24*n times:
        L.append(i+1)      #       c25

    return L               #c27
                           #--------
                           #(c25*c24)*n + (c23+c27)

def create_list_b(n):
    'creates a list of the first n positive integers'
    L = []                  #1
    for i in range(n):      #l*n times:
        L.insert(0, n-i)    #  ~n/2
    
    return L                #1
                            #----------
                            # 1 + 1*n^2/2 + 1
                            # (1/2)*n**2 + 2
                            
if __name__ == '__main__':
    #table header
    print('='*40)
    x = 'n'
    y = 't_a (ms)'
    z = 't_b (ms)'
    print(f'{x:<10}{y:<10}{z:<10}')
    print('-'*40)

    for n in [10000, 20000, 50000, 100000]:
        t_a = 1000*time_func(create_list_a, n)
        t_b = 1000*time_func(create_list_b, n)

        print(f'{n:<10}{t_a:<10.3f}{t_b:<10.3f}')