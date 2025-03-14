# Database, API, and ML Integration Assignment

## Objective

This project focuses on designing and implementing a relational (SQL) and NoSQL (MongoDB) database, developing API endpoints using FastAPI, and creating a script to fetch and prepare data for machine learning predictions.

---

## Task 1: Database Creation in SQL and MongoDB

### Database Schema

We designed a relational database using **PostgreSQL** with the following tables:

- **Users** (user\_id, name, email, created\_at)
- **Transactions** (transaction\_id, user\_id, amount, transaction\_date)
- **Products** (product\_id, name, category, price)

Primary and foreign keys were defined to ensure data integrity. The ERD Diagram was created using **Lucidchart**.

### MongoDB Implementation

A **MongoDB** collection was implemented to store unstructured data related to user activity logs.

### Stored Procedures & Triggers

- **Stored Procedure:** Automatically updates user transaction history upon a new transaction.
- **Trigger:** Logs changes whenever a user updates their email.

---

## Task 2: API Endpoints for CRUD Operations

### Technology Stack:

- **FastAPI** for API development.

### Endpoints:

- **Create (POST):** Add new users, transactions, or products.
- **Read (GET):** Retrieve data from the database.
- **Update (PUT):** Modify existing records.
- **Delete (DELETE):** Remove records from the database.

These operations interact with the PostgreSQL database via an ORM.

---

## Task 3: Data Fetching & ML Prediction

### Steps:

1. **Fetch Latest Entry:** The script retrieves the most recent transaction record using the API.
2. **Prepare Data for Prediction:** The retrieved data is preprocessed.
3. **ML Model Integration:**
   - We used a **Linear Regression Model** trained during our Intro to ML course.
   - The model predicts potential future transactions.

---

## Contributors

&#x20;

- **Kevin Kenny Mugisha**  - Database Design & SQL Implementation
- **Bernice Awinpang Akudbilla** – API Development & MongoDB Implementation
- **Steven SHYAKA** – Data Fetching & ML Prediction

---

## How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/KennyKvn001/Database_Design.git
   cd Database_Design
   ```
2. **Set Up PostgreSQL & MongoDB:**
   - Import the SQL schema.
   - Run MongoDB collections.
3. **Start FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```
4. **Run the Prediction Script:**
   ```bash
   main.py
   ```

---

This project follows best practices for database management, API integration, and machine learning model implementation.
