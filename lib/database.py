# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from .models import Base

# # Set the database file path
# db_file_path = os.path.join(os.path.dirname(__file__), '..', 'Restaurantreservation.db')

# # Create the database engine
# engine = create_engine('sqlite:///restaurantreservation.db')

# # Create the database session
# Session = sessionmaker(bind=engine)

# # Create the tables
# def create_tables():
#     if not os.path.exists(db_file_path):
#         Base.metadata.create_all(engine)
#     else:
#         print("Database file already exists. Skipping table creation.")

# # Drop the tables
# def drop_tables():
#     Base.metadata.drop_all(engine)

# # Create a session
# def create_session():
#     return Session()
