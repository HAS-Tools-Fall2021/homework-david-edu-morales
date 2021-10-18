# %%
import numpy as np

# %%
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate((arr1, arr2))

arr4 = np.concatenate((arr1, arr2), axis=0)

arr5 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

five = arr5[1,1]
second_row = arr5[1,:]
# %%
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
# %%
np.concatenate((x, y), axis=0)
# %%
np.concatenate((arr2,arr1), axis=0)
# %%
arr_zeros = np.zeros(10)
# %%
arr_ones = np.ones(10)
# %%
linespace_arr = np.linspace(0, 10, num=5)
# %%
arange_arr = np.arange(8)
# %%
arr_3d = np.array([[[1, 0, 3],
                    [4, 5, 6],
                    [7, 8, 9]],

                   [[1, 2, 3],
                    [4, 0, 6],
                    [7, 8, 9]],

                   [[1, 2, 3],
                    [4, 5, 6],
                    [7, 0, 9]]])

arr_3d[:,:,1]
arr_3d[:,0,:]
# %%
arr_3d.mean()
# %%
arr_3d.mean(axis=0)
arr_3d.mean(axis=1)
arr_3d.mean(axis=2)
# %%
arr_3d[:,0,0]
# %%
