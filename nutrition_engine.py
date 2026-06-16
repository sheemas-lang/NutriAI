"""
nutrition_engine.py
Rule-based nutrition recommendation engine — no external API required.
"""

FOOD_DB = {
    "Weight Loss": {
        "eat": ["Oats", "Moong Dal", "Brown Rice", "Spinach", "Broccoli", "Cucumber",
                "Greek Yoghurt", "Eggs", "Chicken Breast", "Tofu", "Berries",
                "Apple", "Green Tea", "Lemon Water", "Flaxseeds"],
        "avoid": ["White Bread", "Sugary Drinks", "Fried Snacks", "Maida",
                  "Sweets & Mithai", "Packaged Juices", "Butter Naan"]
    },
    "Muscle Gain": {
        "eat": ["Chicken Breast", "Paneer", "Eggs", "Lentils", "Quinoa",
                "Brown Rice", "Banana", "Milk", "Greek Yoghurt", "Almonds",
                "Peanut Butter", "Tofu", "Chickpeas", "Sweet Potato"],
        "avoid": ["Alcohol", "Processed Meats", "Sugary Cereals",
                  "Deep-fried Food", "Carbonated Drinks"]
    },
    "Maintain Weight": {
        "eat": ["Whole Grains", "Seasonal Vegetables", "Fruits", "Dal",
                "Curd", "Nuts & Seeds", "Lean Protein", "Olive Oil", "Legumes"],
        "avoid": ["Trans Fats", "Excess Salt", "Ultra-processed Snacks",
                  "Refined Sugar", "Alcohol"]
    },
    "Improve Energy": {
        "eat": ["Bananas", "Oats", "Dates", "Nuts", "Dark Chocolate",
                "Eggs", "Spinach", "Sweet Potato", "Coconut Water", "Iron-rich Greens"],
        "avoid": ["Excess Caffeine", "Heavy Fried Meals", "Sugary Snacks",
                  "Refined Carbs", "Alcohol"]
    },
    "Better Gut Health": {
        "eat": ["Curd / Probiotic Yoghurt", "Bananas", "Oats", "Ginger",
                "Turmeric", "Flaxseeds", "Papaya", "Kefir", "Fermented Foods",
                "Leafy Greens", "Beans"],
        "avoid": ["Spicy Oily Food", "Excess Dairy (if sensitive)", "Alcohol",
                  "Carbonated Drinks", "Artificial Sweeteners"]
    },
    "Heart Health": {
        "eat": ["Walnuts", "Flaxseeds", "Oats", "Salmon / Mackerel",
                "Olive Oil", "Garlic", "Berries", "Dark Leafy Greens",
                "Avocado", "Legumes"],
        "avoid": ["Saturated Fats", "Trans Fats", "Excess Salt",
                  "Red Meat", "Processed Foods", "Sugary Drinks"]
    },
    "Manage Diabetes": {
        "eat": ["Bitter Gourd", "Methi Seeds", "Barley", "Moong Dal",
                "Cinnamon", "Brown Rice (small portions)", "Leafy Greens",
                "Nuts", "Eggs", "Fish"],
        "avoid": ["White Rice", "Maida", "Sugary Drinks", "Sweets",
                  "Potatoes (excess)", "Processed Cereals", "Fruit Juices"]
    },
    "Athletic Performance": {
        "eat": ["Banana", "Oats", "Chicken / Fish", "Eggs", "Brown Rice",
                "Sweet Potato", "Greek Yoghurt", "Beets", "Quinoa",
                "Coconut Water", "Dark Chocolate"],
        "avoid": ["Alcohol", "High-fibre Before Training", "Heavy Fried Food",
                  "Excess Caffeine", "Sugary Sports Drinks"]
    },
}

