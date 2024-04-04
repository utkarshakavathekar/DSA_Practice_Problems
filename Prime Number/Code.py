class Solution:
    def isPrime (self, N):
        # Brute force approach (divide by all number from 2 to N-1)
        prime = 1
        if N==1:
            prime = 0
        for i in range(2,N):
            if N%i==0:
                prime=0
                break
        return prime

        # Better approach (Divide by all numbers from 2 to N//2 as 2 will be the min divisor for most)
        prime = 1
        if N==1:
            prime = 0
        for i in range(2,(N//2)+1):
            if N%i==0:
                prime=0
                break
        return prime

        # Optimized approach (divide by 2 to square_root of that no)
        prime = 1
        if N==1:
            prime = 0
        for i in range(2,int(N**0.5)+1):
            if N%i==0:
                prime=0
                break
        return prime
