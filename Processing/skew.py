import numpy as np
from scipy.stats import norm, skew
from scipy.special import boxcox1p
import pandas as pd

class skew_validation:
    def validate(self,saleprice):
        if(saleprice.skew()>1.5):
            saleprice = np.log(saleprice+2)
            return saleprice
        else:
            return saleprice
        
    def all_num_skew(self,comp_data):
        numeric_feats = comp_data.dtypes[comp_data.dtypes != "object"].index
        # Check the skew of all numerical features
        skewed_feats = comp_data[numeric_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending=False)
        print("\nSkew in numerical features: \n")
        skewness = pd.DataFrame({'Skew' :skewed_feats})
        
        skewness = skewness[abs(skewness) > 0.75]
        print("There are {} skewed numerical features to Box Cox transform".format(skewness.shape[0]))
        
        skewed_features = skewness.index
        lam = 0.15
        for feat in skewed_features:
            comp_data[feat] = boxcox1p(comp_data[feat], lam)
        return comp_data