KEY_NUTRIENTS = {
    "Weight Loss": [
        {"nutrient": "Fibre", "reason": "Keeps you full longer, reduces calorie intake", "sources": ["Oats", "Lentils", "Broccoli"]},
        {"nutrient": "Protein", "reason": "Preserves muscle while in a calorie deficit", "sources": ["Eggs", "Chicken", "Tofu"]},
        {"nutrient": "Vitamin C", "reason": "Boosts metabolism and immunity", "sources": ["Berries", "Lemon", "Amla"]},
        {"nutrient": "Iron", "reason": "Prevents fatigue during weight-loss phase", "sources": ["Spinach", "Moong Dal", "Seeds"]},
    ],
    "Muscle Gain": [
        {"nutrient": "Protein", "reason": "Essential for muscle repair and synthesis", "sources": ["Chicken", "Paneer", "Eggs"]},
        {"nutrient": "Creatine (natural)", "reason": "Supports explosive strength", "sources": ["Red Meat", "Fish", "Poultry"]},
        {"nutrient": "Zinc", "reason": "Supports testosterone and recovery", "sources": ["Pumpkin Seeds", "Chickpeas", "Nuts"]},
        {"nutrient": "Complex Carbs", "reason": "Fuel for intense training sessions", "sources": ["Sweet Potato", "Brown Rice", "Quinoa"]},
    ],
    "Maintain Weight": [
        {"nutrient": "Balanced Macros", "reason": "Sustains energy without excess storage", "sources": ["Dal", "Rice", "Veggies"]},
        {"nutrient": "Magnesium", "reason": "Supports metabolic regulation", "sources": ["Nuts", "Seeds", "Dark Greens"]},
        {"nutrient": "B-Vitamins", "reason": "Efficient energy metabolism", "sources": ["Whole Grains", "Eggs", "Dairy"]},
        {"nutrient": "Omega-3", "reason": "Reduces inflammation", "sources": ["Flaxseeds", "Walnuts", "Fish"]},
    ],
    "Improve Energy": [
        {"nutrient": "Iron", "reason": "Prevents anaemia-related fatigue", "sources": ["Spinach", "Dates", "Dal"]},
        {"nutrient": "Vitamin B12", "reason": "Critical for nerve & energy metabolism", "sources": ["Eggs", "Milk", "Fish"]},
        {"nutrient": "Complex Carbs", "reason": "Sustained energy release", "sources": ["Oats", "Sweet Potato", "Banana"]},
        {"nutrient": "Magnesium", "reason": "Involved in 300+ energy reactions", "sources": ["Nuts", "Seeds", "Dark Chocolate"]},
    ],
    "Better Gut Health": [
        {"nutrient": "Probiotics", "reason": "Replenishes good gut bacteria", "sources": ["Curd", "Kefir", "Fermented Foods"]},
        {"nutrient": "Prebiotics", "reason": "Feeds beneficial bacteria", "sources": ["Oats", "Banana", "Garlic"]},
        {"nutrient": "Fibre", "reason": "Promotes healthy bowel movement", "sources": ["Flaxseeds", "Beans", "Veggies"]},
        {"nutrient": "Zinc", "reason": "Supports gut lining integrity", "sources": ["Pumpkin Seeds", "Chickpeas", "Meat"]},
    ],
    "Heart Health": [
        {"nutrient": "Omega-3 Fatty Acids", "reason": "Lowers triglycerides and blood pressure", "sources": ["Walnuts", "Flaxseeds", "Salmon"]},
        {"nutrient": "Potassium", "reason": "Balances sodium, reduces BP", "sources": ["Bananas", "Sweet Potato", "Legumes"]},
        {"nutrient": "Antioxidants", "reason": "Protects arterial walls", "sources": ["Berries", "Dark Chocolate", "Greens"]},
        {"nutrient": "Soluble Fibre", "reason": "Reduces LDL cholesterol", "sources": ["Oats", "Barley", "Beans"]},
    ],
    "Manage Diabetes": [
        {"nutrient": "Chromium", "reason": "Improves insulin sensitivity", "sources": ["Broccoli", "Whole Grains", "Nuts"]},
        {"nutrient": "Magnesium", "reason": "Linked to lower diabetes risk", "sources": ["Leafy Greens", "Seeds", "Legumes"]},
        {"nutrient": "Fibre", "reason": "Slows glucose absorption", "sources": ["Barley", "Methi", "Moong Dal"]},
        {"nutrient": "Alpha-Lipoic Acid", "reason": "Reduces oxidative stress in diabetics", "sources": ["Spinach", "Broccoli", "Meat"]},
    ],
    "Athletic Performance": [
        {"nutrient": "Complex Carbs", "reason": "Primary fuel for endurance and strength", "sources": ["Oats", "Sweet Potato", "Brown Rice"]},
        {"nutrient": "Electrolytes", "reason": "Prevents cramping, maintains hydration", "sources": ["Coconut Water", "Banana", "Salt"]},
        {"nutrient": "Protein", "reason": "Muscle repair post-training", "sources": ["Chicken", "Eggs", "Greek Yoghurt"]},
        {"nutrient": "Nitrates", "reason": "Improves blood flow and stamina", "sources": ["Beetroot", "Leafy Greens", "Arugula"]},
    ],
}

