# Class Manager Readme

This repository contains two Python classes, `ClassManagerMongo` and `ClassManager`, designed to manage a database of advisors and students. Each class interfaces with a different database management system, MongoDB and SQLite respectively.

## Prerequisites
- Python 3.x
- pymongo (for MongoDB interaction)
- sqlite3 (built-in, for SQLite interaction)

## Setup Instructions
1. Clone the repository to your local machine.
2. Ensure that Python 3.x is installed.
3. Install the required packages:
    ```bash
    pip install pymongo
    ```
4. Run the scripts.

## ClassManagerMongo
- This class interacts with a MongoDB database.
- Ensure MongoDB is running on localhost:27017.
- To use this class, create an instance of `ClassManagerMongo`, then call its methods to set up the database, count the number of students per advisor, and close the connection.

```python
from pymongo import MongoClient

# Example usage:
manager = ClassManagerMongo()
manager.setup_database()
count_table = manager.count_function()
for row in count_table:
    print(f"ID: {row['AdvisorID']}, Name: {row['AdvisorName']}, Number of Students: {row['StudentCount']}")
manager.close()
