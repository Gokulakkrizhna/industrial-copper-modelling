import pandas as pd
import category_encoders as ce
import numpy as np


def data_collection():
    df = pd.read_excel("Copper_Set.xlsx")
    return df

def fill_nan(df, group_cols, target_col, method):
    if method == 'mode':
        modes = df.groupby(group_cols)[target_col].apply(lambda x: x.mode().iloc[0])

        def fill_mode(row):
            if pd.isna(row[target_col]):
                return modes[tuple(row[col] for col in group_cols)]
            return row[target_col]
        
        df.loc[:, target_col] = df.apply(fill_mode, axis=1)

    elif method == 'mean':
        means = df.groupby(group_cols)[target_col].mean()

        def fill_mean(row):
            if pd.isna(row[target_col]):
                return means[tuple(row[col] for col in group_cols)]
            return row[target_col]
        
        df.loc[:, target_col] = df.apply(fill_mean, axis=1)

    return df


def outlier_handling(df1):

    upper_limit = df1['selling_price'].mean() + 3*df1['selling_price'].std()
    lower_limit = df1['selling_price'].mean() - 3*df1['selling_price'].std()
    df1['selling_price'] = np.where(df1['selling_price']>upper_limit,upper_limit,df1['selling_price'])
    df1['selling_price'] = np.where(df1['selling_price']<lower_limit,lower_limit,df1['selling_price'])

    upper_limit = df1['quantity tons'].mean() + 3*df1['quantity tons'].std()
    lower_limit = df1['quantity tons'].mean() - 3*df1['quantity tons'].std()
    df1['quantity tons'] = np.where(df1['quantity tons']>upper_limit,upper_limit,df1['quantity tons'])
    df1['quantity tons'] = np.where(df1['quantity tons']<lower_limit,lower_limit,df1['quantity tons'])

    upper_limit = df1['thickness'].mean() + 3*df1['thickness'].std()
    lower_limit = df1['thickness'].mean() - 3*df1['thickness'].std()
    df1['thickness'] = np.where(df1['thickness']>upper_limit,upper_limit,df1['thickness'])
    df1['thickness'] = np.where(df1['thickness']<lower_limit,lower_limit,df1['thickness'])

    upper_limit = df1['width'].mean() + 3*df1['width'].std()
    lower_limit = df1['width'].mean() - 3*df1['width'].std()
    df1['width'] = np.where(df1['width']>upper_limit,upper_limit,df1['width'])
    df1['width'] = np.where(df1['width']<lower_limit,lower_limit,df1['width'])

    return df1


    
def data_cleaning(df):
    df1 = df[[ 'quantity tons', 'customer', 'country', 'status','item type', 'application', 'thickness', 'width','product_ref', 'selling_price']]

    df1 = fill_nan(df1,['product_ref', 'item type','status'],'country','mode')
    df1 = fill_nan(df1,['product_ref', 'item type','country','status'],'application','mode')
    df1 = fill_nan(df1,['product_ref', 'item type','country','application'],'status','mode')
    df1 = fill_nan(df1,['product_ref', 'item type','country','application'],'customer','mode')
    df1 = fill_nan(df1,['product_ref', 'item type','country','application'],'thickness','mode')
    df1 = fill_nan(df1,['product_ref', 'item type','country','status','application'],'selling_price','mean')
   
    df1 = df1[df1["quantity tons"] != "e"]
    df1["quantity tons"] = df1["quantity tons"].astype("float")

    df1 = df1[df1["selling_price"] >= 1]
    df1 = df1[df1["quantity tons"] > 0]

    encoder = ce.OrdinalEncoder(cols=[ 'status', 'item type'])
    df1 = encoder.fit_transform(df1)

    df1_min = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_min.append(min(df1[i]))

    df1_max = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_max.append(max(df1[i]))

    df1_mean = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_mean.append(int(df1[i].mean())) 

    df1_median = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_median.append(df1[i].median()) 

    df1_mode = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_mode.append(df1[i].mode()[0]) 
    
    df1_stddev = []
    for i in ['quantity tons','thickness', 'width','selling_price']:
        df1_stddev.append(df1[i].std()) 

    df1 = outlier_handling(df1)

    df1["quantity tons"] = np.log10(df1["quantity tons"])
    df1["thickness"] = np.log10(df1["thickness"])
    df1["width"] = np.log10(df1["width"])
    df1["selling_price"] = np.log10(df1["selling_price"])

    return df1,df1_min,df1_max,df1_mean,df1_median,df1_mode,df1_stddev


a = data_collection()
a,b,c,d,e,f,g = data_cleaning(a)
print(f)