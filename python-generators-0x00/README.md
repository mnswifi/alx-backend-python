# Python Generators – SQL Streaming

## Objective

This project demonstrates how to:
- Set up a MySQL database (`ALX_prodev`) with a table `user_data`.
- Seed the database with sample data from a CSV file.
- Use a Python **generator** to stream rows from the database **one by one** instead of fetching all at once.

---

## Project Structure

```bash
python-generators-0x00/
│── 0-main.py # Test script (provided)
│── seed.py # Handles DB setup, CSV loading, and row streaming
│── user_data.csv # Sample CSV file with user data
│── README.md # Project documentation
```

---

## Requirements

- Python 3.7+
- MySQL server installed and running locally
- Python library:

  ```bash
  pip install mysql-connector-python
  ```

---

## Database Setup

- Database name: `ALX_prodev`
- Table name: `user_data`
- Fields:
  - `user_id` – UUID (Primary Key, Indexed)
  - `name` – VARCHAR, not null
  - `email` – VARCHAR, not null
  - `age` – DECIMAL, not null

---

## Usage

### 1. Prepare the CSV file

Create a user_data.csv with the following format:

```csv
name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
Bob Johnson,bob@example.com,40
```

### 2. Update MySQL credentials

  In seed.py, set your MySQL username and password:

```python
user="root",
password="your_password"
```

### 3. Run the test script

```bash
python3 0-main.py
./0-main.py
```

### Example output:

```text
connection successful
Table user_data created successfully
Data inserted successfully from CSV
Database ALX_prodev is present 
[('uuid1', 'John Doe', 'john@example.com', 30), ...]
```

---
