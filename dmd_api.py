# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:43:38 2017

@author: qzh

**Attention**:  This is a 32-bite python script.
"""
# -*- coding:utf-8 -*-
import ctypes
DLL_FILE = "DmdDll_v1.dll"
dll = ctypes.cdll.LoadLibrary(DLL_FILE)

def OpenDevice():
    '''
    打开DMD设备
    Argument:
    - dll文件
    Return：
    - status状态值
    if status == -1:
        print "初始化失败"
    elif status == -2:
        print "设备未连接
    elif status == -3:
        print "FPGA未开启，请重启FPGA"
    '''
    return dll.dmd_OpenDevice()

def CloseDevice():
    '''
    关闭DMD
    if status == -1:
        print "DMD未正常关闭"
    elif status == 1:
        print "DMD正常关闭"
    '''
    return dll.dmd_CloseDevice()

def OpenImgFiles():
    '''
    手动打开文件夹，选择文件载入内部文件列表
    '''
    return dll.dmd_OpenImgFiles()

def ReadSingleImg(filename):
    '''
    传入文件名，写入内部文件列表
    Argument:
    - filename：文件名，包含目录
    Return：
    - file_count内部文件个数
    '''
    OSIBF = dll.dmd_OpenSingleImgByFilename
    OSIBF.argtypes = [ctypes.c_char_p]
    OSIBF.restype = ctypes.c_int
    pStr = ctypes.c_char_p()
    pStr.value = filename
    return OSIBF(pStr)
def LoadOneStep(filename):
	'''
	传入文件名参数，加载图像到内存上，相当于readSingleImg + LoadImgFiles
	'''
	LDOSBF = dll.dmd_LoadDataOneStepByFilename
	LDOSBF.argtypes = [ctypes.c_char_p]
	LDOSBF.restype = ctypes.c_int
	pStr = ctypes.c_char_p()
	pStr.value = filename
	return LDOSBF(pStr)


def SetFrequency(period):
    '''
    设置刷新频率：周期是period*100us
    正常返回1，异常返回-1
    '''    
    sf = dll.dmd_SetFrequency
    sf.argtypes = [ctypes.c_uint]
    sf.restype = ctypes.c_int
    return sf(period)

def LoopShowStart(max_number):
    '''
    开始循环载入的图像
    max_number是载入的图像数
    正常返回1，异常返回-1
    '''
    lss = dll.dmd_LoopShowStart
    lss.argtypes = [ctypes.c_int]
    lss.restype = ctypes.c_int
    return lss(max_number)

def LoopShowHalt(): #有问题
    '''
    停止循环显示模式
    '''
    return dll.dmd_LoopShowHalt()

def LoadImgFiles():
    '''
    加载写入内存的图像
    '''
    return dll.dmd_LoadImgFiles()

def Reset():
    '''
    重启FPGA
    '''
    return  dll.dmd_Reset()

def LoopShowGoOn():
    '''
    继续循环
    '''
    return dll.dmd_LoopShowGoOn()  
def LoopShowStop():
    '''
    停止循环模式，和halt区别？？
    '''
    return dll.dmd_LoopShowStop()
def LoopShowNext():
    '''
    显示下一幅
    '''
    return dll.dmd_LoopShowNext()

def Set_Resolution():
    '''
    默认分辨率是1024*768
    '''
    sr = dll.dmd_SetResolution
    sr.argtypes = [ctypes.c_int]
    sr.restype = ctypes.c_int
    return sr(0)

def ClearImgList():
    '''
    清空内存中的图片列表
    '''
    return dll.ClearImgList()
    
def Demo(im_name, directory=b'C:\\DMD_img\\'):
    '''
    Arguments:
    - im_name: 图片名称
    - directory: 存放图片的目录
    '''
    filename = directory + im_name
    if OpenDevice() != 1:
        print "DMD未连接！"
        return -1
    
    if LoadOneStep(filename) != 1:
        print "没有正确载入图像"
        return -1
    
    LoopShowStart(0)
    return 0
    
    
    
    
if __name__ == "__main__":
    print OpenDevice()
    
