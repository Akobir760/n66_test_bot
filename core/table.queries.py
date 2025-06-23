from core.db_settings import execute_query

users = """
CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMERY KEY,
full_name VRCHAR(89) NOT NULL,
phone_number VARCHAR(20) NOT NULL UNIQUE,
latitude VARCHAR(25) NOT NULL,
longitude VARCHAR(25) NOT NULL,
language CHAR(2) NOT NULL,
chat_id BIGINT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

def initializing_table():
    execute_query(query=users)