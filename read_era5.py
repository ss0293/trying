# TODO: Read data from the era5 formated file

import numpy as np
import matplotlib.pyplot as plt

data=xr.open_mfdataset(data)
data1=data['rainfall']
data1=data1.compute()

