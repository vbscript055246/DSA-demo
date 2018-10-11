# 1
score = int(input())
if score >= 90:
    print("A")
elif 89 >= score > 60:
    print("B")
else:
    print("C")

# 2
for i in range(1, 10):
    for j in range(1, 10):
        print("{:<3d}".format(i*j), end="")
    print()


# 3
meter = 100
sum = 0
for i in range(10):
    sum += meter
    meter = meter / 2

print("共經過:" + str(sum) + "公尺")
print("高度:" + str(meter) + "公尺")

# 4
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp > 0:
        sum += (temp % 10) ** 3
        temp = temp // 10
    if sum == i:
        print(i)

print()
# 5
marker = [0] * 5
array = [0] * 3
def dfs(ptr):
    global marker, array
    if ptr < 3:
        for i in range(5):
            if marker[i] == 0:
                array[ptr] = i+1
                marker[i] = 1
                dfs(ptr+1)
                marker[i] = 0
    else:
        for i in array:
            print(i, end="")
        print()


dfs(0)


# 6
start = 1
for i in range(10):
    start += 1
    start *= 2
print(start)

# 7
def output(a, b):
    for i in range(a):
        print(" ", end="")
    for i in range(b):
        print("*", end="")
    print()


for i in range(3):
    output(3 - i, i * 2 + 1)
output(0, 7)
for i in range(2, -1, -1):
    output(3 - i, i * 2 + 1)


# 8
F = [1, 1]
while len(F) <= 22:
    F.append(F[-1]+F[-2])

ans = 0
for i in range(20):
    ans += F[i+3]/F[i+2]
print(ans)

# 9
sieve = [0]*100
prime = []

def linear_sieve():
    global prime, sieve
    for i in range(2, 100):
        if sieve[i] == 0:
            prime.append(i)
        for j in prime:
            if i*j >= 100:
                break
            sieve[i*j] = 1
            if i == j:
                break

linear_sieve()

print("{}, 共{}個".format(prime, len(prime)))


