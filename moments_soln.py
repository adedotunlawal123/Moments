import math
Nmax = 16;
Sshow = 7;
Smax = Nmax+1;

last = [0] * Smax
current = [0] * Smax

def crossbar(): # Draw the box in which answer is displayed
    print("   +", end = '')
    for i in range(Sshow):
        print("-------", end = '')
    print("+-------")

def verify_singlet(N): # Function for verifying total number of singlet (S =0) States
    # (!) write the function body
    return math.gamma(N+1)//math.gamma((N/2)+1)//math.gamma((N/2)+2) #math.gamma is a factorial for real numbers 
    
    
#for i in range(Smax):
#    last[i] = 0
#    current[i] = 0

for i in range(Sshow): # Function to print the column labels (The different spin states)
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
        # (!) increment elements of current
        for i in range(0, Nmax):
            current[i] = last[i-1] + last[i+1]
        last = current 
        current = [0] * Smax
            
        

    # (!) uncomment the following line
    assert n%2 == 1 or verify_singlet(n) == last[0]

    print("{:3}|".format(n), end = '') # Print left most column
    for i in range(Sshow):
        if last[i] == 0:
            print("       ", end = '')
        else:
            print("{:7}".format(last[i]), end = '')
    num_states = 2**n # Number of states according to formula
    # (!) accumulate values in num_states
    print("|{:7}".format(num_states))
crossbar() # End dash lines of box
