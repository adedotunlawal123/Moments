Nmax = 16
Sshow = 7
Smax = Nmax+1

last = [0] * Smax
current = [0] * Smax

def crossbar():
    print("   +", end = '')
    for i in range(Sshow):
        print("-------", end = '')
    print("+-------")

def verify_singlet(N):
    #assert(N%2 == 0)
    if N == 2: 
        return 1
    else:
        Np = N/2
        prod = N
        while N > Np+2:
            N -= 1
            prod *= N
        while Np > 1:
            prod /= Np
            Np -= 1
    return prod

#for i in range(Smax):
#    last[i] = 0
#    current[i] = 0

for i in range(Sshow):
    if i==0:
        print("{:11}".format(i/2.0), end = '')
    else:
        print("{:7}".format(i/2.0), end = '')
print("    num")
crossbar()

for n in range(1,Nmax+1):
    if n == 1:
        last[1] = 1
    else:
        for i in range(Smax):
            jm = i-1
            jp = i+1
            if jm > -1:
                current[jm] += last[i]
            if jp < Smax:
                current[jp] += last[i]
        last = current
        current = [0] * Smax

    #print(n)
    #print(verify_singlet(n))
    #print(last[0])
    #assert n%2 == 1 or verify_singlet(n) == last[0]

    print("{:3}|".format(n), end = '')
    for i in range(Sshow):
        if last[i] == 0:
            print("       ", end = '')
        else:
            print("{:7}".format(last[i]), end = '')
    num_states = 0
    for i in range(Smax):
        num_states += (i+1)*last[i];
    print("|{:7}".format(num_states))
crossbar()
