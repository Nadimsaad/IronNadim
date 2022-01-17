Readme File Project 5: Data visualization and reporting in Streamlit (Group4  DAFT NOV21)

First we imported the libraries 
streamlit as st, pandas as pd, numpy as np, from sklearn import datasets
matplotlib.pyplot as plt, plotly.graph_objects as go, from plotly import tools
plotly.offline as py, plotly.express as px, from cycler import cycler
seaborn as sns and warnings

Then we imported the IBM csv file dataset

We gave a title to our Streamlit ("IBM Employees KPI Dashboard")

And placed a relevant photo to the topic ('Attrition')

We place the key metrics in a checkbox

#################### information on dataset ##################################
We installed the widget on the side bar/ 1er selection

We use an st.checkbox('Click here to select general information on DATASET')
followe by an if condition to select from :
    a sidebar "Selection1 -in general"
    "Choose your table:",
        "Descriptive statistique", 
        "Employees and income by Department", 
        "Salary, max, min and mean", and
        "IBM Employees Job Satisfaction"

    if "Descriptive statistique" is chosen
        st.write('Theme: List of IBM Employees')
        st.write ('Describe : ', IBM.describe())

    elif "Employees and income by Department":
        st.markdown('**Total of employee** by department.')
        st.table(IBM['Department'].value_counts())   
        st.markdown('**Montly Income in average** by department.')
        st.table(IBM.groupby(by=['Department'])['MonthlyIncome'].mean())
         
    elif "Salary, max, min and mean":
      We can chose from 3 columns
       'Maximum Salary  
       'Average Salary $ ' 
       'Average Salary $ ' 

    elif "IBM Employees Job Satisfaction":
      IBM.JobSatisfaction.value_counts
        
        fig3 plots the pie chart "Job Satisfaction"
   we propose two other charts
        a bar chart 
        or a line chart
        
#################### scatter Logic - relevant on attrition ##################################
if 'Click here to Scatter Chart, relevant to the attrition'):
     we use the sidebar "Scatter Chart: According Attrition status explore different caracteristics"

    we name the columns in the following lists
    measurements = IBM.drop(labels=["Attrition"], axis=1).columns.tolist()
    x_axis = st.sidebar.selectbox("X-Axis", measurements)
    y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)


    if x_axis and y_axis: 
       we plot the scatter chart


########## Bar Chart Logic - relevant to attrition  ##################
if checkbox 'Click here to Bar Chart, relevant to the attrition' is selected
we plot the Bar Chart "According to Attrition Status, explore caracteristics"

    # we delete from measure nn-numeric colums": 'Department','EducationField','MaritalStatus','MaritalStatus',
    indexbarshart=['Age', 'DistanceFromHome',
     'Education',
     'EnvironmentSatisfaction',
     'JobSatisfaction',
     'MonthlyIncome',
     'NumCompaniesWorked',
     'WorkLifeBalance',
     'YearsAtCompany']
     we show the attrition mean
    "Average of columns Per Attrition Status"

    if bar_axis:
        we show the "Average Per Attrition Status Type" based the corresponding parameters
    else:
        "Average Per Attrition Status Type" based on the relevant parameters


################# Histogram Logic -relevant to all compagny ########################
if checkbox 'Click here to Histogram, relevant to the whole company' is selected
    we do the Histogram: "Explore caracteristics of the whole company"
    
    if hist_axis:
       we draw the histogram "Distribution of Measurements" based the corresponding parameters
        
    else:
        "Distribution of Measurements" based on the relevant parameters

        
#################### Hexbin Chart Logic - relevant to all compagny##################################

if checkbox('Click here to Hexbin Chart, relatif to the whole company' is selected
    we do a Hexbin Chart: Explore company caracteristics:"
    based on the name of columns in lists
    'Age', 'DistanceFromHome','Education','EnvironmentSatisfaction',
     'JobSatisfaction','MonthlyIncome','NumCompaniesWorked','WorkLifeBalance','YearsAtCompany'
        

#################### selection on attrition ##################################  

if checkbox('Click here to select information on ATTRITION') is selected
    
    # Install the widget on the side bar / 1er selection
    we display the sidebar "Selection2 - for attrition" 
    to choose a graph from "Attrition", "Department","Income", "Marital Status", "WorkLifeBalance"})

    if selection == 'Attrition':
        "Attrition Key Metrics"
         we display 2 charts
         Chart 1 - Bar chart
         Chart 2 - Pie Chart
     
    if selection == "Department":
        #Chart 4 'Attrition and Years in the company per department'
     
    elif selection == 'Income':
        we display 'Monthly Income distribution'        

    elif selection == "Marital Status":
        we draw the pie chart 'Marital Satus, for the ones who left company' 
        #WorkLifeBalance, for the ones who left the company
    
    elif selection == "WorkLifeBalance":
       we draw the chart 'Work Life Balance, for the ones who left company'
        