MEAL_TEMPLATES = {
    "Weight Loss": [
        {"name": "Lemon Water + Soaked Almonds", "time": "6:30 AM", "description": "Kickstart metabolism with warm lemon water. 5–6 soaked almonds provide healthy fat & vitamin E."},
        {"name": "Oats Porridge with Berries", "time": "8:00 AM", "description": "Steel-cut oats with skimmed milk, mixed berries, chia seeds. High fibre, low GI breakfast."},
        {"name": "Buttermilk + Fruit", "time": "11:00 AM", "description": "Low-fat buttermilk with 1 seasonal fruit. Probiotic mid-morning snack, ~150 kcal."},
        {"name": "Moong Dal + Sabzi + Salad", "time": "1:30 PM", "description": "1 cup moong dal, 1 cup mixed vegetable sabzi, cucumber-tomato salad with lemon dressing. Balanced macro lunch."},
        {"name": "Green Tea + Roasted Makhana", "time": "4:30 PM", "description": "Unsweetened green tea with a handful of roasted fox nuts. Antioxidant-rich, low-calorie snack."},
        {"name": "Grilled Paneer / Tofu Stir-fry", "time": "7:30 PM", "description": "100g grilled paneer or tofu with stir-fried broccoli, bell peppers, minimal oil. Light, protein-rich dinner."},
    ],
    "Muscle Gain": [
        {"name": "Pre-workout Banana + Peanut Butter Toast", "time": "6:30 AM", "description": "1 banana + 2 tsp peanut butter on multigrain toast. Fast carbs + healthy fats for energy."},
        {"name": "Egg White Omelette + Milk", "time": "8:00 AM", "description": "4-egg white omelette with vegetables, 1 glass full-fat milk. ~35g protein to start the day."},
        {"name": "Greek Yoghurt + Almonds", "time": "11:00 AM", "description": "200g Greek yoghurt with 10 almonds and a drizzle of honey. Protein-rich mid-morning fuel."},
        {"name": "Chicken / Paneer Rice Bowl", "time": "1:30 PM", "description": "150g grilled chicken or paneer, 1 cup brown rice, steamed veggies. High-protein power lunch."},
        {"name": "Post-workout Protein Shake + Banana", "time": "5:00 PM", "description": "Whey / plant protein shake with milk, 1 banana. Anabolic window — consume within 30 min of training."},
        {"name": "Dal + Roti + Sabzi", "time": "8:00 PM", "description": "2 whole-wheat rotis, 1 cup dal, vegetable sabzi. Complete amino acid profile for overnight recovery."},
    ],
    "Maintain Weight": [
        {"name": "Warm Water + Soaked Seeds", "time": "7:00 AM", "description": "Warm water with soaked sabja / chia seeds. Hydrates and sets a healthy tone."},
        {"name": "Poha / Upma with Veggies", "time": "8:30 AM", "description": "Vegetable poha or upma with mustard seeds, curry leaves, peas. Light, balanced breakfast."},
        {"name": "Fruit + Curd", "time": "11:00 AM", "description": "Seasonal fruit bowl with 100g low-fat curd. Probiotics + natural sugars."},
        {"name": "Balanced Thali", "time": "1:30 PM", "description": "1 cup dal, 1 cup sabzi, 2 rotis or 1 cup rice, salad, curd. All macros in proportion."},
        {"name": "Nuts & Seeds Mix", "time": "5:00 PM", "description": "Mixed handful of walnuts, almonds, pumpkin seeds. Omega-3 and mineral rich snack."},
        {"name": "Light Khichdi or Soup + Salad", "time": "7:30 PM", "description": "Moong dal khichdi with ghee or vegetable soup. Easy to digest, well-balanced dinner."},
    ],
    "Improve Energy": [
        {"name": "Dates + Warm Milk", "time": "6:30 AM", "description": "2–3 dates with warm milk. Natural sugars + calcium for an instant energy boost."},
        {"name": "Banana Oat Smoothie", "time": "8:00 AM", "description": "Banana, oats, milk, almond butter blended. Sustained-release energy breakfast."},
        {"name": "Coconut Water + Roasted Chana", "time": "11:00 AM", "description": "Natural electrolyte drink with iron-rich roasted chickpeas."},
        {"name": "Iron-rich Lunch", "time": "1:30 PM", "description": "Palak paneer or spinach dal with brown rice. Iron + vitamin C combo boosts absorption."},
        {"name": "Dark Chocolate + Green Tea", "time": "4:30 PM", "description": "2 squares of 70%+ dark chocolate with unsweetened green tea. Magnesium + antioxidants."},
        {"name": "Egg / Tofu Stir-fry with Quinoa", "time": "7:30 PM", "description": "Complete protein dinner with quinoa — all essential amino acids for overnight repair."},
    ],
    "Better Gut Health": [
        {"name": "Warm Water with Honey & Ginger", "time": "6:30 AM", "description": "Anti-inflammatory morning drink that activates digestive enzymes."},
        {"name": "Curd with Banana & Flaxseeds", "time": "8:00 AM", "description": "Probiotic curd with prebiotic banana and fibre-rich flaxseeds. Triple gut support."},
        {"name": "Papaya or Kiwi", "time": "11:00 AM", "description": "Papain and actinidin enzymes aid protein digestion and gut motility."},
        {"name": "Khichdi with Ghee + Fermented Pickle", "time": "1:30 PM", "description": "Easy-to-digest khichdi with probiotic achaar (fermented pickle) in moderation."},
        {"name": "Buttermilk + Ajwain", "time": "4:30 PM", "description": "Homemade buttermilk with carom seeds — classic Ayurvedic digestive aid."},
        {"name": "Vegetable Soup + Whole Grain Roti", "time": "7:30 PM", "description": "Light fibre-rich dinner that doesn't overload the gut before sleep."},
    ],
    "Heart Health": [
        {"name": "Warm Lemon Water + Walnuts", "time": "6:30 AM", "description": "5 walnuts provide Omega-3 ALA. Lemon water supports arterial health."},
        {"name": "Oat Porridge with Berries & Flaxseeds", "time": "8:00 AM", "description": "Soluble fibre from oats lowers LDL. Berries add antioxidants. Flaxseeds add Omega-3."},
        {"name": "Fruit + Unsalted Nuts", "time": "11:00 AM", "description": "Almonds and seasonal fruit. Healthy fats + potassium for blood pressure control."},
        {"name": "Grilled Fish / Dal + Salad", "time": "1:30 PM", "description": "Omega-3-rich fish or lentils with raw vegetable salad, olive oil dressing."},
        {"name": "Green Tea + Seeds Mix", "time": "5:00 PM", "description": "EGCG in green tea is cardioprotective. Pumpkin & sunflower seeds for magnesium."},
        {"name": "Steamed Vegetables + Brown Rice + Garlic Dal", "time": "7:30 PM", "description": "Garlic reduces cholesterol. Steamed veggies preserve heart-healthy antioxidants."},
    ],
    "Manage Diabetes": [
        {"name": "Methi Water + Soaked Almonds", "time": "6:30 AM", "description": "Overnight soaked fenugreek water controls morning glucose spikes."},
        {"name": "Vegetable Oats Upma / Egg White Omelette", "time": "8:00 AM", "description": "Low-GI breakfast. Avoid fruits or simple carbs in the morning."},
        {"name": "Buttermilk or Cucumber", "time": "11:00 AM", "description": "Low-carb, hydrating mid-morning snack. Keeps blood sugar stable."},
        {"name": "Moong Dal + Karela Sabzi + 1 Roti", "time": "1:30 PM", "description": "Bitter gourd regulates blood sugar. Small portions of whole-wheat roti."},
        {"name": "Roasted Chana + Green Tea", "time": "4:30 PM", "description": "High-protein, low-GI snack that prevents afternoon glucose dip."},
        {"name": "Palak Soup + Grilled Paneer / Fish", "time": "7:30 PM", "description": "Low-carb, high-protein dinner. Spinach provides chromium for insulin sensitivity."},
    ],
    "Athletic Performance": [
        {"name": "Pre-workout: Banana + Black Coffee", "time": "6:00 AM", "description": "Fast carbs for energy, caffeine for focus and performance. Consume 30 min before training."},
        {"name": "Post-workout: Protein + Carb Meal", "time": "8:30 AM", "description": "4 egg whites / whey shake + oats or banana. Golden 30-minute anabolic window."},
        {"name": "Coconut Water + Nuts", "time": "11:00 AM", "description": "Electrolyte replenishment. Nuts for sustained energy."},
        {"name": "Chicken / Fish + Sweet Potato + Salad", "time": "1:30 PM", "description": "Performance lunch: lean protein for repair, sweet potato for glycogen, greens for micronutrients."},
        {"name": "Beet Juice + Whole Grain Toast", "time": "5:00 PM", "description": "Nitrates in beetroot enhance blood flow and stamina for evening sessions."},
        {"name": "Dal + Brown Rice + Curd", "time": "8:00 PM", "description": "Complete recovery dinner. Casein in curd supports slow overnight muscle repair."},
    ],
}

