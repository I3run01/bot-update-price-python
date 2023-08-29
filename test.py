import random

random_num_list = []

def unique_randoms():
    while True:
        random_number = random.randint(0, 99)
        
        if random_number not in random_num_list:
            random_num_list.append(random_number)
            return random_number

for _ in range(100):
    print(unique_randoms())
