
import random
num_of_picks = int(input("Enter the number of picks: "))
rand_out = []

for i in range(0, num_of_picks):
    dif = i * 6
    for x in range(0, 6):
        rand_int = random.randint(1, 46)
        while rand_int in rand_out[0+dif:6+dif]:
            rand_int = random.randint(1, 46)
        rand_out.append(rand_int)

    print(sorted(rand_out[0+dif:6+dif]))
