# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
def error_diffusion(pixel, size): 
    '''
      Diffuse on a single channel, using Floyd-Steinberg kerenl.
      @param pixel PIL PixelAccess object.
      @param size A tuple to represent the size of pixel.
      Reference: 
      1.matlab version: https://cn.mathworks.com/matlabcentral/fileexchange/
      6953-error-diffusion-algorithm?focused=5058869&tab=function&requestedDomain=www.mathworks.com
      2.pseudo code: http://www.dfstudios.co.uk/articles/
      programming/image-programming-algorithms/image-processing-algorithms-part-2-error-diffusion/
      
    '''
    for x in range(size[0]):
        for y in range(size[1]):
            oldpixel = pixel[x,y]
            pixel[x, y] = 255 if oldpixel > 127 else 0
            quant_error = oldpixel - pixel[x, y]
            if x + 1 < size[0]:
                pixel[x+1, y] += int(7/16.0 * quant_error) #不能是float型，必须是整型，否则会报错：
            if y + 1 < size[1] and x - 1 >= 0: #SystemError: new style getargs format but argument is not a tuple
                pixel[x-1, y+1] += int(3/16.0 * quant_error)
            if y + 1 < size[1]:
                pixel[x,   y+1] += int(5/16.0 * quant_error)
            if x + 1 < size[0] and y + 1 < size[1]:
                pixel[x+1, y+1] += int(1/16.0 * quant_error)       

if __name__ == "__main__":
    im = Image.open("1.jpg").convert('L')
    pixel = im.load()
    error_diffusion(pixel, im.size)
    im.show()
