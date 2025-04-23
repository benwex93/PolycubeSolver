import numpy as np

#     __
#    /\ \__
#    \ \/\ \
#     \   \_\
#      \/\/_/

shape = [((0,0,0),'b'), ((1,0,0),'b'), ((2,0,0),'b'), ((2,1,0),'b'), ((3,1,0),'b')]

shapes_ls = []
for i in range(25):
	shapes_ls.append((shape, f's{i + 1}'))
# shapes_ls = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]