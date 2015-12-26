import fileinput

def surface(l,w,h):
    return 2 * (l*w + l*h + w*h)

def min_area(l,w,h):
    return min(l*w, l*h, w*h)

def total(l,w,h):
    return surface(l,w,h) + min_area(l,w,h)

def min_peri(l,w,h):
    return 2*min(l+w, l+h, w+h)

def volume(l,w,h):
    return l*w*h

def ribbon(l,w,h):
    return min_peri(l,w,h) + volume(l,w,h)

if __name__ == "__main__":
    total_ribbon = 0
    for line in fileinput.input():
        param = map(int, line.split('x'))
        total_ribbon += ribbon(param[0], param[1], param[2])

    print total_ribbon

"""
    total_area = 0
    for line in fileinput.input():
        param = map(int, line.split('x'))
        total_area += total(param[0], param[1], param[2])

    print total_area

"""