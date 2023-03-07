from decimal import *

def is_prime(number):
    for x in range(2,number):
        if ((number%x)==0):
            return False
    return True

def one_over_prime(prime):
    numerator=Decimal('1')
    denominator=Decimal(f'{prime}')
    fraction=(numerator/denominator)
    fraction=(f'{fraction}')
    fraction=fraction[2:]
    decimal_list=list()
    decimal_pattern=list()
    decimal_working_set=list()
    match_length=-1
    length=0
    stoplength=-2
    if (prime>1000):
        ignore_leading_zeros=-3
    else:
        ignore_leading_zeros=0
    for decimal in fraction:
        if ( ignore_leading_zeros>0 and stoplength==match_length and decimal==decimal_list[0]):
            pattern=True
            for x in range(match_length):
                if (decimal_working_set[x] != decimal_list[x]):
                    pattern=False
            if (pattern):
                return decimal_working_set
        if (match_length!=-1 and decimal == decimal_list[match_length]):
            if(match_length==0):
                stoplength=length
            decimal_working_set.append(decimal)
            match_length+=1
        else:
            decimal_working_set=list()
            match_length=0
        decimal_list.append(decimal)
        decimal_pattern.append(decimal)
        length+=1
        ignore_leading_zeros+=1
        if (match_length==-1):
            match_length+=1
    else:
        return []



nums=list(range(1,1000))
primes=list(filter(is_prime,nums))
#print(primes)
decimal_patterns=list()
getcontext().prec=2000
for prime in primes:
    decimal=one_over_prime(prime)
    is_cyclic=''
    decimal_patterns.append(prime)
    clean_decimal=''.join(map(str,decimal))
    length=len(decimal)
    if (length==(prime-1)):
        is_cyclic='*Cyclic*'
        if ((prime-1)%10==0):
            is_cyclic="**Proper Prime**"
    print(f'1/{prime} :  {length} {is_cyclic}')
