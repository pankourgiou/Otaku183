import time


t1 = time.time()

name = input("Enter your name: ")
print("Hello", name + "!")
Age = input("Enter your Age: ")
print(Age)
Hungry = input("Are you hungry?")
print(Hungry)
Sleepy = input("Do you feel like sleeping?")
print(Sleepy)
print("That's all folks!")

t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
