# streamlitOne

A simple Streamlit dashboard for exploring student performance data from a sample CSV file. This project demonstrates how to build a lightweight analytics app with filters, summary metrics, and visual charts in Python.

## Project overview

The app loads data from `data/sample_data.csv` and presents:

- a summary of student counts and average scores
- subject-wise performance metrics
- bar charts and a pie chart for subject distribution
- a searchable/filterable table of student records
- a leaderboard of the top-performing students

The dashboard is designed to help visualize trends in a dataset and practice building data insight interfaces with Streamlit.

## Features

- Subject filter in the sidebar
- Key KPI cards for student counts and score summaries
- Visual breakdowns by subject
- Student data table view
- Top 10 student leaderboard

## Project structure

```bash
streamlitOne/
├── main.py                  # Streamlit app entry point
├── data/
│   └── sample_data.csv      # Sample dataset used by the dashboard
├── README.md                # Project documentation
└── LICENSE                  # Project license
```

## Prerequisites

Make sure you have Python 3.9+ installed on your system.

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

1. Install the required dependencies:

```bash
pip install streamlit pandas altair
```

If you prefer to install everything from a requirements file, create one with:

```bash
pip freeze > requirements.txt
```

Then install with:

```bash
pip install -r requirements.txt
```

## Run the app

From the project root, start the Streamlit app with:

```bash
streamlit run main.py
```

This will launch the dashboard in your default browser. If it does not open automatically, copy the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Data source

The application reads data from `data/sample_data.csv`. You can replace this file with your own CSV data as long as it contains columns like `name`, `subject`, and `score`.

## Notes

- The app automatically converts the `score` column to numeric values.
- If your data uses different column names, update the relevant sections in `main.py`.

## License

This project is licensed under the terms included in the `LICENSE` file.
