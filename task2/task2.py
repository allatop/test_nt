import sys

ellipse_file = sys.argv[1]
points_file = sys.argv[2]

f = open(ellipse_file)
line1 = f.readline()
line2 = f.readline()
f.close()

parts1 = line1.split()
parts2 = line2.split()

cx = float(parts1[0])  
cy = float(parts1[1])  
rx = float(parts2[0])  
ry = float(parts2[1])  

f = open(points_file)
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()
    if line == "":
        continue
    
    parts = line.split()
    x = float(parts[0])
    y = float(parts[1])
    
    s = ((x - cx) ** 2) / (rx ** 2) + ((y - cy) ** 2) / (ry ** 2)
    
    if s < 1:
        print(1)     
    elif s > 1:
        print(2)    
    else:
        print(0)    