import random
a = random.randint(0, 100)
if a < 30:
    print("Rainy")
elif a < 60:
    print("Cloudy")
else:
    print("Sunny")