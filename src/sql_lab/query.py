import os
import logging
import pandas as pd
import mysql.connector

logging.basicConfig(level=logging.INFO)


def read_data(filename):
    """Read a CSV file and return it as a pandas DataFrame."""
    logging.info("Reading CSV data")
    data = pd.read_csv(filename)
    return data


def clean_data(data):
    """Remove rows containing missing values."""
    logging.info("Cleaning data")
    cleaned_data = data.dropna()
    return cleaned_data


def load_data(data, table):
    """Create the mock table and upload the cleaned DataFrame to MySQL."""
    if table != "mock":
        raise ValueError("This lab requires the table name to be 'mock'")

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database=os.getenv("DBNAME")
        )

        cursor = connection.cursor()

        # Create the destination table if it does not already exist.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mock (
                id BIGINT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255),
                gender VARCHAR(255),
                `group` VARCHAR(255)
            )
        """)

        # Clear existing rows so the script can safely be run again.
        cursor.execute("DELETE FROM mock")

        # Insert each cleaned row using a parameterized query.
        insert_query = """
            INSERT INTO mock
            (id, first_name, last_name, email, gender, `group`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for _, row in data.iterrows():
            cursor.execute(insert_query, tuple(row))

        connection.commit()
        logging.info("Data uploaded successfully")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)


def main():
    """Read, clean, and upload the mock dataset."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()
