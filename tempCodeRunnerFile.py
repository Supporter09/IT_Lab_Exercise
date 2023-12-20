ax, ay, bx, by, cx, cy = [float(i) for i in input().split()]

# YOUR CODE HERE
# Check if it is a line => if not check which type of triangle
ab_x = bx - ax
ab_y = by - ay
ac_x = cx - ax
ac_y = cy - ay

if ((cy - by)*(bx - ax) == (by - ay)*(cx - bx)):
    print('line')
else:
    ab = (ab_x**2 + ab_y**2)
    ac = (ac_x**2 + ac_y**2)
    bc = ((cx - bx)**2 + (cy - by)**2)
    arr = [ab, ac, bc]
    arr.sort()
    if arr[-1] == arr[0] + arr[1]:
        print('right')
    elif arr[-1] < arr[0] + arr[1]:
        print('acute')
    else: 
        print('obtuse')