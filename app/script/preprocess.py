from config import config
import pandas as pd

def impute(df):
    for col in config.IMPUTER:
        df[col]=df[col].fillna(config.IMPUTER[col])
    return df

def label_cate(df):
    for c in config.ONE_HOT_VECTOR:
         df[c]=df[c].map(config.ONE_HOT_VECTOR[c])
         broken_df=pd.DataFrame(df[c].to_list(), columns = [c+"_"+str(i) for i in config.ONE_HOT_VECTOR[c]])
         df=pd.concat([df,broken_df],axis=1)
         df=df.drop(c,axis=1)
    return df
def preprocess_data(data):
    df=pd.DataFrame(data)
    df=df[config.FINAL_COLUMNS]
    df=impute(df)
    df=label_cate(df)
    return df[config.POST_PROCESSING]