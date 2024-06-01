from Datacoll_dataclean import a,b,c,d,e,f,g
import pandas as pd
from scipy.stats import spearmanr
import scipy.stats as stats


def statistical_analysis(df,b,c,d,e,f,g):
    correlation_matrix = df.corr()

    a_dict = {"Category":['quantity tons','thickness', 'width','selling_price'],
              "Min":b,"Max":c,"Mean":d,"Median":e,"Mode":f,"Standard Deviation":g}

    df1 = pd.DataFrame(a_dict)

    return correlation_matrix,df1


def eda_analysis_sp(df1):
    correlation, p_value = spearmanr(df1['selling_price'], df1['quantity tons'])

    correlation, p_value1 = spearmanr(df1['selling_price'], df1['customer'])

    price_by_country = {}
    for country_category in df1['country'].unique():
        key = country_category
        price_by_country[key] = df1[(df1['country'] == country_category)]['selling_price']
    statistic,p_value2 = stats.kruskal(*price_by_country.values())

    price_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        price_by_status[key] = df1[(df1['status'] == status_category)]['selling_price']
    statistic1,p_value3 = stats.kruskal(*price_by_status.values())

    price_by_item = {}
    for item_category in df1['item type'].unique():
        key = item_category
        price_by_item[key] = df1[(df1['item type'] == item_category)]['selling_price']
    statistic2,p_value4 = stats.kruskal(*price_by_item.values())

    price_by_application = {}
    for application_category in df1['application'].unique():
        key = application_category
        price_by_application[key] = df1[(df1['application'] == application_category)]['selling_price']
    statistic3,p_value5 = stats.kruskal(*price_by_application.values())

    correlation, p_value6 = spearmanr(df1['selling_price'], df1['thickness'])

    correlation, p_value7 = spearmanr(df1['selling_price'], df1['width'])

    price_by_product = {}
    for product_category in df1['product_ref'].unique():
        key = product_category
        price_by_product[key] = df1[(df1['product_ref'] == product_category)]['selling_price']
    statistic8,p_value8 = stats.kruskal(*price_by_product.values())

    return p_value,p_value1,p_value2,p_value3,p_value4,p_value5,p_value6,p_value7,p_value8


def eda_analysis_st(df1):
    quantity_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        quantity_by_status[key] = df1[(df1['status'] == status_category)]['quantity tons']
    statistic1,p_value = stats.kruskal(*quantity_by_status.values())

    customer_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        customer_by_status[key] = df1[(df1['status'] == status_category)]['customer']
    statistic1,p_value1 = stats.kruskal(*customer_by_status.values())

    country_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        country_by_status[key] = df1[(df1['status'] == status_category)]['country']
    statistic1,p_value2 = stats.kruskal(*country_by_status.values())

    item_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        item_by_status[key] = df1[(df1['status'] == status_category)]['item type']
    statistic1,p_value3 = stats.kruskal(*item_by_status.values())

    application_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        application_by_status[key] = df1[(df1['status'] == status_category)]['application']
    statistic1,p_value4 = stats.kruskal(*application_by_status.values())

    thickness_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        thickness_by_status[key] = df1[(df1['status'] == status_category)]['thickness']
    statistic1,p_value5 = stats.kruskal(*thickness_by_status.values())

    width_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        width_by_status[key] = df1[(df1['status'] == status_category)]['width']
    statistic1,p_value6 = stats.kruskal(*width_by_status.values())

    product_ref_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        product_ref_by_status[key] = df1[(df1['status'] == status_category)]['product_ref']
    statistic1,p_value7 = stats.kruskal(*product_ref_by_status.values())

    price_by_status = {}
    for status_category in df1['status'].unique():
        key = status_category
        price_by_status[key] = df1[(df1['status'] == status_category)]['selling_price']
    statistic1,p_value8 = stats.kruskal(*price_by_status.values())

    return p_value,p_value1,p_value2,p_value3,p_value4,p_value5,p_value6,p_value7,p_value8



s1,s2 = statistical_analysis(a,b,c,d,e,f,g)
e1,e2,e3,e4,e5,e6,e7,e8,e9 = eda_analysis_sp(a)
E1,E2,E3,E4,E5,E6,E7,E8,E9 = eda_analysis_st(a)

