# End-to-End Insurance Risk Analytics & Predictive Modeling (Task 1 & Task 2)

This repository contains the implementation of Tasks 1 and 2 for Week 3 of the End-to-End Insurance Risk Analytics project. The project demonstrates a systematic approach to Exploratory Data Analysis (EDA) and Data Version Control (DVC) for ensuring reproducibility and auditability in financial data workflows.

---

## Objective

- **Task 1:** Gain a foundational understanding of the insurance dataset, assess its quality, and uncover initial patterns in risk and profitability. Provide insights into factors like loss ratios, temporal trends, and claim patterns by vehicle type, province, and gender.
- **Task 2:** Establish a reproducible and auditable data pipeline using DVC to ensure data inputs are as rigorously version-controlled as code, enabling reproducibility for regulatory compliance and debugging.

---

## Workflow Overview

### Task 1: Exploratory Data Analysis (EDA)

The workflow is implemented in [`notebooks/eda.ipynb`](notebooks/eda.ipynb):

1. **Git and GitHub Setup**
   - Create a GitHub repository to host project code and data.
   - Add a detailed README.md, .gitignore, and requirements.txt.
   - Use branches for logical tasks (task-1, task-2).
   - Commit frequently with descriptive messages.
   - Use GitHub Actions for CI/CD to automate testing and deployment.

2. **Data Understanding and Preprocessing**
   - **Data Summarization:**  
     - Descriptive statistics for numerical features like TotalPremium, TotalClaims, and LossRatio.
     - Check column data types and confirm formatting.
   - **Data Quality Assessment:**  
     - Identify and handle missing values.
     - Check for duplicates and ensure data consistency.

3. **Exploratory Data Analysis (EDA)**
   - **Univariate Analysis:**  
     - Visualize distributions of numerical and categorical variables using histograms and bar charts.
   - **Bivariate Analysis:**  
     - Analyze relationships between variables (e.g., TotalClaims vs. TotalPremium) using scatter plots and correlation matrices.
   - **Temporal Trends:**  
     - Investigate claim frequencies and severities over time.
   - **Outlier Detection:**  
     - Use box plots to identify anomalies in numerical data.
   - **Visualization:**  
     - Produce 3 insightful and visually appealing plots to highlight key findings.

4. **Guiding Questions**
   - What is the overall Loss Ratio (TotalClaims / TotalPremium) for the portfolio? How does it vary by Province, VehicleType, and Gender?
   - Are there outliers in TotalClaims or CustomValueEstimate that could skew the analysis?
   - Did claim frequency or severity change over the 18-month period?
   - Which vehicle makes/models are associated with the highest and lowest claim amounts?

---

### Task 2: Data Version Control (DVC)

The workflow is implemented in [`notebooks/dvc_pipline.ipynb`](notebooks/dvc_pipline.ipynb):

1. **Install and Initialize DVC**
   - Install DVC:  
     `pip install dvc`
   - Initialize DVC in the project root:  
     `dvc init`

2. **Configure Local Remote Storage**
   - Create a storage directory:  
     `mkdir data/remote_storage`
   - Add the remote storage:  
     `dvc remote add -d localstorage data/remote_storage`

3. **Add and Track Data**
   - Place your datasets in the project directory and track them using DVC:  
     `dvc add data/raw/MachineLearningRating_v3.txt`
   - Commit the .dvc files and updates to your Git repository:  
     ```
     git add data/raw/MachineLearningRating_v3.txt.dvc data/raw/.gitignore
     git commit -m "Track dataset with DVC"
     ```
   - Push the tracked data to the configured remote storage:  
     `dvc push`

4. **Update Data Versions**
   - Modify or update the data as needed.
   - Use `dvc add` to track new versions, and commit changes to the repository.

---

## Project Structure

```
End-to-End Insurance Risk Analytics/
├── data/
│   ├── raw/              # Raw datasets
│   ├── processed/        # Processed datasets
│   └── remote_storage/   # DVC remote storage
├── notebooks/
│   ├── eda.ipynb         # EDA notebook
│   └── dvc_pipline.ipynb # DVC pipeline notebook
├── src/utils/
│   ├── eda.py            # EDA helper functions
│   └── dvc_setup.py      # DVC configuration scripts
├── .dvc/                 # DVC metadata
├── .gitignore
├── requirements.txt
├── README.md
└── .github/workflows/    # CI/CD configuration
```

---

## Key Performance Indicators (KPIs)

### Task 1 (EDA)
- Complete and reproducible EDA workflow.
- Insightful visualizations and statistical summaries.
- Evidence-based answers to guiding questions.

### Task 2 (DVC)
- Functional and well-documented DVC setup.
- Data tracked and pushed to remote storage.
- Git repository reflects structured and versioned workflow.

---

## References

- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [DVC Documentation](https://dvc.org/doc)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## Contact

For questions or collaboration, contact:  
matiasashenafi0@gmail.com