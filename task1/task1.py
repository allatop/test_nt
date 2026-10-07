import sys

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

def get_path(n, m):
    path = ""
    i = 1
    
    while True:
        path = path + str(i)

        for j in range(m - 1):
            i = i + 1
            if i > n:
                i = 1
            
        if i == 1:
            break
    
    return path


result = get_path(n1, m1) + get_path(n2, m2)
print(result)