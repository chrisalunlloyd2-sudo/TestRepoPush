import os
import sys
from utils import *
from models import *

def main():
    # Initialize database
    db = Database()

    # Load data models
    models = load_models()

    # Run application
    run_application(models, db)

if __name__ == "__main__":
    main()
