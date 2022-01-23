#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 18:44:41 2022

@author: nadimsaad
"""

# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets

breast_cancer = datasets.load_breast_cancer(as_frame=True)

breast_cancer_df = pd.concat((breast_cancer["data"], breast_cancer["target"]), axis=1)

breast_cancer_df["target"] = [breast_cancer.target_names[val] for val in breast_cancer_df["target"]]

pd.set_option("display.max_columns", 50)
st.title("Breast Cancer Stats")

measurements = breast_cancer_df.drop(labels=["target"], axis=1).columns.tolist()


X_axis = st.sidebar.selectbox("X-axis", measurements)
Y_axis = st.sidebar.selectbox('Y-axis', measurements)

if X_axis and Y_axis:
    figure = plt.figure(figsize=(6,4))
    scatter_1 =figure.add_subplot(111)

    malignant_df = breast_cancer_df[breast_cancer_df["target"] == "malignant"]
    benign_df = breast_cancer_df[breast_cancer_df["target"] == "benign"]
    
    malignant_df.plot.scatter(x=X_axis, y=Y_axis, ax=scatter_1,c='r', label="Malignant")
    benign_df.plot.scatter(x=X_axis, y=Y_axis, ax=scatter_1,c='b', label='Benign')

else:
    figure = plt.figure(figsize=(6,4))
    scatter_1 = figure.add_subplot(111)

    malignant_df = breast_cancer_df[breast_cancer_df["target"] == "malignant"]
    benign_df = breast_cancer_df[breast_cancer_df["target"] == "benign"]
    
    malignant_df.plot.scatter(x="mean texture", y="mean area",c='r', ax=scatter_1, label="Malignant")
    benign_df.plot.scatter(x="mean texture", y="mean area", ax=scatter_1, label='Benign')


avg_breast_cancer_df = breast_cancer_df.groupby("target").mean()
 
multi_measures= st.sidebar.multiselect('measurements names', measurements,default=["mean radius","mean area"],key=1)


if multi_measures:  
    figure1 = plt.figure(figsize=(6,4))
    bar1 = figure1.add_subplot(111)
    sub_avg_breast_cancer_df = avg_breast_cancer_df[multi_measures]
    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar1, title="Average Measurements per Tumor Type"); # plotting the data
else: 
    figure1 = plt.figure(figsize=(6,4))
    bar1 = figure1.add_subplot(111)
    sub_avg_breast_cancer_df = avg_breast_cancer_df[["mean radius", "mean texture", "mean perimeter", "area error"]]
    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar1, title="Average Measurements per Tumor Type");
    

multi_measures2 = st.sidebar.multiselect('measurements names', measurements,default=["mean radius","mean texture", "mean perimeter", "area error"],key=2)

""""Create radio buttons and link them with a histogram to select bins of a histogram. """
radio_bins = st.sidebar.radio("bins", [10,20,30,40,50])

if radio_bins:
    figure2 = plt.figure(figsize=(6,4))
    hist1 = figure2.add_subplot(111)
    sub_df = breast_cancer_df[multi_measures2]
    sub_df.plot.hist(bins=radio_bins, ax=hist1)
else:
    figure2 = plt.figure(figsize=(6,4))
    hist1 = figure2.add_subplot(111)
    sub_df = breast_cancer_df["mean radius", "mean texture"]
    sub_df.plot.hist(bins=radio_bins, ax=hist1)
    

hex_x = st.sidebar.selectbox("Hex_X-axis", measurements)
hex_y = st.sidebar.selectbox('Hex_Y-axis', measurements)

if hex_x and hex_y:
    figure3 = plt.figure(figsize=(6,4))
    hex1 = figure3.add_subplot(111)
    hex_x_df = breast_cancer_df[hex_x]
    hex_y_df = breast_cancer_df[hex_y]
    plt.hexbin(hex_x_df, hex_y_df)
else:
    figure3 = plt.figure(figsize=(6,4))
    hex1 = figure3.add_subplot(111)
    hex_x_df = breast_cancer_df['mean_texture']
    hex_y_df = breast_cancer_df['mean_area']
    plt.hexbin(hex_x_df, hex_y_df)


st.markdown('Widgets are in the sidebar')

container1 = st.container()
col1, col2 = st.columns(2)
with container1:
    with col1:
        figure
    with col2:
        figure1
container2 = st.container()
col3, col4 = st.columns(2)
with container2:
    with col3:
        figure2
    with col4:
        figure3

