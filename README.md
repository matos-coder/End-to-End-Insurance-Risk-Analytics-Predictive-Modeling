End-to-End Insurance Risk Analytics & Predictive Modeling (Task 1 & Task 2)
This repository contains the implementation of Tasks 1 and 2 for Week 3 of the End-to-End Insurance Risk Analytics project. The project demonstrates a systematic approach to Exploratory Data Analysis (EDA) and Data Version Control (DVC) for ensuring reproducibility and auditability in financial data workflows.

Task 1: Exploratory Data Analysis (EDA)
Objective
Gain a foundational understanding of the dataset, assess its quality, and uncover initial patterns in risk and profitability. The goal is to provide insights into factors like loss ratios, temporal trends, and claim patterns by vehicle type, province, and gender.

Workflow Overview
1.1 Git and GitHub Setup
Repository Initialization:

Create a GitHub repository to host project code and data.

Add a detailed README.md, .gitignore, and requirements.txt.

Version Control:

Create branches for logical tasks (task-1, task-2).

Commit frequently with descriptive messages.

Use GitHub Actions for CI/CD to automate testing and deployment.

1.2 Data Understanding and Preprocessing
Data Summarization:

Descriptive statistics for numerical features like TotalPremium, TotalClaims, and LossRatio.

Check column data types and confirm formatting.

Data Quality Assessment:

Identify and handle missing values.

Check for duplicates and ensure data consistency.

Exploratory Data Analysis (EDA):

Univariate Analysis:

Visualize distributions of numerical and categorical variables using histograms and bar charts.

Bivariate Analysis:

Analyze relationships between variables (e.g., TotalClaims vs. TotalPremium) using scatter plots and correlation matrices.

Temporal Trends:

Investigate claim frequencies and severities over time.

Outlier Detection:

Use box plots to identify anomalies in numerical data.

Visualization:

Produce 3 insightful and visually appealing plots to highlight key findings.

Guiding Questions
What is the overall Loss Ratio (TotalClaims / TotalPremium) for the portfolio? How does it vary by Province, VehicleType, and Gender?

Are there outliers in TotalClaims or CustomValueEstimate that could skew the analysis?

Did claim frequency or severity change over the 18-month period?

Which vehicle makes/models are associated with the highest and lowest claim amounts?

Task 2: Data Version Control (DVC)
Objective
Establish a reproducible and auditable data pipeline using DVC to ensure data inputs are as rigorously version-controlled as code, enabling reproducibility for regulatory compliance and debugging.

Workflow Overview
2.1 Install and Initialize DVC
Install DVC:

bash
Copy
Edit
pip install dvc
Initialize DVC:

bash
Copy
Edit
dvc init
2.2 Configure Local Remote Storage
Create a Storage Directory:

bash
Copy
Edit
mkdir /path/to/your/local/storage
Add the Remote Storage:

bash
Copy
Edit
dvc remote add -d localstorage /path/to/your/local/storage
2.3 Add and Track Data
Add Your Data:
Place your datasets in the project directory and track them using DVC:

bash
Copy
Edit
dvc add data/raw/dataset.csv
Commit Changes to Git:
Commit the .dvc files and updates to your Git repository:

bash
Copy
Edit
git add data/raw/dataset.csv.dvc .gitignore
git commit -m "Track dataset with DVC"
Push Data to Remote:
Push the tracked data to the configured remote storage:

bash
Copy
Edit
dvc push
2.4 Update Data Versions
Modify or update the data as needed.

Use dvc add to track new versions, and commit changes to the repository.

Key Performance Indicators (KPIs)
Task 1 (EDA)
Complete and reproducible EDA workflow.

Insightful visualizations and statistical summaries.

Evidence-based answers to guiding questions.

Task 2 (DVC)
Functional and well-documented DVC setup.

Data tracked and pushed to remote storage.

Git repository reflects structured and versioned workflow.

Project Structure
bash
Copy
Edit
End-to-End Insurance Risk Analytics/
├── data/
│   ├── raw/              # Raw datasets
│   ├── processed/        # Processed datasets
├── notebooks/
│   ├── eda.ipynb         # EDA notebook
│   ├── dvc_setup.ipynb   # DVC setup notebook
├── src/utils
│   ├── eda.py            # EDA helper functions
│   ├── dvc_setup.py      # DVC configuration scripts
├── .dvc/                 # DVC metadata
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── README.md             # Project description
└── .github/workflows/    # CI/CD configuration
References
Pandas Documentation

Matplotlib Documentation

DVC Documentation

GitHub Actions

Contact
For questions or collaboration, contact: matiasashenafi0@gmail.com