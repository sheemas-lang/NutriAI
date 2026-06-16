# 🌿 NutriAI

> A lightweight, **offline-first** nutrition recommendation system — no API key, no internet required after install, no sign-up friction.

Built as a course mini-project for **Biology for Information Technology (BBOC407)** at **BMSIT&M**, Bengaluru (2025–26).

---

## ✨ Features

| Feature | Details |
|---|---|
| 🧮 **BMR / TDEE Engine** | Mifflin-St Jeor equation + activity-adjusted Total Daily Energy Expenditure |
| 🎯 **8 Health Goals** | Weight Loss, Muscle Gain, Maintain Weight, Improve Energy, Better Gut Health, Heart Health, Manage Diabetes, Athletic Performance |
| 🥗 **9 Dietary Styles** | Vegetarian, Vegan, Keto, Mediterranean, Gluten-Free, and more — with automatic food substitution |
| 🚫 **Allergy Filtering** | Excludes flagged ingredients across 9 allergy categories |
| 🩺 **Health Condition Aware** | Adjusts plans for Type 2 Diabetes, Hypertension, PCOS, Thyroid Disorder, and 6 more conditions |
| 🍽️ **Daily Meal Plan** | 6 meals with timings, descriptions, and nutrient rationale |
| 📊 **Health Score & BMI** | 0–100 score + visual BMI gauge with category breakdown |
| 🎨 **Aesthetic Dashboard** | Dark-themed Streamlit UI with colour-coded macro cards and SVG health ring |
| 🔒 **100% Private** | Fully offline — no external API calls, no data leaves your machine |

---

## 📁 Project Structure

```
NutriAI/
├── app.py                  # Streamlit UI — sidebar inputs + results dashboard
├── nutrition_engine.py     # Core rule-based engine: BMR, TDEE, macros, meal plans
├── requirements.txt        # Python dependencies (just Streamlit)
└── README.md
```

---

## 🚀 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/sheemas-lang/NutriAI.git
cd NutriAI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| UI Framework | Streamlit |
| Logic | Rule-based engine — no ML model, no external API |
| Styling | Custom CSS injected into Streamlit (dark botanical theme) |

---

## 🧬 Algorithms

| Algorithm | Formula |
|---|---|
| **BMR (Male)** | `10 × weight + 6.25 × height − 5 × age + 5` |
| **BMR (Female)** | `10 × weight + 6.25 × height − 5 × age − 161` |
| **TDEE** | `BMR × Activity Multiplier (1.2 – 1.9)` |
| **Calorie Target** | `TDEE ± Goal-specific offset` (e.g. −400 kcal for Weight Loss) |
| **Health Score** | `Base 60 + BMI bonus + Activity bonus − Condition penalties` (capped 10–97) |

---

## 👥 Team

| Name | USN |
|---|---|
| Chaitra Shree Y S | 1BY24CS054 |
| Srujan S Rao | 1BY24CS286 |
| Thejaswini V Bhat | 1TD24CS319 |
| Sheema Sadiyah Tadipatri | 1TE24CS266 |

**Faculty Guide:** Prof. Indrakumar D R, Assistant Professor, Dept. of CSE, BMSIT&M
**Course:** Biology for Information Technology — BBOC407

---

## 🌍 SDG Alignment

| Target | Description |
|---|---|
| **3.4** | Reduce premature mortality from non-communicable diseases |
| **3.8** | Universal health coverage and access to nutrition information |
| **3.d** | Strengthen capacity for health risk reduction and management |

---

## ⚠️ Disclaimer

Nutritional values and recommendations are generated using general clinical formulae for **educational purposes only**. This application is **not a substitute for professional dietary or medical advice**. Please consult a registered dietitian or physician before making significant dietary changes, especially if you have an existing health condition.
