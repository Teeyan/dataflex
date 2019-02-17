import numpy as np
import pandas as pd
import scipy
import json

class DataManagement:
    
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_pkl(cls, data):
        return cls(data)

    @classmethod
    def from_file(cls, filename, header_file=None, delimiter=","):
        if header_file is None:
            return cls(pd.read_csv(filename, sep=delimiter))
        else:
            with open(header_file, "r") as headers:
                columns = headers.read().strip().split(",")
                return cls(pd.read_csv(filename, sep=delimiter, names=columns))

        
    def get_labels(self): # DONE
        return json.dumps(list(self.data.columns.values))
    
    
    def retrieve_metadata(self, attr_name): # DONE
        """
        Get the mean, median, mode, variance, and num missing values of the provided attr.
        Return as a key value dict of json
        """
        metadata = {}
        metadata["mean"] = self.get_mean(attr_name)
        metadata["median"] = self.get_median(attr_name)
        metadata["mode"] = self.get_mode(attr_name)
        metadata["variance"] = self.get_variance(attr_name)
        metadata["num_null"] = self.get_num_null(attr_name)
        return json.dumps(metadata)
    
    
    def view_values(self, attr_list): # DONE
        """
        View actual points of the provided attr based on data frame
        """
        values = {}
        for attr in attr_list:
            values[attr] = list(self.data[attr].values)
        return json.dumps(values)
    
    
    def normalize(self, attr_name): # DONE
        """
        Normalize the values in the pandas df of the current attr_name
        """
        self.data[attr_name] = (self.data[attr_name] - self.data[attr_name].mean()) / self.data[attr_name].std()
    
    
    def fill_in_missing(self, attr_name, method="mode", default="0"): # DONE
        """
        Fill in null values for the attr_name based on the selected method:
            "mode": most frequent value in the set
            "mean": meaen value of the set
            "default": user defined value of the set (will default to 0)
        """
        if method == "mode":
            self.data[attr_name].fillna(value=self.get_mode(attr_name), inplace=True)
        elif method == "mean":
            self.data[attr_name].fillna(value=self.get_mean(attr_name), inplace=True)
        else:
            self.data[attr_name].fillna(value=default, inplace=True)
            
    
    def correlation_matrix(self, attr_list, method="pearson"):
        """
        Return the correlation matrix of the attr_list
        Will json out as an "adjacency list"
        """
        corr_matrix = self.data.corr(method=method)
        corr_dict = {}
        for attr in attr_list:
            corr_dict[attr] = list(corr_matrix[attr][attr_list].values)
        return json.dumps(corr_dict)
        
        
    def save_csv(self, filename): # DONE
        """
        Save the current data frame as a csv filter
        """
        self.data.to_csv(filename)
    
    
    def drop_attr(self, attr_name): # DONE
        """
        Drop the specified attribute from the list
        """
        self.data.drop(attr_name, axis=1, inplace=True)
    
    """
    Helper Methods for getting meta info
    """
    def get_mean(self, attr_name):
        return self.data[attr_name].mean()
    
    def get_mode(self, attr_name):
        return self.data[attr_name].mode().values[0]
    
    def get_median(self, attr_name):
        return self.data[attr_name].median()
    
    def get_variance(self, attr_name):
        return self.data[attr_name].var()
    
    def get_num_null(self, attr_name):
        return int(self.data[attr_name].isnull().sum())

        
        
    

