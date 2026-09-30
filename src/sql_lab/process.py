import pandas as pd
import mysql.connector


def load_data():
    df = pd.read_csv("MOCK_DATA.csv")
    return df


def clean_data(df):
    df = df.dropna()
    return df


def connect_db():
    connection = mysql.connector.connect(
        host="ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com",
        user="ynr6uw",
        password="ynr6uw",
        database="ynr6uw_mock"
    )
    return connection


def create_table(connection):
    cursor = connection.cursor()

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

    connection.commit()
    cursor.close()


def insert_data(connection, df):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM mock")

    sql = """
        INSERT INTO mock
        (id, first_name, last_name, email, gender, `group`)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    data = load_data()
    clean = clean_data(data)

    connection = connect_db()
    create_table(connection)
    insert_data(connection, clean)
    connection.close()

    print("Data inserted successfully")