HYDRATION = {
    "Weight Loss":          "Aim for 2.5–3 L of water daily. Start with 500 ml warm water in the morning. Avoid caloric beverages — swap sugary drinks with green tea or jeera water.",
    "Muscle Gain":          "Drink 3–4 L daily — muscles are 75% water. Increase by 500 ml on training days. Coconut water post-workout restores electrolytes naturally.",
    "Maintain Weight":      "Target 2–2.5 L daily. A glass of water before each meal aids portion control and digestion.",
    "Improve Energy":       "Dehydration is the #1 cause of fatigue. Drink 2.5–3 L daily. Add a pinch of Himalayan salt + lemon to morning water for electrolytes.",
    "Better Gut Health":    "Drink 2.5 L daily, mostly between meals rather than during — it preserves digestive enzyme concentration.",
    "Heart Health":         "Aim for 2–2.5 L daily. Warm herbal teas (tulsi, hibiscus) additionally support cardiovascular health.",
    "Manage Diabetes":      "Drink 2.5–3 L of plain water daily. Avoid fruit juices entirely. Cinnamon-infused water can help manage blood sugar.",
    "Athletic Performance": "3–4 L on rest days, 4–5 L on training days. Sip 200–250 ml every 20 minutes during exercise to stay hydrated.",
}

