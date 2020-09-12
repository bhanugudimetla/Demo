from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

class Model_build:
    
    def build(self,X_train, X_test, y_train, y_test):
        GBoost = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10)
        GBoost.fit(X_train, y_train)
        GBoost_pred = GBoost.predict(X_test)
        df=pd.DataFrame(GBoost_pred,y_test)
        print("y pre vs y actual",df.head())
        return mean_squared_error(y_test, GBoost_pred)
    
    
        