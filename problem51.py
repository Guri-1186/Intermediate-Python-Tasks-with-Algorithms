#create numpy 3 dimension array with shape(3,4,4) and set to a variable
import numpy as np
import numpy as np
#solution 1
arr = np.array([
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ],
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ],
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
])



#solution 2
arr = np.tile([1,2,3,4], (3,4,1))
print(arr)
print("Shape:", arr.shape)