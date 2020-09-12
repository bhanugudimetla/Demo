class num_missing:
    def missing_validate(self,comp_data):
        comp_data["LotFrontage"] = comp_data.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))
        for col in ('GarageYrBlt', 'GarageArea', 'GarageCars'):
            comp_data[col] = comp_data[col].fillna(0)
        for col in ('BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF','TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath'):
            comp_data[col] = comp_data[col].fillna(0)
        comp_data['MSZoning'] = comp_data['MSZoning'].fillna(comp_data['MSZoning'].mode()[0])
        comp_data["MasVnrArea"] = comp_data["MasVnrArea"].fillna(0)
        comp_data['Electrical'] = comp_data['Electrical'].fillna(comp_data['Electrical'].mode()[0])
        comp_data['SaleType'] = comp_data['SaleType'].fillna(comp_data['SaleType'].mode()[0])
        comp_data['KitchenQual'] = comp_data['KitchenQual'].fillna(comp_data['KitchenQual'].mode()[0])
        comp_data['Exterior1st'] = comp_data['Exterior1st'].fillna(comp_data['Exterior1st'].mode()[0])
        comp_data['Exterior2nd'] = comp_data['Exterior2nd'].fillna(comp_data['Exterior2nd'].mode()[0])
        return comp_data