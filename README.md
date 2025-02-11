# Python Exam Fall 2024 - ICTU

Welcome to the Python Exam Fall 2024 project repository for ICTU. This repository contains all the necessary materials and instructions for the Python exam.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [ChatMateServerApp](#chatmateserverapp)

## Introduction

This project is designed to help students prepare for the Python exam in Fall 2024. It includes sample questions, practice exercises, and reference materials.

## Project Structure

The repository is organized as follows:

```
python-exam-fall2024-ictu/
│
├── src/
│   ├── maths/
│   └── solutions/
│
├── tests/
│
├── docs/
│
├── chat-mate/
│   └── ChatMateServerApp/
│
└── README.md
```

- `src/`: Contains the source code for exercises and solutions.
- `tests/`: Contains test cases for the exercises.
- `docs/`: Contains documentation and reference materials.
- `chat-mate/ChatMateServerApp/`: Contains the Blazor Server App project that uses a SQLite database.

## Installation

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/rodern/python-exam-fall2024-ictu.git
cd python-exam-fall2024-ictu
```

## Usage

Navigate to the `src/` directory to find the exercises and solutions. You can run the exercises using Python:

```bash
python src/maths/exercise1.py
```

## Contributing

We welcome contributions from the community. If you would like to contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## ChatMateServerApp

The `ChatMateServerApp` is a Blazor Server App included in this repository. It uses a SQLite database and provides various services.

### Project Structure

The `ChatMateServerApp` is organized as follows:

```
chat-mate/ChatMateServerApp/
│
├── Data/
├── DbModels/
├── DbServices/
├── Pages/
├── Program.cs
├── appsettings.json
└── Startup.cs
```

- `Data/`: Contains data services and context.
- `DbModels/`: Contains database models.
- `DbServices/`: Contains database service interfaces and implementations.
- `Pages/`: Contains Blazor pages.
- `Program.cs`: Main entry point of the application.
- `appsettings.json`: Configuration file.
- `Startup.cs`: Configuration for services and middleware.

### Running the Application

To run the `ChatMateServerApp`, navigate to the project directory and use the following command:

```bash
dotnet run
```

The application will be available at `https://localhost:5001`.

### Database Configuration

The application uses a SQLite database. The connection string is configured in the `appsettings.json` file. Ensure you have the necessary SQLite tools installed to manage the database.
