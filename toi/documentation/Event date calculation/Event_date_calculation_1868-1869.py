months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dc(e_y, e_m, e_d, random_days = 100, s_y = 1868, s_m = 1, s_d = 1):
    y, m, d = e_y-s_y, s_m, e_d-s_d
    c = 0
    if m > e_m:
        y -= 1
    days = 0
    while m != e_m:
        days += months[m]
        if m == 12:
            m = 1
        else:
            m += 1
    days += y*365+d
    if random_days % 2 == 1:
        random_days += 1
        c = 1
    print("days =",int(days-random_days*0.5),end=" ")
    if random_days > 0:
        print("random_days =",random_days-c)
    else:
        print()
while True:
    vl = [int(x) for x in input("Enter the date around which you want to receive the event (YYYY MM DD, separated by spaces):").split()]
    r = input("Enter the range in which the event can fire in days:")
    if r == "":
        r = 100
    else:
        r = int(r)
    y = vl[0]
    m = vl[1]
    d = vl[2]
    print("For the End of a New Beginning start date:",end=" ")
    dc(y,m,d,r)
    if y > 1870 or (y == 1870 and m > 5) or (y == 1870 and m == 5 and d >= 19):
        print("For the Blood and Iron start date:",end=" ")
        dc(y,m,d,r,1870,5,19)
    if y > 1885 or (y == 1885 and m > 10):
        print("For the Noon of Empires start date:",end=" ")
        dc(y,m,d,r,1885,11,1)
