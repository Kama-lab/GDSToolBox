with open('requirements.txt') as f:
    line = f.readlines()

with open('ignore_req_packages.txt') as f2:
    line2 = f2.readline()

m = line2
print(len(line))

for l in m:
    for l2 in line2:
        if l.strip() == l2.strip():
            m.remove(l)

print(len(m))
