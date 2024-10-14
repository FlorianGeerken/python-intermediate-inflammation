"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:
    """
    Loads all the inflammation CSV files within a specified directory.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path


    def load_inflammation_data(self):

        """
        Gets all the inflammation data from CSV files within a directory,

        :param data_dir: path to uploaded datafiles
        :return: 2D data array with inflammation data
        """
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)# Load inflammation data from each CSV file

        return list(data)# Return the list of 2D NumPy arrays with inflammation data

class JSONDataSource:
    """
    Loads all the inflammation JSON files within a specified directory.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path


    def load_inflammation_data(self):

        """
        Gets all the inflammation data from JSON files within a directory,

        :param data_dir: path to uploaded datafiles
        :return: 2D data array with inflammation data
        """
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)# Load inflammation data from each JSON file

        return list(data)# Return the list of 2D NumPy arrays with inflammation data

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.


    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data = data_source.load_inflammation_data()

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation

def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets
    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    return daily_standard_deviation





# CONTROLLER
# _, extension = os.path.splitext(infiles[0])
# if extension == '.json':
#   data_source = JSONDataSource(os.path.dirname(infiles[0]))
# elif extension == '.csv':
#   data_source = CSVDataSource(os.path.dirname(infiles[0]))
# else:
#   raise ValueError(f'Unsupported data file format: {extension}')
# analyse_data(data_source)



# eigen oplossing controller:
# file_name  = os.path.dirname(infiles[0])
#
# if file_name.endswith(".json"):
#     data_source = JSONDataSource(file_name)
# elif file_name.endswith(".csv"):
#     data_source = CSVDataSource(file_name)


# analyse_data(data_source)