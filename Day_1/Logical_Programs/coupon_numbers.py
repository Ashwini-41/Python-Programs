import random

def get_distinct_coupon(n) :
    coupons = set()
    count = 0
    
    while len(coupons) < n:
        get_coupons = random.randint(1,n)
        coupons.add(get_coupons)
        count += 1
    
    print(f"Total random number generated are {count}")

get_distinct_coupon(5)
    