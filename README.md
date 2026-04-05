# Looqbox Data Challenge

This repository contains the solutions for the **Looqbox Data Challenge** using **Python** and **MySQL**.

The project connects to the provided MySQL database and solves the proposed SQL queries and Python cases, including data extraction, transformation, and visualization.

---

# Project Structure

```
.
├── cases/
│   ├── case_1.py
│   ├── case_2.py
│   └── case_3.ipynb
├── sql_test/
│   ├── queries/
│       ├── query_1.sql
│       ├── query_2.sql
│       └── query_3.sql
│   ├── question_1.ipynb
│   ├── question_2.ipynb
│   └── question_3.ipynb
├── requirements.txt
├── .env
└── README.md
```

- **case_1.py** → Dynamic query function to retrieve product sales data  
- **case_2.py** → Data transformation and visualization for store sales  
- **case_3.py** → Custom visualization using the `IMDB_movies` table  

---

# Requirements

- Python **3.9+**
- MySQL access credentials (provided by Looqbox)
- Python dependencies listed in `requirements.txt`

---

# Environment Setup


Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root of the project with the database credentials:

```env
DB_IP=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_SCHEMA=your_schema
DB_NAME=looqbox_challenge
DB_PORT=3306
```

These variables are used to establish the connection with the MySQL database.

---

# Running the Project

Each case can be executed individually.

### Case 1 – Dynamic Query Function

Run:

```bash
python cases/case_1.py
```

### Case 2 – Store Sales Visualization

Run:
```bash
python cases/case_2.py
```

### Case 3 and sql_tests 

Run the notebook files to reproduce the analysis and visualizations.

```bash
jupyter notebook