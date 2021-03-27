months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def rdc(s_y,s_m,s_d,d):
    d += s_d
    e_y = s_y + d // 365
    d = d % 365
    m = s_m
    while d > months[m]:
        d -= months[m]
        if m == 12:
            m = 1
            e_y += 1
        else:
            m += 1
    if d == 0:
        m -= 1
        d = months[m]
    print("The end date is ",e_y,".",m,".",d,sep="")


while True:
    vl = [int(x) for x in input("Enter the start date (YYYY MM DD, separated by spaces):").split()]
    if vl == []:
        y = 1857
        m = 5
        d = 11
    else:
        y = vl[0]
        m = vl[1]
        d = vl[2]
    r = int(input("Enter the amount of days from the start date:"))
    rdc(y,m,d,r)
