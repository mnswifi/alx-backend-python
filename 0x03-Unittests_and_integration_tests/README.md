# 0x03. Unittests and Integration Tests

This project focuses on writing **unittests** and **integration tests** in Python.  
You will learn how to isolate logic using mocks, parameterize tests, and perform integration testing with fixtures to simulate real-world API responses.

The goal is to practice **Test-Driven Development (TDD)** principles while ensuring code reliability and maintainability.

---

## 📂 Project Structure

```bash
0x03-Unittests_and_integration_tests/
├── client.py # Contains the GithubOrgClient class
├── utils.py # Utility functions with unit tests
├── fixtures.py # Predefined payloads for integration testing
├── test_client.py # Unit and integration tests for client.py
├── test_utils.py # Unit tests for utils.py
└── README.md # Project documentation
```

---

## 🛠️ Requirements

- All files are interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3.7**
- The first line of all Python files must be:

  ```python
  #!/usr/bin/env python3

- All files must:

  - End with a new line
  - Be executable
  - Respect pycodestyle (version 2.5)

- Documentation:
     - All modules, classes, and functions must have a complete docstring

    - A documentation is a real sentence explaining the purpose of the component

- Type annotations are mandatory for all functions and coroutines

- A README.md file is mandatory at the root of the project

## 📦 Installation
Clone the repository and navigate into the project directory:

```bash
git clone <repo-link>
cd 0x03-Unittests_and_integration_tests
```

Create a virtual environment (optional but recommended):
```bash

python3 -m venv venv
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Note: The project mainly uses unittest and parameterized, both of which will be installed via the requirements.txt.

## 🚀 Usage

Run any script directly since all files are executable:

```bash
./client.py
./utils.py
```

Or run with Python explicitly:

```bash
python3 client.py
```

## 🧪 Running Tests

Run all tests with:

```bash
python3 -m unittest discover -v
```

Run a specific test file:

```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```

## ✅ Example

Example running the integration tests:

```bash

$ python3 -m unittest test_client.py
test_public_repos (test_client.TestIntegrationGithubOrgClient) ... ok
test_public_repos_with_license (test_client.TestIntegrationGithubOrgClient) ... ok
```