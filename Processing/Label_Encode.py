from sklearn.preprocessing import LabelEncoder

class encoder:
    def lable_encode(self,comp_data):
        columns = ('FireplaceQu', 'BsmtQual', 'BsmtCond', 'GarageQual', 'GarageCond', 
                'ExterQual', 'ExterCond','HeatingQC', 'PoolQC', 'KitchenQual', 'BsmtFinType1', 
                'BsmtFinType2', 'Functional', 'Fence', 'BsmtExposure', 'GarageFinish', 'LandSlope',
                'LotShape', 'PavedDrive', 'Street', 'Alley', 'CentralAir', 'MSSubClass', 'OverallCond', 
                'YrSold', 'MoSold')
        for col in columns:
            labl = LabelEncoder() 
            labl.fit(list(comp_data[col].values)) 
            comp_data[col] = labl.transform(list(comp_data[col].values))
            return comp_data