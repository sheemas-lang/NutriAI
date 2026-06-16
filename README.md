# 🌿 NutriAI — AI-Based Nutrition Recommendation System

A fully offline, rule-based nutrition recommendation system built with **Python** and **Streamlit**. No API key, no internet connection required after installation.

## Features

- Personalised daily calorie & macro-nutrient targets (BMR via Mifflin-St Jeor equation, activity-adjusted TDEE)
- Supports 8 health goals: Weight Loss, Muscle Gain, Maintain Weight, Improve Energy, Better Gut Health, Heart Health, Manage Diabetes, Athletic Performance
- 9 dietary styles (Vegetarian, Vegan, Keto, Mediterranean, etc.) with automatic food substitution
- Allergy filtering across 9 categories
- Health condition–aware recommendations (Type 2 Diabetes, Hypertension, PCOS, and more)
- Health Score (0–100) and BMI analysis with visual gauge
- Daily 6-meal plan with timings and descriptions
- Aesthetic dark-themed dashboard built with custom CSS

## Tech Stack

- **Language:** Python 3.9+
- **UI Framework:** Streamlit
- **Logic:** Rule-based engine (`nutrition_engine.py`) — no ML model, no external API

## Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/NutriAI.git
cd NutriAI

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

## Project Structure

```
NutriAI/
├── app.py                 # Streamlit UI
├── nutrition_engine.py    # Core rule-based computation engine
├── requirements.txt       # Python dependencies
└── README.md
```

## How It Works

1. User enters age, weight, height, gender, activity level, health goal, diet type, allergies, and health conditions via the sidebar
2. `nutrition_engine.py` computes BMR (Mifflin-St Jeor), TDEE, goal-adjusted calorie target, and macro-nutrient split
3. A personalised 6-meal daily plan, food recommendations, key nutrients, hydration tip, and weekly habit are generated
4. Results render in a dashboard with a health score ring, BMI gauge, and colour-coded macro cards

## License

This project was developed as part of academic coursework (Biology for Information Technology, BBOC407) at BMSIT&M.
