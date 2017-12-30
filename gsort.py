import json
from functools import cmp_to_key

f = open('input.txt')
myfile = f.read()

def gettotal(a1,b1,c1,a2,b2,c2):
    total1 = int(a1,16)+int(b1,16)+int(c1,16)
    total2 = int(a2,16)+int(b2,16)+int(c2,16)
    return [total1,total2]

def compare_colors(a,b):
    first = a['value']
    second = b['value']
    a1 = first[1:]
    a2 = second[1:]

    r1 = a1[0:1]
    g1 = a1[2:3]
    b1 = a1[4:5]
    
    r2 = a2[0:1]
    g2 = a2[2:3]
    b2 = a2[4:5]
    
    if r1 > g1 and r1 > b1:
        r1 += "FF"
    if g1 > r1 and g1 > b1:
        g1 += "FF"
    if b1 > g1 and g1 > r1:
        b1 += "FF"
    
    totals = gettotal(r1,g1,b1,r2,g2,b2)
    total1 = totals[0]
    total2 = totals[1]
    if total1 < total2:
        return 1
    elif total1 == total2:
        return 0
    else:
        return -1

def outputcolors(arr):
    for x in arr:
        print(x['name']+':          '+x['value'])

parsed = json.loads(myfile)

greygrad = []
redgrad = []
bluegrad = []
greengrad = []

for item in parsed:
    v = item['value'][1:]
    r = int(v[0:1],16)
    g = int(v[2:3],16)
    b = int(v[4:5],16)
    greydiff = 2
    if abs(r-g) < greydiff and abs(r-b) < greydiff and abs(g-b) < greydiff:
        greygrad.append(item)
    elif r > g and r >b:
        redgrad.append(item)
    elif g > r and g > b:
        greengrad.append(item)
    elif b > r and b > g:
        bluegrad.append(item)

greyg = sorted(greygrad,key=cmp_to_key(compare_colors))
greeng = sorted(greengrad,key=cmp_to_key(compare_colors))
redg = sorted(redgrad,key=cmp_to_key(compare_colors))
blueg = sorted(bluegrad,key=cmp_to_key(compare_colors))

outputcolors(redg)
outputcolors(greeng)
outputcolors(blueg)
outputcolors(greyg)