WEEKLY_TIPS = {
    "Weight Loss":          "Meal prep on Sundays: cook a large batch of moong dal, boil eggs, and chop salad veggies so you have healthy options ready all week.",
    "Muscle Gain":          "Track your weekly protein intake. Aim for 1.6–2.2g per kg bodyweight. If short, add a scoop of plant or whey protein to your morning oats.",
    "Maintain Weight":      "Practise mindful eating: put your phone down, chew slowly, and stop at 80% full (hara hachi bu). It takes 20 minutes for satiety signals to reach the brain.",
    "Improve Energy":       "Add a 10-minute morning sunlight walk to your routine. Sunlight resets your circadian rhythm and dramatically improves daytime energy.",
    "Better Gut Health":    "Introduce one new fermented food per week — homemade curd, kanji, idli/dosa batter, or homemade pickles — to diversify your gut microbiome.",
    "Heart Health":         "Replace your cooking oil with cold-pressed mustard or extra virgin olive oil this week. Small fat swaps make a significant long-term difference.",
    "Manage Diabetes":      "Walk for 15–20 minutes after each main meal. Post-meal walks are clinically proven to reduce glucose spikes by up to 30%.",
    "Athletic Performance": "Log your sleep — target 7–9 hours. Growth hormone is released in deep sleep, making it the single most powerful recovery tool available.",
}


