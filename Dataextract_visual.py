from Datacoll_dataclean import a,b,c
from analysis import s1,s2,e1,e2,e3,e4,e5,e6,e7,e8,e9,E1,E2,E3,E4,E5,E6,E7,E8,E9 
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def streamlit():
    tab1, tab2, tab3= st.tabs(["Home", "Statistical Insights","EDA Insights"])
    S = {
        'Won': 1,
        'Draft': 2,
        'To be approved': 3,
        'Lost': 4,
        'Not lost for AM': 5,
        'Wonderful': 6,
        'Revised': 7,
        'Offered': 8,
        'Offerable': 9
    }
    I = {
        'W': 1,
        'WI': 2,
        'S': 3,
        'Others': 4,
        'PL': 5,
        'IPL': 6,
        'SLAWR': 7
    }

    with tab1:
        st.markdown('<h1 style="text-align: center; color: red;">Industrial Copper Modeling</h1>', unsafe_allow_html=True)
        tab4,tab5 = st.tabs(["Selling Price","Status"])
        with tab4:
            col1, col2 = st.columns(2)
            with col1:
                Quan = np.log10(st.number_input("Enter the Quantity tons between {0} and {1}".format(b[0],c[0]), value=b[0], placeholder="Type a number..."))
                cust = st.number_input("Enter the Customer number {0} and {1}".format(min(a["customer"]),max(a["customer"])), value=None, placeholder="Type a number...")
                thick = np.log10(st.number_input("Enter the thickness value {0} and {1}".format(b[1],c[1]), value=b[1], placeholder="Type a number..."))
                width = np.log10(st.number_input("Enter the width value {0} and {1}".format(b[2],c[2]), value=b[2], placeholder="Type a number..."))
                status = st.selectbox("Select the status",['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM','Wonderful', 'Revised', 'Offered', 'Offerable'])
                status = S[status]

            with col2:
                country = float(st.selectbox("Select a country",[ '28',  '25',  '30',  '32',  '38',  '78',  '27',  '77', '113',  '79',  '26','39',  '40',  '84',  '80', '107',  '89']))
                item = st.selectbox("Select the Item type",['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR'])
                item = I[item]
                Application = float(st.selectbox("Select the Application",['2', '3', '4', '5', '10', '15', '19', '20', '22', '25', '26', '27', '28', '29', '38', '39', '40', '41', '42', '56', '58', '59', '65', '66', '67', '68', '69', '70', '79', '99']))
                product = int(st.selectbox("Select the product",['611728', '611733', '611993', '628112', '628117', '628377', '640400', '640405', '640665', '929423819', '1282007633', '1332077137', '164141591', '164336407', '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']))

            if st.button("Predict Selling Price"):
                with open('pred.pkl', 'rb') as file:
                    model = pickle.load(file)
                
                y_pred = model.predict([[Quan,cust,country,status,item,Application,thick,width,product]])
                pred_val = 10**(y_pred)

                st.subheader(":red[Predicted Selling price:] {0}".format(pred_val[0]))

        with tab5:
            col3,col4 = st.columns(2)
            with col3:
                    Quan = np.log10(st.number_input("Enter the Quantity ton between {0} and {1}".format(b[0],c[0]), value=b[0], placeholder="Type a number..."))
                    cust = st.number_input("Enter the Customer ID {0} and {1}".format(min(a["customer"]),max(a["customer"])), value=None, placeholder="Type a number...")
                    thick = np.log10(st.number_input("Enter the Thickness value {0} and {1}".format(b[1],c[1]), value=b[1], placeholder="Type a number..."))
                    width = np.log10(st.number_input("Enter the Width value {0} and {1}".format(b[2],c[2]), value=b[2], placeholder="Type a number..."))
                    price = np.log10(st.number_input("Enter the Selling price {0} and {1}".format(b[3],c[3]), value=b[3], placeholder="Type a number..."))

            with col4:
                country = float(st.selectbox("Select a Country",[ '28',  '25',  '30',  '32',  '38',  '78',  '27',  '77', '113',  '79',  '26','39',  '40',  '84',  '80', '107',  '89']))
                item = st.selectbox("Select the item type",['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR'])
                item = I[item]
                Application = float(st.selectbox("Select the spplication",['2', '3', '4', '5', '10', '15', '19', '20', '22', '25', '26', '27', '28', '29', '38', '39', '40', '41', '42', '56', '58', '59', '65', '66', '67', '68', '69', '70', '79', '99']))
                product = int(st.selectbox("Select the Product",['611728', '611733', '611993', '628112', '628117', '628377', '640400', '640405', '640665', '929423819', '1282007633', '1332077137', '164141591', '164336407', '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']))

            if st.button("Predict Status"):
                with open('class.pkl', 'rb') as file:
                    model = pickle.load(file)
                
                y_pred = model.predict([[Quan,cust,country,item,Application,thick,width,product,price]])

                if y_pred == 1:
                    st.subheader(":red[Predicted Status:] Won")
                else:
                    st.subheader(":red[Predicted Status:] Lost")

    with tab2:
        st.header(":red[Correlation using Heatmap]")

        fig = px.imshow(s1, text_auto=True, aspect="auto",color_continuous_scale="reds")
        fig.update_layout(coloraxis_colorbar=dict(title="Correlation"))
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("Do you like to see statistical data"):
            st.dataframe(s2)

    with tab3:
        tab6,tab7 = st.tabs(["Selling Price", "Status"])

        with tab6:
            #Analysis1
            st.header(":red[Analysis of Quantity over Price]")
            if e1 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between amount of quantity and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between amount of quantity and their prices. It is a strong evidence.           
                """)

            #Analysis2
            st.header(":red[Analysis of customer and price]")
            if e2 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between customer and selling price of product. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between customer and selling price of product. It is a strong evidence.           
                """)
            
            #Analysis3
            st.header(":red[Analysis for country and price]")
            if e3 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different countries and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different countries and their prices. It is a strong evidence.           
                """)

            #Analysis4
            st.header(":red[Analysis for status Over price]")
            if e4 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different status and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different status and their prices. It is a strong evidence.           
                """)

            #Analysis5
            st.header(":red[Analysis for price over item type]")
            if e5 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between over each item type and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between over each item type and their prices. It is a strong evidence.           
                """)
            
            #Analysis6
            st.header(":red[Analysis for Application over price]")
            if e6 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different application and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different application and their prices. It is a strong evidence.           
                """)

            #Analysis7
            st.header(":red[Analysis for thickness over price]")
            if e7 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different thickness of product and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different thickness of product and their prices. It is a strong evidence.           
                """)

            #Analysis8
            st.header(":red[Analysis for width over price]")
            if e8 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different width of product and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different different width of product  and their prices. It is a strong evidence.           
                """)

            #Analysis9
            st.header(":red[Analysis of Product reference over price]")
            if e9 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different product reference and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different product reference and their prices. It is a strong evidence.           
                """)

        with tab7:
            #Analysis1
            st.header(":red[Analysis of Quantity over Status]")
            if E1 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between amount of quantity and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between amount of quantity and their status. It is a strong evidence.           
                """)

            #Analysis2
            st.header(":red[Analysis of customer and status]")
            if E2 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between customer and status of each product. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between customer and status of each product. It is a strong evidence.           
                """)
            
            #Analysis3
            st.header(":red[Analysis for country and status]")
            if E3 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different countries and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different countries and their status. It is a strong evidence.           
                """)

            #Analysis4
            st.header(":red[Analysis for item type over status]")
            if E4 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different item types and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different item types and their status. It is a strong evidence.           
                """)

            #Analysis5
            st.header(":red[Analysis for status over application]")
            if E5 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different application and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different application and their status. It is a strong evidence.           
                """)
            
            #Analysis6
            st.header(":red[Analysis for Thickness over status]")
            if E6 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different thickness of product and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different thickness of product and their status. It is a strong evidence.           
                """)

            #Analysis7
            st.header(":red[Analysis for width over price]")
            if E7 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different width of product and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different width of product and their status. It is a strong evidence.           
                """)

            #Analysis8
            st.header(":red[Analysis for Product reference over status]")
            if E8 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different Product reference and their status. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different different Product reference and their status. It is a strong evidence.           
                """)

            #Analysis9
            st.header(":red[Analysis of status over price]")
            if E9 < 0.05:
                st.markdown("""
                - P-Value < 0.05
                - Reject H0
                - Dependent
                - From this we can conclude that there is a significant connection between different status and their prices. It is a strong evidence.           
                """)
            else:
                st.markdown("""
                - P-Value > 0.05
                - Fail to Reject H0
                - Independent
                - From this we can conclude that there is no connection between different status and their prices. It is a strong evidence.           
                """)


streamlit()