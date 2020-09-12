import pandas as pd
class missing_count:
    def missing_num(self,comp_data):
        missing_val = comp_data.isnull().sum().sort_values(ascending=False)
        missing_val_df = pd.DataFrame({'Feature':missing_val.index, 'Count':missing_val.values})
        missing_val_df = missing_val_df.drop(missing_val_df[missing_val_df.Count == 0].index)
        return missing_val_df