# FAST-API

Simple project with endpoints

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Issues](#issues)
- [Code Breakdown](#code-breakdown)
    - [Database](#database)
    - [Models](#models)
    - [Main](#main)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Getting Started

I try to explain every line of code to the best of my understanding. Hope it helps you out.

### Prerequisites

- Python 3.x (Recommended: Python 3.8 or later)
- pip (Python package manager)

### Installation

1. Create a directory/folder

2. Navigate to the folder
- On linux/macOs
```bash
cd [folder_name]
```
- On windows
```powershell
cd [folder_name]
```

3. create a virtual environment
- On macOs/linux
```bash
python3 -m venv venv
```
- On Windows
```powershell
python -m venv venv
```
4. Activate the virtual environment
- On macOs/linux
```bash
source venv/bin/activate
```
- On Windows
```powershell
venv\Scripts\Activate
```
5. Install some dependencies
```bash or powershell
pip install uvicorn sqlalchemy
```

### Issues

Any issues arising with installation. Visit 
https://github.com/Fourteen98/RegNow.git to resolve the issue.

## Code Breakdown

Simplified explanation

### Database

This acts as the connector between the sqlite database application and the FastApi

--Importing classes abd functions from SQLAlchemcy librabry

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

--Pathway to database

URL_DATABASE = 'sqlite:///./student_portal.db'

--Create database engine and also allow multithreading

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

--Create objects for database interaction

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

--Creating a base class that can be inherited.

Base = declarative_base()

### Models

This acts as the table for the sqlite application

### Main

This act as the main entry point of where every comes together

## API Documentation
The API documentation is automatically generated using Swagger UI. You can access the documentation by visiting http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc after starting the development server.

## Contributing
Contributions are welcome! If you have any bug fixes, improvements, or new features, please open an issue or a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Authors
👤 Napaa Samuel
GitHub: @Thenebit