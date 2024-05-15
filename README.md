# System Control App

## Overview

This Python application provides functionalities to control system operations like shutdown, restart, scheduling a restart, and logging out. It is designed to work on Windows, macOS, and Linux.

## Features

- **Shutdown**: Turn off the system.
- **Restart**: Restart the system.
- **Schedule Restart**: Schedule a system restart after a specified time.
- **Logout**: Log out the current user operation.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/system-control-app.git
    cd system-control-app
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script to access the features:

```bash
python main.py
