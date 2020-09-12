class cat_missing:
    def cat_validate(self,comp_data):
        for col in ('PoolQC', 'MiscFeature', 'Alley'):
            comp_data[col] = comp_data[col].fillna('None')
        comp_data["MasVnrType"] = comp_data["MasVnrType"].fillna("None")
        comp_data["Fence"] = comp_data["Fence"].fillna("None")
        comp_data["FireplaceQu"] = comp_data["FireplaceQu"].fillna("None")
        for col in ('GarageType', 'GarageFinish', 'GarageQual', 'GarageCond'):
            comp_data[col] = comp_data[col].fillna('None')
        for col in ('BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2'):
            comp_data[col] = comp_data[col].fillna('None')
        comp_data['MSSubClass'] = comp_data['MSSubClass'].fillna("None")
        comp_data['SaleType'] = comp_data['SaleType'].fillna(comp_data['SaleType'].mode()[0])
        comp_data = comp_data.drop(['Utilities'], axis=1)
        comp_data['OverallCond'] = comp_data['OverallCond'].astype(str)
        comp_data["Functional"] = comp_data["Functional"].fillna("Typ") 
        comp_data['MSSubClass'] = comp_data['MSSubClass'].apply(str)
        comp_data['YrSold'] = comp_data['YrSold'].astype(str)
        comp_data['MoSold'] = comp_data['MoSold'].astype(str)
        return comp_data