def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "Female":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return 10 * weight + 6.25 * height - 5 * age - 78


ACTIVITY_MULTIPLIERS = {
    "Sedentary (desk job, no exercise)":   1.2,
    "Lightly Active (1–3 days/week)":      1.375,
    "Moderately Active (3–5 days/week)":   1.55,
    "Very Active (6–7 days/week)":         1.725,
    "Athlete / Intense Training":          1.9,
}

GOAL_CALORIE_ADJUST = {
    "Weight Loss":          -400,
    "Muscle Gain":          +350,
    "Maintain Weight":      0,
    "Improve Energy":       +100,
    "Better Gut Health":    0,
    "Heart Health":         -100,
    "Manage Diabetes":      -200,
    "Athletic Performance": +300,
}


def calculate_macros(tdee, goal):
    if goal == "Weight Loss":
        protein_pct, carb_pct, fat_pct = 0.35, 0.40, 0.25
    elif goal == "Muscle Gain":
        protein_pct, carb_pct, fat_pct = 0.30, 0.50, 0.20
    elif goal == "Manage Diabetes":
        protein_pct, carb_pct, fat_pct = 0.30, 0.35, 0.35
    elif goal == "Athletic Performance":
        protein_pct, carb_pct, fat_pct = 0.25, 0.55, 0.20
    elif goal == "Heart Health":
        protein_pct, carb_pct, fat_pct = 0.20, 0.50, 0.30
    else:
        protein_pct, carb_pct, fat_pct = 0.25, 0.50, 0.25

    protein_g = int((tdee * protein_pct) / 4)
    carbs_g   = int((tdee * carb_pct)    / 4)
    fat_g     = int((tdee * fat_pct)     / 9)
    return protein_g, carbs_g, fat_g


def calculate_health_score(bmi, activity, goal, conditions):
    score = 60

    if 18.5 <= bmi <= 24.9:
        score += 15
    elif 25 <= bmi <= 29.9:
        score += 5
    elif bmi < 18.5:
        score += 8
    else:
        score -= 5

    activity_bonus = {
        "Sedentary (desk job, no exercise)":   0,
        "Lightly Active (1–3 days/week)":      5,
        "Moderately Active (3–5 days/week)":   10,
        "Very Active (6–7 days/week)":         14,
        "Athlete / Intense Training":          18,
    }
    score += activity_bonus.get(activity, 5)

    penalty_conditions = {
        "Type 2 Diabetes", "Hypertension", "High Cholesterol",
        "Kidney Disease", "Celiac Disease", "Thyroid Disorder"
    }
    if conditions:
        for c in conditions:
            if c in penalty_conditions:
                score -= 8
            elif c != "None":
                score -= 4

    return max(10, min(score, 97))


