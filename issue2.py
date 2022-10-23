def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal

print( binaryTodecimal(101) ) #5
print( binaryTodecimal(1010) ) #10
print( binaryTodecimal(0) ) #0
print( binaryTodecimal(1) ) #1
print( binaryTodecimal(1000) ) #8
print( binaryTodecimal(11111) ) #31
print( binaryTodecimal(100) ) #4
print( binaryTodecimal(111) ) #7
print( binaryTodecimal(1101) ) #13