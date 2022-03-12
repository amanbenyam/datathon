import sys
with open(sys.argv[1], 'r') as f:
     #f.readline()
     out = open(sys.argv[2], "w")
     #f.readline()
     for i in range(100):
             f_line = f.readline()
             out.write(f_line)
