
# ATBD-PR02

**ATBD-PR02** is a project for the Big Data subject from the Master's degree in Computing and Intelligent Systems. This repository focuses on implementing a NoSQL database solution for managing structured football player data using MongoDB, Python, and Docker.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Workflow](#data-workflow)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

---

## Overview

The ATBD-PR02 project simulates a real-world use case for managing and querying football player statistics using NoSQL databases. The primary goal is to evaluate MongoDB's flexibility, indexing capabilities, and performance for storing hierarchical data structures.

### Key Objectives:
1. Implement a MongoDB schema suitable for football player data, including statistics, personal information, and teams.
2. Automate data processing and insertion for up to 100 player records.
3. Perform advanced queries and analyze execution times to optimize the schema and database performance.
4. Provide a user-friendly pipeline for data ingestion, processing, and querying.

---

## Features

- **MongoDB Integration**: Uses MongoDB to store structured football data in JSON-like documents.
- **Data Transformation**: `transform.py` processes raw CSV data into a structured format for MongoDB.
- **Batch Insertions**: Efficiently inserts multiple records using `pymongo`.
- **Custom Query Execution**: `queries.py` implements and benchmarks advanced MongoDB queries.
- **Registry Modifications**: `modifyRegistries.py` automates record updates, such as changing player names to uppercase.
- **Docker Support**: Provides Dockerized setup for MongoDB to simplify deployment.
- **Performance Analysis**: Measures execution time for queries and operations to identify optimization opportunities.
- **Modular Code**: Organized scripts for modular execution and flexibility.

---

## Installation

### Prerequisites:
- Python 3.8 or later
- MongoDB installed locally or accessible remotely
- Docker (optional for containerized deployment)

### Steps to Install:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AsierBujedo/ATBD-PR02.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd ATBD-PR02
   ```

3. **Set Up a Python Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     SERVER=your_database_host
     PORT=your_database_port
     USR=your_database_user
     PWD=your_database_password
     ```

6. **Optional: Use Docker for MongoDB**:
   - Start the Docker container:
     ```bash
     docker-compose --profile mongo up
     ```

---

## Usage

### General Workflow

1. **Run the Main Script**:
   - This script processes and inserts data into MongoDB.
   ```bash
   python main.py
   ```

2. **Run Query Scripts**:
   - Execute specific queries and measure performance:
     ```bash
     python queries.py
     ```

3. **Modify Records**:
   - Update existing records in the database:
     ```bash
     python modifyRegistries.py
     ```

### Example Commands:

- **Data Transformation**:
  ```bash
  python transform.py
  ```

- **Insert Data into MongoDB**:
  ```bash
  python main.py
  ```

- **Modify Player Records**:
  ```bash
  python modifyRegistries.py
  ```

- **Query Data**:
  ```bash
  python queries.py
  ```

---

## Project Structure

```
ATBD-PR02/
├── data/
│   ├── raw/             # Raw input data (CSV files, etc.)
│   └── processed/       # Processed data for MongoDB
├── docker/              # Docker configuration files
├── results/             # Output results and logs
├── .env                 # Environment configuration
├── .gitignore           # Git ignore rules
├── big_data_e2.pdf      # Project documentation
├── main.py              # Main execution script
├── modifyRegistries.py  # Script for modifying registries
├── queries.py           # Script for executing queries
├── requirements.txt     # Python dependencies
├── transform.py         # Data transformation script
└── README.md            # Project README
```

---

## Data Workflow

1. **Data Preparation**:
   - Use `transform.py` to clean and organize raw player data from CSV files.

2. **Data Insertion**:
   - Insert 100 records into MongoDB using `main.py`. This step includes creating indices for optimal performance.

3. **Data Queries**:
   - Execute queries to filter players based on conditions like `EstimatedStartYear` or team names starting with "Manchester."

4. **Record Updates**:
   - Modify specific player data (e.g., update names to uppercase) with `modifyRegistries.py`.

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request to the main repository.

---

## Troubleshooting

- **Dependencies Not Installing**:
  - Ensure you're using the correct Python version (see `requirements.txt`).
  - Use a virtual environment for isolated dependency management.

- **Database Connectivity**:
  - Verify `.env` file contains correct MongoDB credentials.
  - Test the connection manually using a MongoDB client or tool like `mongo`.

- **Docker Issues**:
  - Check that Docker is installed and running on your machine.
  - Validate the `docker-compose.yml` file for correct configurations.

---

## Contact

For questions, feedback, or support, contact [Asier Bujedo](mailto:asier.bujedo@opendeusto.es) or open an issue on this repository.
