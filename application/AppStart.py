import os
import DbInitializer

initializer = DbInitializer
environment = os.getenv("ENV")

print(f"Starting app in {environment} mode.")
if environment == 'development':
    initializer.initialize_db()


print(f"Printing short db statistics.")
initializer.print_db_statistics()

