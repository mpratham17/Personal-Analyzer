
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# connect to database
# conn=sqlite3.connect("data.db")
conn = sqlite3.connect("data.db")

study = pd.read_sql_query("SELECT * FROM study_hours", conn)
sleep = pd.read_sql_query("SELECT * FROM sleep", conn)
expenses = pd.read_sql_query("SELECT * FROM expenses", conn)


# st.subheader("Study Hours Data")
# st.dataframe(study)

# st.subheader("Sleep Hours Data")
# st.dataframe(sleep)

# st.subheader("Expenses Data")
# st.dataframe(expenses)


# hours per subject
# st.subheader("Total Study Hours per Subject")
# hours_per_subject=study.groupby("subject")["hours"].sum()
# fig,ax=plt.subplots(figsize=(10,6))
# ax.bar(hours_per_subject.index,hours_per_subject.values)
# st.pyplot(fig)


def home():
    st.title("Personal Analyser Dashboard")
    st.markdown(
        """
    ## 📊**What This Dashboard Shows**
    ### This dashboard analyzes my personal study hours, sleep patterns, and expenses over time.
    #### It helps visualize:
    - How much I study each day and each subject  
    - My sleep consistency  
    - Where I spend most of my money  
    - Relationship between sleep and study productivity  
    """
    )
    st.markdown("<hr/>", unsafe_allow_html=True)


def graphs_study():
    st.title("Study Analysis Graphs")
    st.metric("**Total Study Hours:**", round(study["hours"].sum(), 2))
    st.metric("**Most Studied Subject:**", study.groupby("subject")["hours"].sum().idxmax())

    st.markdown("<hr/>", unsafe_allow_html=True)
    
    # bar: total hours per subject
    st.subheader("Total Study Hours per Subject")
    hours_per_subject = study.groupby("subject")["hours"].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(hours_per_subject.index, hours_per_subject.values)
    ax.set_xlabel("Subject")
    ax.set_ylabel("Total Hours")
    ax.set_title("Total Study Hours per Subject")
    st.pyplot(fig)
    st.caption("This chart shows how much time I spent on each subject overall. It helps identify which subjects I focus on the most.")

    st.markdown("<hr/>", unsafe_allow_html=True)
    # line: hours per day
    st.subheader("Daily Study Hours – Shows how consistently I studied this month")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(study["date"], study["hours"], marker="o", linestyle="-", color="purple")
    ax.set_xlabel("Date")
    ax.set_ylabel("Hours Studied")
    ax.set_title("Study Hours per Day")
    ax.grid(True)
    plt.xticks(rotation=90)
    st.pyplot(fig)
    st.caption("This chart helps identify patterns and consistency.")

    st.markdown("<hr/>", unsafe_allow_html=True)

    # pie: subject-wise distribution
    st.subheader("📊 Study Time Distribution Across Subjects")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        hours_per_subject.values,
        labels=hours_per_subject.index,
        autopct="%1.1f%%",
        startangle=140,
    )
    ax.set_title("Study Hours Distribution by Subject")
    st.pyplot(fig)
    st.caption("This pie chart represents the percentage of total study hours each subject contributes. Useful for balancing study schedules.")


def graphs_sleep():
    st.title("Sleep Analysis Graphs")
    st.metric("**Average Sleep Hours:**", round(sleep["sleep_hours"].mean(), 2))
    st.metric("**Best Sleep Day:**", sleep.loc[sleep["sleep_hours"].idxmax()]["date"])

    st.markdown("<hr/>", unsafe_allow_html=True)
    # line plot: sleep hours per day
    st.subheader("😴 Daily Sleep Duration")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        sleep["date"],
        sleep["sleep_hours"],
        marker="o",
        linestyle="--",
        color="darkblue",
    )
    ax.set_title("Sleep Hours per Day")
    ax.set_xlabel("Date")
    ax.set_ylabel("Hours Slept")
    ax.grid(True)
    plt.xticks(rotation=90)
    st.pyplot(fig)
    st.caption("Shows how many hours I slept each day. Helps identify patterns like oversleeping or days with insufficient rest.")
    st.markdown("<hr/>", unsafe_allow_html=True)

    # histogram: distribution of sleep hours
    st.subheader("🛌 Sleep Hours Distribution")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        sleep["sleep_hours"],
        bins=range(0, 13),
        color="skyblue",
        edgecolor="black",
        alpha=0.7,
    )
    st.pyplot(fig)
    st.caption("This histogram shows how often I sleep specific amounts of time. Helps measure consistency and sleeping habits.")



def graphs_expenses():
    st.title("Expense Analysis Graphs")
    st.metric("**Total Expenses:**", round(expenses["amount"].sum(),2))
    st.metric("**Highest Spending Category:**", expenses.groupby("category")["amount"].sum().idxmax())

    st.markdown("<hr/>", unsafe_allow_html=True)

    # pie chart: category-wise distribution
    st.subheader("💸 Expense Distribution by Category")
    per_category = expenses.groupby("category")["amount"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        per_category.values,
        labels=per_category.index,
        autopct="%1.1f%%",
        startangle=140,
    )
    ax.set_title("Expenses Distribution by Category")
    st.pyplot(fig)
    st.caption("This chart shows where most of my spending happens. Useful for budgeting and identifying unnecessary expenses.")



def graph_study_vs_sleep():
    st.title("Study Hours vs Sleep Hours Analysis")
    merge = pd.merge(sleep, study, on="date", how="inner")
    coorelation = merge["hours"].corr(merge["sleep_hours"])
    st.subheader(
        " 🔄 Relationship Between Sleep and Study Hours:[{:.2f}]".format(coorelation)
    )
    # scatter plot: sleep hours vs study hours
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(merge["sleep_hours"], merge["hours"])
    ax.set_xlabel("Sleep Hours")
    ax.set_ylabel("Study Hours")
    ax.set_title("Sleep vs Study Hours")
    st.pyplot(fig)
    st.caption("This scatter plot shows how sleep duration relates to study performance. Helps understand whether more sleep improves productivity.")



# side bar
page = st.sidebar.selectbox(
    "Select Page",
    [
        "Home",
        "Study Analysis",
        "Sleep Analysis",
        "Expense Analysis",
        "Sleep vs Study",
    ],
)
if page == "Study Analysis":
    with st.expander("Show Raw Data"):
        st.dataframe(study)

    # st.title("Study Analysis")
    # subject_filter = st.selectbox("Select subject", study["subject"].unique())
    # filtered = study[study["subject"] == subject_filter]
    # st.dataframe(filtered)
    graphs_study()
    # st.dataframe(study)
elif page == "Sleep Analysis":
    with st.expander("Show Raw Data"):
        st.dataframe(sleep)
    # st.title("Sleep Analysis")
    graphs_sleep()
    # st.dataframe(sleep)
elif page == "Expense Analysis":
    with st.expander("Show Raw Data"):
        st.dataframe(expenses)
    st.title("Expense Analysis")
    expense_filter = st.selectbox("Select Category", expenses["category"].unique())
    filtered = expenses[expenses["category"] == expense_filter]
    st.dataframe(filtered)
    graphs_expenses()

    # st.dataframe(expenses)

elif page == "Sleep vs Study":
    with st.expander("Show Raw Data"):
        merge = pd.merge(sleep, study, on="date", how="inner")
        st.dataframe(merge)
    graph_study_vs_sleep()

elif page == "Home": 
    home()
