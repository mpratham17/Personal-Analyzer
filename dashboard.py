import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Personal Analyser Dashboard")

#connect to database 
conn=sqlite3.connect("data.db")
study=pd.read_sql_query("SELECT * FROM study_hours",conn)
sleep=pd.read_sql_query("SELECT * FROM sleep",conn)
expenses=pd.read_sql_query("SELECT * FROM expenses",conn)


# st.subheader("Study Hours Data")
# st.dataframe(study)

# st.subheader("Sleep Hours Data")
# st.dataframe(sleep)

# st.subheader("Expenses Data")
# st.dataframe(expenses)


#hours per subject
# st.subheader("Total Study Hours per Subject")
# hours_per_subject=study.groupby("subject")["hours"].sum()
# fig,ax=plt.subplots(figsize=(10,6))
# ax.bar(hours_per_subject.index,hours_per_subject.values)
# st.pyplot(fig)

def graphs_study():
    #bar: total hours per subject
    st.subheader("Total Study Hours per Subject")
    hours_per_subject=study.groupby("subject")["hours"].sum()
    fig,ax=plt.subplots(figsize=(10,6))
    ax.bar(hours_per_subject.index,hours_per_subject.values)
    ax.set_xlabel("Subject")
    ax.set_ylabel("Total Hours")
    ax.set_title("Total Study Hours per Subject")
    st.pyplot(fig)

    # line: hours per day
    st.subheader("Study Hours per Day")
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(study["date"], study["hours"],marker="o", linestyle="-",color="purple")
    ax.set_xlabel("Date")
    ax.set_ylabel("Hours Studied")
    ax.set_title("Study Hours per Day")
    ax.grid(True)
    st.pyplot(fig)

    # pie: subject-wise distribution
    st.subheader("Study hours distribution by subject")
    fig,ax=plt.subplots(figsize=(8,8))
    ax.pie(hours_per_subject.values, labels=hours_per_subject.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Study Hours Distribution by Subject")
    st.pyplot(fig)
    
def graphs_sleep():
    #line plot: sleep hours per day
    st.subheader("Sleep hours per day")
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(sleep["date"],sleep["sleep_hours"],marker="o",linestyle="--", color="darkblue")
    ax.set_title("Sleep Hours per Day")
    ax.set_xlabel("Date")
    ax.set_ylabel("Hours Slept")
    ax.grid(True)
    st.pyplot(fig)

    #histogram: distribution of sleep hours
    st.subheader("Distribution of Sleep Hours")
    fig,ax=plt.subplots(figsize=(10,6))
    ax.hist(sleep["sleep_hours"], bins=range(0,13), color="skyblue", edgecolor="black", alpha=0.7)
    st.pyplot(fig)

def graphs_expenses():
    #pie chart: category-wise distribution
    st.subheader("Expenses Distribution")
    per_category=expenses.groupby("category")["amount"].sum().sort_values()
    fig,ax=plt.subplots(figsize=(8,8))
    ax.pie(per_category.values, labels=per_category.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Expenses Distribution by Category")
    st.pyplot(fig)

def graph_study_vs_sleep():
    merge=pd.merge(sleep,study,on="date",how="inner")
    coorelation=merge["hours"].corr(merge["sleep_hours"])
    st.subheader("Correlation between Study Hours and Sleep Hours:[{:.2f}]".format(coorelation))
    #scatter plot: sleep hours vs study hours
    fig,ax=plt.subplots(figsize=(10,6))
    ax.scatter(merge["sleep_hours"], merge["hours"])
    ax.set_xlabel("Sleep Hours")
    ax.set_ylabel("Study Hours")
    ax.set_title("Sleep vs Study Hours")
    st.pyplot(fig)


#side bar
page=st.sidebar.selectbox("Select Page",["Study Analysis","Sleep Analysis","Expense Analysis","Sleep vs Study"])
if page=="Study Analysis":
    st.title("Study Analysis")
    # subject_filter = st.selectbox("Select subject", study["subject"].unique())
    # filtered = study[study["subject"] == subject_filter]
    # st.dataframe(filtered)
    graphs_study()
    #st.dataframe(study)  
elif page=="Sleep Analysis":
    st.title("Sleep Analysis")
    graphs_sleep()
    #st.dataframe(sleep)
elif page=="Expense Analysis":
    st.title("Expense Analysis")
    expense_filter=st.selectbox("Select Category",expenses["category"].unique())
    filtered=expenses[expenses["category"]==expense_filter]
    st.dataframe(filtered)
    graphs_expenses()

    #st.dataframe(expenses)
elif page=="Sleep vs Study":

    graph_study_vs_sleep()
