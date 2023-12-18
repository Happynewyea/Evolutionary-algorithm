from brain import compat, mutanted
import numpy as np

env = np.random.randint(1, 10000001)
env = 1
print("Enviroment Term: ", env)

life = np.random.randint(4999900, 5000101, 10)
print("1 gen :", life)


li = 1
while(env not in life):
    li += 1
    life = compat(life, env)
    #print(life)
    for j in range(8):
        life.append(mutanted(life[0], abs(int((life[0] + life[1]) / 2) - env)))

    #print(i, "gen :", life)
    
print(li, " gen :", life)
print("Enviroment Term: ", env)