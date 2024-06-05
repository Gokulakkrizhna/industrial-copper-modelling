# Industrial Copper Modeling
## Overview
This project enables users to delve into copper modeling trends. After retrieving and cleaning sample data, insights are derived through exploratory data analysis (EDA). The cleaned data is then applied in different machine learning algorithm for predicting selling price using Regression models and classified status using Classification models.
## Table of Contents
- [Key Technologies and Skills](#key-technologies-and-skills)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Approach](#approach)
- [Contact](#contact)
# Key Technologies and Skills
- Python Scripting
- Streamlit
- Data Cleaning and analysis
- Pandas-Dataframe
- Numpy
- EDA Analysis
- Scikit-Learn
- Pickle
# Installation
To run this project, please install below python packages as prerequisites.

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install numpy
pip install scipy
pip install category_encoders
pip install scikit-learn
```
# Usage
To use this project, Please follow the below steps.
- To clone this repository: ```git clone https://github.com/Gokulakkrizhna/industrial-copper-modelling.git```
- Install the required packages: ```pip install -r requirements.txt ```
- To extract and clean data:```python Datacoll_dataclean.py```
- To perform EDA analysis:```python analysis.py```
- Run the Streamlit app: ```streamlit run Dataextract_visual.py```
- Access the app in your browser at ```http://localhost:8501```
# Features
- Fetch Copper modeling data from Excel file
- Data Cleaning and pre-processing
- Perform EDA analysis
- Perform Machine Leanrning analysis
- User-friendly interface powered by Streamlit
# Approach
```Data Collection```: Clone the copper modeling data from your local directory. 

```Data Cleaning```: Refine pre-processing methods like Data handling is applied to the collected data.

```Statistical Analysis```: Cleaned numerical data has been analysed to get a valuable insights.

```EDA Analysis```: The cleaned data has been analyzed using various exploratory data analysis (EDA) techniques, revealing insights into current trends.

```Setup the Streamlit app```: Streamlit is a user-friendly web development tool that simplifies the process of creating intuitive interfaces.

```Data Analysis```: Cleaned data has been analyzed and visualized in Streamlit through Pandas DataFrame.

```Machine Learning```: Cleaned data has been applied in different machine learning algorithm to predict and classify the data.

The provided code utilizes Python scripting along with various libraries to fetch data from the our local directory. Data manipulation techniques are then applied, followed by exploratory data analysis (EDA) on the cleaned dataset to extract meaningful insights. Furthermore, the implementation includes a Streamlit web application to enhance user friendly dashboard.

Here's a breakdown of what the code does:
- Importing all the neccessary libraries includes ```Streamlit``` which creates UI to interact with user and display the analysed data, ```Pandas``` which helps to display the analysed data in Streamlit web,```numpy``` which will help in mathematical conversion,```Plotly```  is employed to visualize the data and gain insights from it,```Scipy``` aids in conducting exploratory data analysis (EDA) and extracting valuable insights, ```category_encoders``` used to convert categorical values to numerical data,```pickle``` is used to load the trained model.
```bash
import pandas as pd
import category_encoders as ce
import numpy as np
from scipy.stats import spearmanr
import scipy.stats as stats
import streamlit as st
import pickle
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
```
- ```Datacoll_dataclean``` file is responsible for fetching data from the local directory and performing necessary data cleaning operations. **Note: Replace your file name in ```df```**
```bash
df = pd.read_excel("please provide the file name here")
```
- ```analysis``` file is responsible for exploratory data analysis (EDA) and extracting valuable insights.
- ```Dataextract_visual``` file is used to display the predicted and classified data from ML model and display over the streamlit dashboard.
- Three separate tabs have been implemented in the Streamlit web application to facilitate user interaction and enhance data visualization for insightful analysis.
```bash
tab1, tab2, tab3= st.tabs(["Home", "Statistical Insights","EDA Insights"])
```
- In Tab1 of the Streamlit web application,Users can input various data to receive the corresponding predicted selling price and classified status.
- In Tab2, Cleaned data has undergone Statistical analysis procedure to get a valuable insights.
- In Tab3, exploratory data analysis (EDA) was conducted on the dataset to extract valuable insights, which are then presented to the user for further analysis and interpretation.

This Python script streamlines the process of fetching data from a local directory, implementing crucial data cleaning procedures, and conducting exploratory data analysis (EDA) to extract valuable insights. Analysed data was applied on ML to predict Selling price and classify the status.

# Contact
📧 Email: [gokulakkrizhna@gmail.com](mailto:gokulakkrizhna@gmail.com)

🌐 LinkedIn: [linkedin.com/in/gokulakkrizhna-s-241562159](https://www.linkedin.com/in/gokulakkrizhna-s-241562159/)

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
