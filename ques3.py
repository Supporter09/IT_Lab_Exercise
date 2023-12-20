
distance = float(input())
speed = float(input())

hour = distance / speed # Calculate time take to go that dist
# YOUR CODE HERE
if distance <= 2:
    print(12000)
else:
    res = 12000
    res += (distance - 2) * 3500 # Add money dist take
    res += (hour - 2/speed) * 350 # Add hour fee
    res = round(res, 0)
    print(int(res))


