import random


def flip_coin() :
    num_flip = int(input("Enter number of times to flip the coin (positive number) : "))
    
    while num_flip <= 0 :
        print("Enter positive number")
        num_flip = int(input("Enter number of times to flip the coin (positive number) : "))
    
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flip):
        if random.random() < 0.5 :
            heads_count += 1
        else :
            tails_count += 1
    
    head_per = (heads_count / num_flip) * 100
    tails_per = (tails_count / num_flip) * 100
    
    print(f"Number of flip is {num_flip}")
    print(f"Heads count : {heads_count} Percentage : {head_per: .2f}%")
    print(f"Tails count : {tails_count} Percentage : {tails_per: .2f}%")

flip_coin()
    
            
        