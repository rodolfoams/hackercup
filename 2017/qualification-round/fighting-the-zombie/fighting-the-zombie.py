def read_int():
    return int(raw_input())

def read_int_tuple(str_in=None, sep=" "):
    if str_in is None:
        str_in = raw_input().strip()
    return tuple(map(int, str_in.split(sep)))

def read_string_array():
    return raw_input().strip().split(" ")

def generate_simulation(n_sides, throws):
    counters = [0] * (n_sides * throws + 1)
    counters[0] = 1
    for i in xrange(throws):
        new_counters = [0] * (n_sides * throws + 1)
        for j in xrange(i,i*n_sides+1):
            for k in xrange(1,n_sides+1):
                new_counters[j+k] += counters[j]
        counters = list(new_counters)
    return counters
        
def probability_of_killing(s, h):
    add = 0
    if "-" in s:
        add -= int(s.split("-")[1])
        s = s.split("-")[0]
    if "+" in s:
        add += int(s.split("+")[1])
        s = s.split("+")[0]
    x, y = read_int_tuple(s,"d")
    h -= add

    counters = generate_simulation(y, x)
    total_results = 0
    killing_results = 0.0
    for i in xrange(len(counters)):
        total_results += counters[i]
        if i >= h: killing_results += counters[i]
        
    return killing_results/total_results

def solve(h, s):
    spells = read_string_array()
    max_probability = 0.0
    for spell in spells:
        p = probability_of_killing(spell, h)
        max_probability = max(max_probability, p)
    return max_probability

def main():
    t = read_int()
    for i in xrange(1, t+1):
        h, s = read_int_tuple()
        ans = solve(h, s)
        print "Case #%d: %.6f" % (i, ans)

if __name__ == "__main__":
    main()
