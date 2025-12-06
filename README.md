🧠 PERSONAL ANALYZER DASHBOARD — PROJECT REPORT

1. Project Title
    Personal Analyzer Dashboard

2. Introduction
    This project is a complete personal data analytics system that tracks and visualizes:
    - Study hours
    - Sleep patterns
    - Daily expenses
    - Relationship between sleep and study hours
    The aim is to understand personal habits using data science and make improvements through insights.
    It is fully interactive and deployed live using Streamlit Cloud.

3. Objectives
    - Collect and organize personal data using a SQLite database.
    - Analyze study, sleep, and expense patterns using Python and Pandas.
    - Create visual insights using Matplotlib and Streamlit.
    - Understand trends and correlations in personal productivity.
    - Deploy the complete dashboard as a live website.

4. Features of the Dashboard

    📘 Study Analysis
    - Daily study hours visualization  
    - Total hours per subject  
    - Weekly study trends  
    - Subject-wise distribution  
    - Productivity insights  

    😴 Sleep Analysis
    - Daily sleep duration  
    - Sleep hour distribution  
    - Identify high/low sleep days  
    - Rest pattern analysis  

    💸 Expense Analysis
    - Category-wise spending  
    - Daily spending  
    - Filter by category  
    - Budget understanding  

    🔄 Sleep vs Study Relationship
    - Correlation calculation  
    - Scatter plot visualization  
    - Productivity linkage

5. Tech Stack Used
    - Frontend: Streamlit  
    - Backend/Data: Python, Pandas, Matplotlib  
    - Database: SQLite  
    - Deployment: Streamlit Cloud, GitHub  

6. Database Tables
    - study_hours (id, date, subject, hours, notes)  
    - sleep (id, date, sleep_hours, sleep_quality)  
    - expenses (id, date, category, amount, notes)

7. Project Folder Structure
    Personal-Analyzer/
    │ dashboard.py
    │ data.db
    │ requirements.txt
    │ README.md
    └─ .streamlit/
        config.toml

8. How It Works
    - The app loads data from SQLite database.
    - Data is cleaned, sorted, and analyzed using Python.
    - Visualizations are shown on multiple pages via Streamlit.
    - App is deployed live on Streamlit Cloud.

9. Live Demo Link
    - https://personal-analyzer.streamlit.app/

10. Purpose of the Project
    - Practice data analysis, dashboard development, SQL, deployment, and visualization.

11. Key Learnings
    - SQL & databases  
    - Python analytics  
    - Visualization skills  
    - GitHub workflow  
    - Deployment skills  

12. Future Enhancements
    - Add habits/workout tracking  
    - Add monthly reports  
    - Add interactive charts  
    - Add user input forms  
    - Add machine learning  

13. Author Details
    - Pratham Makhecha
    - GitHub: https://github.com/mpratham17