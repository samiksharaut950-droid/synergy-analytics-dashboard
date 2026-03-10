import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SynergyAnalyticsDashboard:

    def __init__(self):
        self.data = None

    # -----------------------------
    # Page Configuration
    # -----------------------------
    def initialize_app(self):
        st.set_page_config(
            page_title="Corporate Synergy Dashboard",
            layout="wide"
        )
        st.title("📊 Corporate Synergy Analytics Dashboard")
        st.markdown("Upload Excel file to analyze collaboration and synergy performance.")

    # -----------------------------
    # File Upload
    # -----------------------------
    def upload_file(self):
        uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

        if uploaded_file:
            self.data = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")
            st.write("### Preview Data")
            st.dataframe(self.data.head())

    # -----------------------------
    # Basic Charts (40% Complete)
    # -----------------------------
    def basic_visualizations(self):
        if self.data is not None:

            st.subheader("1️⃣ Department Distribution")

            dept_counts = self.data["Department"].value_counts()

            fig1, ax1 = plt.subplots()
            ax1.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
            st.pyplot(fig1)

            # ------------------------

            st.subheader("2️⃣ Synergy Score Distribution")

            fig2, ax2 = plt.subplots()
            ax2.hist(self.data["Synergy_Score"], bins=20)
            st.pyplot(fig2)

            # ------------------------

            st.subheader("3️⃣ Average Productivity by Department")

            avg_productivity = self.data.groupby("Department")["Productivity_Score"].mean()

            fig3, ax3 = plt.subplots()
            avg_productivity.plot(kind='bar', ax=ax3)
            st.pyplot(fig3)

            # ------------------------

            st.subheader("4️⃣ Correlation Heatmap")

            numeric_cols = self.data.select_dtypes(include=['int64', 'float64'])
            corr = numeric_cols.corr()

            fig4, ax4 = plt.subplots(figsize=(8,5))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
            st.pyplot(fig4)

    # -----------------------------
    # Students Task Section (To Be Completed)
    # -----------------------------
    def student_tasks_placeholder(self):
        st.markdown("## 🚀 Students To Complete (60%)")

        st.markdown("""
        🔹 Add Sidebar Filters:
            - Filter by Department
            - Filter by Project
            - Filter by Collaboration Type

        🔹 Add KPI Cards:
            - Average Synergy Score
            - Success Rate %
            - Total Revenue Impact

        🔹 Create Advanced Charts:
            - Boxplot of Synergy vs Department
            - Scatter: Synergy vs Productivity
            - Revenue vs Project Duration

        🔹 Add Insight Section:
            - Auto-generate 3 business insights from data

        🔹 Add Download Filtered Data Option
        """)

    # -----------------------------
    # Run App
    # -----------------------------
    def run(self):
        self.initialize_app()
        self.upload_file()
        self.basic_visualizations()
        self.student_tasks_placeholder()


if __name__ == "__main__":
    app = SynergyAnalyticsDashboard()
    app.run()