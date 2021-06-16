class Cleaning():
    
    def __init__(self,df):
        self.df = df
        
    def find_columns(self):
        return list(self.df.columns)
    
    def find_null(self):
        import missingno
        print(self.df.isna().sum())
        return missingno.matrix(self.df);
        
    def find_duplicates(self,keep=False,subset=None):
        return self.df[self.df.duplicated(subset=subset,keep=keep)]
    
    def financial_to_float(self,column):
        self.df[column]=self.df[column].map(lambda x: float(x.replace('$','').replace(',','')))
        print(f'the dtype of {column} column was updated to {self.df[column].dtype}')
