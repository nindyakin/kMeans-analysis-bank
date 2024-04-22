# Import library

import gdown
import pandas as pd                                                 # Library used for working with data sets and perform data analysis
import numpy as np                                                  # To perform mathematical operasion and statistics
from datetime import datetime, date                                 # Used to perform dates and time manipulation
import seaborn as sns                                               # To perform data visualization
import matplotlib.pyplot as plt                                     # To perform data visualization
import shutil                                                       # To download and unzip google drive data
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from yellowbrick.cluster import SilhouetteVisualizer
