# Word Combinator - FastAPI Web Project

This project is a web application built with **FastAPI** and a basic web page interface. The purpose of the application is to allow users to create all possible word combinations based on a set of characters, with several customization options, such as filtering characters or allowing certain characters to be unbound (i.e., appear anywhere in the word).

## Features
- **Character Input**: Users can input a set of characters that will be used to generate all possible word combinations.
- **Empty Input Handling**: The application allows for empty character inputs and will handle them gracefully in the combination process.
- **Optional Inputs**:
  - **Excluded Characters**: Users can specify characters they want to exclude from the generated word combinations.
  - **Unbound Characters**: Users can input characters that can appear anywhere in the word without a fixed position in the combination.

---

## Prerequisites

- Python 3.11 or higher
- FastAPI
- Uvicorn (for running the FastAPI application)

---

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/word-combinator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd word-combinator
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Windows: env\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the web interface by visiting `http://127.0.0.1:8000` in your browser.

---

## Web Interface

The web page allows for the following inputs:

- **Character Set**: A text input field for entering the characters that should be used to generate word combinations. This is the main required input.
  
- **Excluded Characters**: (Optional) A field to specify any characters you want to exclude from the resulting combinations. For example, if you do not want words that contain the letter "a", you can input "a" in this field.

- **Unbound Characters**: (Optional) A field to add characters that can be placed anywhere in the generated words. These characters are not bound by the positional constraints of the main character set and will appear freely in any position within the word.

Once the inputs are provided, the user can submit the form, and all possible word combinations will be displayed.

---

## API Endpoints

- **`POST /generate-combinations`**
    - Request Body:
      ```json
      {
        "characters": "abc",
        "excluded_characters": "d",
        "unbound_characters": "e"
      }
      ```
    - Response:
      ```json
      {
        "combinations": ["abe", "bae", "eab", ...]
      }
      ```

---