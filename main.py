from brain import compat, mutanted
import numpy as np

env = np.random.randint(1, 1000000)

print("Enviroment Term: ", env)

life = np.random.randint(499900, 500100, 10)
print("1 gen :", life)



for i in range(2, 1001):
    life = compat(life, env)
    #print(life)
    for j in range(5):
        life.append(mutanted(life[0], abs(life[0] - env)))
    for k in range(3):
        life.append(mutanted(life[1], abs(life[1] - env)))

    #print(i, "gen :", life)
    
print("1000 gen :", life)
print("Enviroment Term: ", env)