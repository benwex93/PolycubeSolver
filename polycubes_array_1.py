#shapes must be in nxnxn array so the every transformation can fit

import numpy as np

#     __
#    /\ \__
#    \ \/\ \
#     \   \_\
#      \/\/_/

s1 = ((np.array([[[True, False, False, False],
        [True, False, False, False],
        [True, False, False, False],
        [False, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [True, False, False, False],
        [True, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]]]),'b'))

s2 = ((np.array([[[True, False, False, False],
        [True, False, False, False],
        [True, False, False, False],
        [True, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]],

       [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]]]),'r'))


s1long = ((np.array([[[True, False, False, False, False],
        [True, False, False, False, False],
        [True, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [True, False, False, False, False],
        [True, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]]]),'b'))

s2long = ((np.array([[[True, True, True, True, True],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]],

       [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]]]),'b'))

# 2x3x4 
# 6x ----
shapes234 = [s2 for _ in range(6)]

# 2x4x4 
# #4x ---__ 2x ----
shapes244 = [s1 for _ in range(4)]
shapes244 += [s2 for _ in range(3)]

# 2x5x5
#10 ---__
# shapes = [s1 for _ in range(10)]
shapes255 = [s1long for _ in range(10)]

#10 -----
# shapes = [s2long for _ in range(10)]

# 5x5x5
#25 ---__
# shapes = [s1short for _ in range(25)]
shapes555 = [s1long for _ in range(25)]
#25 -----
# shapes = [s2long for _ in range(25)]


# shapes = [s for _ in range(25)]

colors = ('r','b','y')

shapes234 = [(s[0], colors[i % len(colors)]) for i, s in enumerate(shapes234)]

shapes244 = [(s[0], colors[i % len(colors)]) for i, s in enumerate(shapes244)]

shapes255 = [(s[0], colors[i % len(colors)]) for i, s in enumerate(shapes255)]

shapes555 = [(s[0], colors[i % len(colors)]) for i, s in enumerate(shapes555)]
