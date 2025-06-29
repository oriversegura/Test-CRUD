    import os
    from dotenv import load_dotenv
    from sqlalchemy import create_engine

    # Load environment variables from .env file
    load_dotenv()

    # Get database connection details from environment variables
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Construct the MariaDB connection string
    # Use 'mariadb+mariadbconnector' for the official MariaDB Connector/Python
    database_url = f"mariadb+mariadbconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    # Create the SQLAlchemy engine
    engine = create_engine(database_url, echo=True) # echo=True for logging SQL statements
