import string
import random

U = string.ascii_uppercase
l = string.ascii_lowercase

motsDePasse = []
for i in range(36):
    motsDePasse.append(random.choice(l) + random.choice(U) + random.choice(U) + random.choice(U) + '-' + random.choice(l) + random.choice(U) + random.choice(U) + random.choice(U))
    


    
