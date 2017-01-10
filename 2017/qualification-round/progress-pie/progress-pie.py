import math

def read_int():
    return int(raw_input())

def read_int_tuple():
    return tuple(map(int, raw_input().strip().split()))

def distance(x1, y1, x2, y2, x3, y3):
    return abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)/math.sqrt((y2-y1)**2 + (x2-x1)**2)

def solve(p, x3, y3):
    x1 = 0
    y1 = 0
    x2 = 50*math.sin(2*math.pi*p/100)
    y2 = 50*math.cos(2*math.pi*p/100)
    x3 -= 50
    y3 -= 50

    if math.hypot(x3,y3) > 50 + 1./(10**6): return "white"
    if p == 0: return "white"
    if p == 100: return "black"
    if distance(x1, y1, x2, y2, x3, y3) <= 1./(10**6): return "black"

#    print "x2: %.2f; y2: %.2f; x3: %.2f; y3: %.2f" % (x2,y2,x3,y3)

    if x3>=0 and y3>=0:
        if p >= 25: return "black"
        if x3 == 0: return "black"
#        print "Point on first quadrant"
#        print "Point slope is %.2f.\nLimit slope is %.2f" % (float(x3)/y3, x2/y2)
        if float(y3)/x3 < y2/x2: return "white"
        return "black"
    elif x3>=0:
        if p >= 50: return "black"
        if p <= 25: return "white"
#        print "Point on second quadrant"
#        print "Point slope is %.2f.\nLimit slope is %.2f" % (float(y3)/x3, y2/x2)
        if float(y3)/x3 < y2/x2: return "white"
        return "black"
    if x3<0 and y3<=0:
        if p >= 75: return "black"
        if p <= 50: return "white"
#        print "Point on third quadrant"
#        print "Point slope is %.2f.\nLimit slope is %.2f" % (float(y3)/x3, y2/x2)
        if float(y3)/x3 < y2/x2: return "white"
        return "black"
#    print "Point on fourth quadrant"
#    print "Point slope is %.2f.\nLimit slope is %.2f" % (float(y3)/x3, y2/x2)
    if p <= 75: return "white"
    if float(y3)/x3 < y2/x2: return "white"
    return "black"
        

def main():
    t = read_int()
    for i in xrange(1,t+1):
        p, x, y = read_int_tuple()
        ans = solve(p, x, y)
        print "Case #%d: %s" % (i, ans)

if __name__ == "__main__":
    main()
