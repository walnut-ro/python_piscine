from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_grey
from pimp_image import ft_blue
import numpy as np

array = ft_load("landscape.jpg")
ft_invert(array)
print(ft_invert.__doc__)
ft_red(array)
print(ft_red.__doc__)
ft_green(array)
print(ft_green.__doc__)
ft_blue(array)
print(ft_blue.__doc__)
ft_grey(array)
print(ft_grey.__doc__)

#example_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    
#ft_invert(example_array)
#ft_red(example_array)
#ft_green(example_array)
#ft_blue(example_array)
#ft_grey(example_array)