def read_int():
    return int(raw_input().strip())

def solve(n):
    weights = list()
    for i in xrange(n): weights.append(read_int())
    weights.sort(reverse=True)
    trips = 0
    while len(weights) > 0 and weights[0] * len(weights) >= 50:
        trips += 1
        top_weight = weights[0]
        weights.remove(top_weight)
        if top_weight >= 50: continue
        for i in xrange(50/top_weight - 1):
            weights.pop()
        if 50 % top_weight != 0:
            weights.pop()
    return trips

def main():
    t = read_int()
    for i in xrange(1, t+1):
        n = read_int()
        ans = solve(n)
        print "Case #%d: %d" % (i, ans)

if __name__ == "__main__":
    main()
