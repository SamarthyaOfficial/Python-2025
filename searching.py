import numpy as np
np1 = np.array([1,2,3,4,5,6,7,8,9,10]);

print(np1[np.where(np1%2==0)[0]]) #PRINTING THE EVEN NUMBERS IN THE ARRAY
 
filtered = np1 % 2 == 1
print(filtered);
print(np1[filtered]);
