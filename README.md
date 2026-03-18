# Apex-F1: Formula 1 AI Hub

Apex-F1 is a Django-based web application providing a platform for Formula 1 fans to explore team and driver statistics, predict race winners, rate their favorite drivers, and take interactive, AI-powered quizzes.

## 🚀 Key Features

*   **Driver & Team Stats:** A comprehensive list of Formula 1 drivers and teams with detailed performance statistics.
*   **Race Schedule:** View the 2026 race calendar with track details.
*   **AI-Powered Quiz:** Generate custom F1 trivia quizzes on any topic using Google's Gemini AI. The quiz is interactive, featuring real-time grading and feedback.
*   **Winner Predictions:** Registered users can predict the winner for each race on the calendar.
*   **Driver Ratings:** A weighted rating system where fans can rate driver performances.
*   **User Profiles:** Core authentication system for tracking individual fan predictions and ratings.

## 🛠️ Tech Stack

*   **Framework:** Django (Python-based web framework)
*   **AI Engine:** Google Gemini AI (via `google-genai` SDK)
*   **Database:** SQLite (local development and Vercel-hosted read-only)
*   **Styling:** Vanilla CSS with a minimalist, premium "F1 Red & Black" aesthetic.
*   **Deployment:** Vercel (using a custom WSGI wrapper)

## 📁 Project Architecture

### 1. **Models (`myapp/models.py`)**
*   `Team`: Stores F1 constructor data (Principal, Engine Supplier).
*   `Driver`: Records individual driver stats and team affiliations.
*   `Track`: Contains details for each race venue (Length, Laps, Race Date).
*   `Rating`: Manages user-submitted driver ratings (1-10 scores).
*   `Prediction`: Stores fan predictions for future race winners.

### 2. **AI Quiz Logic (`myapp/views.py` & `quiz.html`)**
*   **Generation:** Uses `gemini-2.0-flash` to generate a structured 3-question quiz in JSON format based on a user-provided topic.
*   **Interactivity:** A JavaScript-powered frontend parses the AI response, manages the radio button selection, and calculates the total score upon submission without reloading the page.

### 3. **Deployment Strategy (`vercel.json` & `api/index.py`)**
*   As Vercel has a read-only filesystem, the application is configured to include the `db.sqlite3` directly in the deployment package.
*   A custom entry point (`api/index.py`) handles the WSGI interface for Vercel's Python runtime.

## 📥 Local Installation

1.  **Clone the Repo:**
    ```bash
    git clone https://github.com/Akshaikumar-N/Apex-F1.git
    cd Apex-F1
    ```

2.  **Setup Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    # venv\Scripts\activate   # Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python mywebsite/manage.py migrate
    ```

5.  **Start Development Server:**
    ```bash
    python mywebsite/manage.py runserver
    ```

## 📜 Configuration

The following environment variables are required for full functionality:
*   `GEMINI_API_KEY`: Your Google GenAI API key for the quiz feature.
*   `SECRET_KEY`: Django's security key.
*   `DEBUG`: Set to `True` for development, `False` for production.
