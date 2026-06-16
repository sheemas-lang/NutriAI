import streamlit as st
from nutrition_engine import get_plan

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NutriAI · Personalised Nutrition",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700;800&display=swap');

:root {
    --bg:#0F1E0F;--bg2:#162616;--bg3:#1D3320;--card:#1A2E1A;
    --border:#2E4A2E;--mint:#7ED4A0;--mintl:#B8F0C8;--gold:#D4A843;
    --cream:#F0EAD6;--muted:#6B8F6B;--radius:16px;
}

html,body,[data-testid="stAppViewContainer"]{background:var(--bg)!important;color:var(--cream)!important;font-family:'Inter',sans-serif;}
[data-testid="stSidebar"]{background:var(--bg2)!important;border-right:1px solid var(--border)!important;}
[data-testid="stSidebar"] *{color:var(--cream)!important;}
#MainMenu,footer,header{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}

.hero-wrap{display:flex;align-items:center;gap:18px;padding:36px 0 8px;}
.hero-icon{font-size:52px;line-height:1;filter:drop-shadow(0 0 18px #7ED4A055);}
.hero-title{font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:800;background:linear-gradient(135deg,var(--mintl) 0%,var(--gold) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1.1;margin:0;}
.hero-sub{color:var(--muted);font-size:.95rem;margin:4px 0 0;}
.ndivider{height:1px;background:linear-gradient(90deg,transparent,var(--border),transparent);margin:20px 0;}
.sec-label{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--mint);margin-bottom:10px;}

[data-testid="stSidebar"] .stSelectbox>div>div,
[data-testid="stSidebar"] .stNumberInput>div>div>input,
[data-testid="stSidebar"] .stTextArea>div>textarea,
[data-testid="stSidebar"] .stTextInput>div>input{background:var(--bg3)!important;border:1px solid var(--border)!important;border-radius:10px!important;color:var(--cream)!important;font-family:'Inter',sans-serif!important;}

div[data-testid="stSidebar"] .stButton>button{width:100%;background:linear-gradient(135deg,#3A7D52 0%,#2E6644 100%)!important;color:var(--mintl)!important;border:none!important;border-radius:12px!important;padding:14px 0!important;font-family:'Inter',sans-serif!important;font-weight:600!important;font-size:.95rem!important;letter-spacing:.04em!important;box-shadow:0 4px 24px #3A7D5244!important;transition:all .2s!important;}
div[data-testid="stSidebar"] .stButton>button:hover{background:linear-gradient(135deg,#4A9D64 0%,#3A7D52 100%)!important;transform:translateY(-1px)!important;}

.macro-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:20px 0;}
.macro-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px 16px;text-align:center;position:relative;overflow:hidden;}
.macro-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
.macro-card.calories::before{background:linear-gradient(90deg,var(--gold),#F0C060);}
.macro-card.protein::before{background:linear-gradient(90deg,#7EC8F0,#5AA8D0);}
.macro-card.carbs::before{background:linear-gradient(90deg,var(--mint),#50B070);}
.macro-card.fat::before{background:linear-gradient(90deg,#E09070,#C06840);}
.macro-value{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700;line-height:1;}
.macro-card.calories .macro-value{color:var(--gold);}
.macro-card.protein  .macro-value{color:#7EC8F0;}
.macro-card.carbs    .macro-value{color:var(--mint);}
.macro-card.fat      .macro-value{color:#E09070;}
.macro-label{color:var(--muted);font-size:.78rem;margin-top:6px;font-weight:500;}

.result-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:26px;margin-bottom:16px;}
.result-card h3{font-family:'Playfair Display',serif;color:var(--mintl);font-size:1.2rem;margin:0 0 14px;padding-bottom:10px;border-bottom:1px solid var(--border);}

.meal-item{background:var(--bg3);border-left:3px solid var(--mint);border-radius:0 10px 10px 0;padding:12px 16px;margin-bottom:10px;}
.meal-name{font-weight:600;font-size:.95rem;color:var(--cream);}
.meal-desc{color:var(--muted);font-size:.83rem;margin-top:3px;line-height:1.5;}

.chip-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;}
.chip{background:var(--bg3);border:1px solid var(--border);border-radius:20px;padding:5px 14px;font-size:.78rem;color:var(--mintl);font-weight:500;}
.chip.warn{border-color:#E09070;color:#E09070;}

.empty-state{text-align:center;padding:70px 40px;color:var(--muted);}
.empty-state .e-icon{font-size:60px;margin-bottom:16px;opacity:.5;}
.empty-state p{font-size:1rem;line-height:1.7;max-width:380px;margin:0 auto;}

.bmi-bar-wrap{margin:10px 0 6px;}
.bmi-bar-bg{height:8px;border-radius:4px;background:linear-gradient(90deg,#7EC8F0 0%,#7ED4A0 30%,#D4A843 60%,#E07070 100%);position:relative;}
.bmi-needle{position:absolute;top:-4px;width:16px;height:16px;border-radius:50%;background:white;border:2px solid #333;transform:translateX(-50%);}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;padding:8px 0 20px;">
        <span style="font-size:28px">🌿</span>
        <span style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:800;
                     background:linear-gradient(135deg,#B8F0C8,#D4A843);
                     -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            NutriAI
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-label">Personal Details</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: age    = st.number_input("Age",        min_value=10,  max_value=100, value=28,   step=1)
    with c2: gender = st.selectbox("Gender",        ["Male","Female","Other"])
    c3, c4 = st.columns(2)
    with c3: weight = st.number_input("Weight (kg)", min_value=30.0, max_value=250.0, value=70.0, step=0.5)
    with c4: height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.5)

    st.markdown('<div class="ndivider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Goals & Activity</div>', unsafe_allow_html=True)

    goal = st.selectbox("Primary Goal", [
        "Weight Loss","Muscle Gain","Maintain Weight",
        "Improve Energy","Better Gut Health","Heart Health",
        "Manage Diabetes","Athletic Performance"
    ])
    activity = st.selectbox("Activity Level", [
        "Sedentary (desk job, no exercise)",
        "Lightly Active (1–3 days/week)",
        "Moderately Active (3–5 days/week)",
        "Very Active (6–7 days/week)",
        "Athlete / Intense Training"
    ])

    st.markdown('<div class="ndivider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Dietary Preferences</div>', unsafe_allow_html=True)

    diet_type = st.selectbox("Diet Type", [
        "No Restriction","Vegetarian","Vegan","Pescatarian",
        "Keto","Paleo","Mediterranean","Gluten-Free","Dairy-Free"
    ])
    allergies = st.multiselect("Allergies / Avoid", [
        "Nuts","Dairy","Gluten","Eggs","Soy","Shellfish","Fish","Nightshades","Legumes"
    ])

    st.markdown('<div class="ndivider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Health Context</div>', unsafe_allow_html=True)

    conditions = st.multiselect("Health Conditions (if any)", [
        "None","Type 2 Diabetes","Hypertension","High Cholesterol",
        "PCOS","IBS / IBD","Thyroid Disorder","Anaemia",
        "Kidney Disease","Celiac Disease"
    ])
    extra = st.text_area("Anything else?",
        placeholder="e.g. I train at 6 am, I prefer South Indian food…", height=70)

    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("✦ Generate My Plan", use_container_width=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-icon">🌿</div>
    <div>
        <p class="hero-title">Your Nutrition Plan</p>
        <p class="hero-sub">Science-backed recommendations tailored to your body, goals &amp; lifestyle</p>
    </div>
</div>
<div class="ndivider"></div>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────
def score_color(s):
    if s >= 80: return "#7ED4A0", "#1A4A2A"
    if s >= 60: return "#D4A843", "#3A2A0A"
    return "#E07070", "#3A1A1A"

def bmi_category(bmi):
    if bmi < 18.5: return "Underweight", "#7EC8F0"
    if bmi < 25:   return "Healthy",     "#7ED4A0"
    if bmi < 30:   return "Overweight",  "#D4A843"
    return "Obese", "#E07070"

def bmi_needle_pct(bmi):
    # Map bmi 15–40 → 0–100%
    return max(0, min(100, (bmi - 15) / 25 * 100))


# ── State ─────────────────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None

# ── Generate ──────────────────────────────────────────────────────────────────
if generate:
    with st.spinner("🌿 Calculating your personalised plan…"):
        import time; time.sleep(0.6)   # brief UX pause
        st.session_state.result = get_plan(
            age, gender, weight, height, goal, activity,
            diet_type, allergies, conditions, extra
        )

# ── Render ────────────────────────────────────────────────────────────────────
if st.session_state.result:
    d = st.session_state.result

    # ── Macro bar ──
    st.markdown(f"""
    <div class="macro-grid">
        <div class="macro-card calories">
            <div class="macro-value">{d['daily_calories']}</div>
            <div style="font-size:.8rem;color:var(--muted);">kcal</div>
            <div class="macro-label">Daily Calories</div>
        </div>
        <div class="macro-card protein">
            <div class="macro-value">{d['protein_g']}<span style="font-size:.9rem">g</span></div>
            <div class="macro-label">Protein</div>
        </div>
        <div class="macro-card carbs">
            <div class="macro-value">{d['carbs_g']}<span style="font-size:.9rem">g</span></div>
            <div class="macro-label">Carbohydrates</div>
        </div>
        <div class="macro-card fat">
            <div class="macro-value">{d['fat_g']}<span style="font-size:.9rem">g</span></div>
            <div class="macro-label">Healthy Fats</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([3, 2], gap="large")

    with left:
        # Summary
        st.markdown(f"""
        <div class="result-card">
            <h3>✦ Personalised Overview</h3>
            <p style="color:var(--cream);line-height:1.75;margin:0 0 14px;">{d['summary']}</p>
            <div style="padding:12px 16px;background:var(--bg3);border-radius:10px;border-left:3px solid var(--gold);">
                <span style="color:var(--gold);font-weight:600;font-size:.82rem;">💧 HYDRATION TIP</span><br>
                <span style="color:var(--muted);font-size:.87rem;">{d['hydration_tip']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Meal Plan
        st.markdown('<div class="result-card"><h3>🍽 Daily Meal Plan</h3>', unsafe_allow_html=True)
        for m in d["meals"]:
            st.markdown(f"""
            <div class="meal-item">
                <div style="display:flex;justify-content:space-between;align-items:start;">
                    <div class="meal-name">{m['name']}</div>
                    <div style="color:#D4A843;font-size:.75rem;font-weight:500;
                                background:#3A2A0A;padding:3px 10px;border-radius:20px;
                                white-space:nowrap;margin-left:10px;">{m['time']}</div>
                </div>
                <div class="meal-desc">{m['description']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Key Nutrients
        st.markdown('<div class="result-card"><h3>⚗ Key Nutrients For You</h3>', unsafe_allow_html=True)
        for n in d["key_nutrients"]:
            st.markdown(f"""
            <div style="margin-bottom:14px;">
                <div style="font-weight:600;color:var(--mintl);font-size:.93rem;">{n['nutrient']}</div>
                <div style="color:var(--muted);font-size:.83rem;margin-top:3px;line-height:1.5;">{n['reason']}</div>
                <div style="color:#D4A843;font-size:.78rem;margin-top:5px;">
                    Sources: {" · ".join(n['sources'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        # Health Score ring
        score = d["health_score"]
        fg, bg_ = score_color(score)
        st.markdown(f"""
        <div class="result-card" style="text-align:center;">
            <h3 style="text-align:left;">◎ Health Score</h3>
            <div style="width:130px;height:130px;border-radius:50%;
                        background:conic-gradient({fg} 0% {score}%,#1D3320 {score}% 100%);
                        display:inline-flex;align-items:center;justify-content:center;
                        box-shadow:0 0 30px {fg}33;margin:10px 0;">
                <div style="width:100px;height:100px;border-radius:50%;background:var(--bg2);
                            display:flex;align-items:center;justify-content:center;flex-direction:column;">
                    <div style="font-family:'Playfair Display',serif;font-size:2rem;
                                font-weight:800;color:{fg};line-height:1;">{score}</div>
                    <div style="font-size:.68rem;color:var(--muted);">/ 100</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # BMI Card
        bmi = d["bmi"]
        bmi_cat, bmi_col = bmi_category(bmi)
        needle = bmi_needle_pct(bmi)
        st.markdown(f"""
        <div class="result-card">
            <h3>⊙ BMI Analysis</h3>
            <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px;">
                <span style="font-family:'Playfair Display',serif;font-size:2rem;
                             font-weight:800;color:{bmi_col};">{bmi}</span>
                <span style="background:{bmi_col}22;color:{bmi_col};
                             font-size:.75rem;font-weight:600;padding:4px 12px;
                             border-radius:20px;border:1px solid {bmi_col}55;">{bmi_cat}</span>
            </div>
            <div class="bmi-bar-wrap">
                <div class="bmi-bar-bg">
                    <div class="bmi-needle" style="left:{needle}%;"></div>
                </div>
            </div>
            <div style="display:flex;justify-content:space-between;
                        font-size:.65rem;color:var(--muted);margin-top:8px;">
                <span>Under</span><span>Healthy</span><span>Over</span><span>Obese</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Foods to Eat
        st.markdown(f"""
        <div class="result-card">
            <h3>✓ Eat More Of</h3>
            <div class="chip-row">
                {"".join(f'<span class="chip">{f}</span>' for f in d['foods_to_eat'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Foods to Avoid
        st.markdown(f"""
        <div class="result-card">
            <h3 style="color:#E09070;">✗ Limit or Avoid</h3>
            <div class="chip-row">
                {"".join(f'<span class="chip warn">{f}</span>' for f in d['foods_to_avoid'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Weekly Habit
        st.markdown(f"""
        <div class="result-card" style="border-color:#3A7D52;">
            <h3>🗓 Weekly Habit</h3>
            <p style="color:var(--cream);font-size:.9rem;line-height:1.65;margin:0;">
                {d['weekly_tip']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Disclaimer
        st.markdown(f"""
        <div style="padding:12px 16px;border-radius:10px;border:1px solid #3A2A0A;background:#1A1200;">
            <span style="color:#D4A843;font-size:.72rem;font-weight:600;">⚠ DISCLAIMER</span><br>
            <span style="color:#6B6030;font-size:.75rem;line-height:1.5;">{d['disclaimer']}</span>
        </div>
        """, unsafe_allow_html=True)

else:
    # Empty state
    st.markdown("""
    <div class="empty-state">
        <div class="e-icon">🌱</div>
        <p>Fill in your profile on the left and click<br>
        <strong style="color:#B8F0C8;">✦ Generate My Plan</strong>
        to receive your personalised nutrition recommendations — instantly, no internet required.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    features = [
        ("🔬","Science-Backed","Mifflin-St Jeor BMR formula with activity-adjusted TDEE. Macro splits calibrated per goal."),
        ("🎯","8 Goal Profiles","Weight loss, muscle gain, diabetes, heart health, gut health and more — each with unique plans."),
        ("⚡","Instant & Offline","No API key, no internet needed after install. Results in under a second."),
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3], features):
        with col:
            st.markdown(f"""
            <div style="background:var(--card);border:1px solid var(--border);
                        border-radius:var(--radius);padding:24px;text-align:center;min-height:150px;">
                <div style="font-size:32px;margin-bottom:10px;">{icon}</div>
                <div style="font-weight:600;color:var(--mintl);font-size:.95rem;margin-bottom:8px;">{title}</div>
                <div style="color:var(--muted);font-size:.82rem;line-height:1.5;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