def generate_summary(name, goal, bmi, calories, activity, diet_type, conditions):
    bmi_cat = (
        "underweight" if bmi < 18.5 else
        "healthy weight" if bmi < 25 else
        "overweight" if bmi < 30 else
        "obese category"
    )
    condition_note = ""
    if conditions and "None" not in conditions:
        condition_note = f" Given your {', '.join(conditions)}, extra care has been taken to align this plan with those needs."

    diet_note = "" if diet_type == "No Restriction" else f" All recommendations respect your {diet_type} dietary style."

    return (
        f"Your BMI of {bmi:.1f} places you in the {bmi_cat} range. "
        f"Based on your {activity.split('(')[0].strip().lower()} lifestyle and goal to {goal.lower()}, "
        f"your personalised daily calorie target is {calories} kcal."
        f"{diet_note}{condition_note} "
        f"Follow the meal plan below consistently for at least 3–4 weeks to see measurable results."
    )


def get_plan(age, gender, weight, height, goal, activity, diet_type, allergies, conditions, extra=""):
    bmi    = round(weight / ((height / 100) ** 2), 1)
    bmr    = calculate_bmr(weight, height, age, gender)
    tdee   = bmr * ACTIVITY_MULTIPLIERS.get(activity, 1.375)
    cal_adj = GOAL_CALORIE_ADJUST.get(goal, 0)
    calories = max(1200, int(tdee + cal_adj))
    protein_g, carbs_g, fat_g = calculate_macros(calories, goal)
    score  = calculate_health_score(bmi, activity, goal, conditions)
    summary = generate_summary("", goal, bmi, calories, activity, diet_type, conditions)

    foods  = FOOD_DB.get(goal, FOOD_DB["Maintain Weight"])
    eat    = [f for f in foods["eat"]   if not any(a.lower() in f.lower() for a in (allergies or []))][:10]
    avoid  = foods["avoid"]

    meals  = MEAL_TEMPLATES.get(goal, MEAL_TEMPLATES["Maintain Weight"])
    # Adjust meals for diet type
    veg_swaps = {"Chicken": "Paneer", "Fish": "Tofu", "Salmon": "Tofu",
                 "Red Meat": "Rajma", "Whey": "Plant Protein"}
    if diet_type in ("Vegetarian", "Vegan"):
        cleaned = []
        for m in meals:
            desc = m["description"]
            name_ = m["name"]
            for animal, veg in veg_swaps.items():
                desc  = desc.replace(animal, veg)
                name_ = name_.replace(animal, veg)
            cleaned.append({"name": name_, "time": m["time"], "description": desc})
        meals = cleaned

    nutrients = KEY_NUTRIENTS.get(goal, KEY_NUTRIENTS["Maintain Weight"])
    hydration = HYDRATION.get(goal, "Aim for 2.5 L of water daily.")
    weekly    = WEEKLY_TIPS.get(goal, "Track your meals in a journal for one week.")

    return {
        "summary":       summary,
        "bmi":           bmi,
        "health_score":  score,
        "daily_calories": calories,
        "protein_g":     protein_g,
        "carbs_g":       carbs_g,
        "fat_g":         fat_g,
        "meals":         meals,
        "key_nutrients": nutrients,
        "foods_to_eat":  eat,
        "foods_to_avoid": avoid,
        "hydration_tip": hydration,
        "weekly_tip":    weekly,
        "disclaimer":    "This plan is for general wellness guidance only. Consult a registered dietitian or doctor before making significant dietary changes, especially if you have existing health conditions.",
    }
