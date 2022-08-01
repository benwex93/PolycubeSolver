import numpy as np
#       __
#      /\_\
#     / / /
#    / / /
#    \ \ \
#     \ \_\
#      \/_/

# s1 = [((0,0,0),'r'), ((1,0,0),'r'), ((2,0,0),'r'), ((0,1,0),'r'), ((0,2,0),'r')]

s1 = ((np.array([[	[True, True, True, False],
			        [True, False, False, False],
			        [True, False, False, False],
			        [False, False, False, False]],

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
#      _ __
#   __/\/\_\
#  /\__  / /
#  \/__\/_/

#s2 = [((0,0,0),'b'), ((0,0,1),'b'), ((0,1,0),'b'), ((1,1,0),'b'), ((1,2,0),'b')]

s2 = ((np.array([[	[True, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'b'))
#     __
#    /\ \__
#    \ \/\ \
#     \   \_\
#      \/\/_/

# s3 = [((0,0,0),'b'), ((1,0,0),'b'), ((2,0,0),'b'), ((2,1,0),'b'), ((3,1,0),'b')]

s3 = ((np.array([[	[True, True, True, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, True, True],
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
			        [False, False, False, False]]]),'b'))
#        __
#   ____/\_\
#  /\__/ / /
#  \/_   \_\
#     \/\/_/

# s4 = [((0,0,0),'r'), ((0,0,1),'r'), ((1,0,0),'r'), ((1,1,0),'r'), ((2,1,0),'r'), ((1,2,0),'r')]

s4 = ((np.array([[	[True, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'r'))
#    __  __
#   /\ \/\_\
#   \ \_ / /
#    \/_ \_\
#     \/\/_/

# s5 = [((0,0,0),'y'), ((1,0,0),'y'), ((0,1,0),'y'), ((0,-1,0),'y'), ((0,0,1),'y'), ((-1,0,1),'y')]

s5 = ((np.array([[	[False, False, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [True, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'y'))
#     __
#    /\_\
#   / / /__
#  / / /__ \
#  \/____ \_\
#        \/_/

# s6 = [((0,0,0),'b'), ((1,0,0),'b'), ((0,0,1),'b'), ((0,0,2),'b'), ((0,1,2),'b'), ((0,2,2),'b')]

s6 = ((np.array([[	[True, True, True, False],
			        [False, False, True, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'b'))
#     __
#    /\ \_
#   / / / \
#   \ \____\
#    \_____/

# s7 = [((0,0,0),'r'), ((0,1,0),'r'), ((1,0,0),'r'), ((0,0,-1),'r'), ((1,0,-1),'r')]

s7 = ((np.array([[	[True, True, False, False],
			        [True, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
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
#      __
#     /\_\
#    / / /__
#   / / / __\
#   \/_ \_\_/
#      \/_/

# s8 = [((0,0,0),'b'), ((0,1,0),'b'), ((0,2,0),'b'), ((0,0,-1),'b'), ((1,0,-1),'b'), ((0,0,-2),'b')]

s8 = ((np.array([[	[True, True, True, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'b'))
#      __
#     /\_\
#    / / /
#   / / /\
#   \/_ \_\
#      \/_/

# s9 = [((0,0,0),'y'), ((0,1,0),'y'), ((0,2,0),'y'), ((0,0,-1),'y'), ((1,0,-1),'y')]

s9 = ((np.array([[	[True, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'y'))
#      __
#     /\_\
#    / / /__
#    \ \____\
#     \/____/  
#       \/_/

# s10 = [((0,0,0),'y'), ((0,1,0),'y'), ((1,0,0),'y'), ((1,0,-1),'y'), ((1,-1,-1),'y')]

s10 = ((np.array([[	[False, False, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [True, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'y'))
#      __
#     /\_\
#    / / /\
#   / /  \_\
#   \/_/\/_/
#     

# s11 = [((0,0,0),'y'), ((0,1,0),'y'), ((0,-1,0),'y'), ((0,0,-1),'y'), ((1,0,-1),'y')]

s11 = ((np.array([[	[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, True, False, False],
			        [False, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'y'))
#      __
#     /\_\_
#    / / /_\
#   / / ___/
#  / / /
#  \/_/   

# s12 = [((0,0,0),'r'), ((0,1,0),'r'), ((0,0,-1),'r'), ((0,-1,0),'r'), ((0,-2,0),'r')]

s12 = ((np.array([[	[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, True, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]],

			       [[True, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False],
			        [False, False, False, False]]]),'r'))

shapes = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]