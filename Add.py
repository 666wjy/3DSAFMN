import scipy as sp
import numpy as np
# 相同体素数目、相同体素大小数字岩心叠加
# 定义模型尺寸
# Nx=400
# Ny=400
# Nz=400
# voxel_size = 4.5e-7 # 定义模型分辨率
# copy_factor = 4
# # 读取数字岩心文件
# # 1为孔隙，0为基质
# matrix1 = np.fromfile('100-0.026.thresholded.raw', dtype='int8')
# print('Size of matrix1:', matrix1.size)
# print('Shape of matrix1:', matrix1.shape)
# matrix1 = matrix1.reshape((100, 100, 100))
# resized_matrix1 = np.repeat(matrix1, repeats=copy_factor, axis=0)
# resized_matrix1 = np.repeat(resized_matrix1, repeats=copy_factor, axis=1)
# resized_matrix1 = np.repeat(resized_matrix1, repeats=copy_factor, axis=2)
# print(matrix1.shape)
# print(type(matrix1))
# # matrix+=1
# print('length of data is: ', len(matrix1))
# print('voxel number in data is: ', np.size(matrix1))
# phase_list = np.unique(matrix1)
# print('voxel value in matrix1 is: ')
# print(phase_list)
#
# matrix2 = np.fromfile('400-0.0065.thresholded.raw', dtype='int8')
# matrix2 = matrix2.reshape((Nx, Ny, Nz))
# # matrix+=1
# print('length of data is: ', len(matrix2))
# print('voxel number in data is: ', np.size(matrix2))
# phase_list = np.unique(matrix2)
# print('voxel value in matrix2 is: ')
# print(phase_list)
#
# # 合并数字岩心
# dual = resized_matrix1 | matrix2
#
#
# # 导出raw文件
# dual = dual.flatten()
# dual.tofile('sp_result_400.raw')

def RawAdd (Nx,Ny,Nz,copy_factor,matrix1_path,matrix2_path,Sx,Sy,Sz,output_path):

    # 相同体素数目、相同体素大小数字岩心叠加
    # 读取数字岩心文件
    # 1为孔隙，0为基质
    matrix1 = np.fromfile(matrix1_path,dtype='int8')
    matrix1 = matrix1.reshape((Sx,Sy,Sz))

    resized_matrix1 = np.repeat(matrix1, repeats=copy_factor, axis=0)
    resized_matrix1 = np.repeat(resized_matrix1, repeats=copy_factor, axis=1)
    resized_matrix1 = np.repeat(resized_matrix1, repeats=copy_factor, axis=2)

    matrix2 = np.fromfile(matrix2_path, dtype='int8')
    matrix2 = matrix2.reshape((Nx, Ny, Nz))

    # 合并数字岩心
    dual = resized_matrix1 | matrix2
    # 导出raw文件
    dual = dual.flatten()
    dual.tofile(output_path)

