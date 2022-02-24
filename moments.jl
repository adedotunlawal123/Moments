using Printf

Nmax = 16
Sshow = 7
Smax = Nmax+1

function crossbar()
   @printf("   +")
   for i in 1:Sshow
      @printf("-------")
   end
   @printf("+-------\n")
end

function verify_singlet(N)
   @assert N%2 == 0
   if N == 2
      return 1
   else
      Np = N/2
      prod = N
      while N > Np+2
         N -= 1
         prod *= N
      end
      while Np > 1
         prod /= Np
         Np -= 1
      end
   end
   return prod
end

let
   last = zeros(Smax)
   current = zeros(Smax)

   for i in 1:Sshow
      if i==1
         @printf("%11.2f",i/2.0)
      else
         @printf("%7.2f",i/2.0)
      end
   end
   println("    num")
   crossbar()

   for n in 1:Nmax
      if n == 1
         last[2] = 1
      else
         for i in 1:Smax
            jm = i-1
            jp = i+1
            if jm >= 1
               current[jm] += last[i]
            end
            if jp <= Smax
               current[jp] += last[i]
            end
         end
         last = current
         current = zeros(Smax)
      end
      @printf("%3d|",n)
      for i in 1:Sshow
         if last[i] == 0
            print("       ")
         else
            @printf("%7d",last[i])
         end
      end
      num_states = 0
      for i in 1:Smax
         num_states += i*last[i]
      end
      @printf("|%7d\n",num_states)
   end
   crossbar()
end
