# TODO: Read data from the era5 formated file

import numpy as np
import matplotlib.pyplot as plt
import numpy as np

data=xr.open_mfdataset(data)
data1=data['rainfall']
data1=data1.compute()

#import data for the plot

data11=data1.mean(dim='time').compute()

data11.plot()


