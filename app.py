import streamlit as st
import joblib

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Review Intelligence",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        text-align: center;
        color: #1f2937;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .review-box {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .result-box {
        padding: 22px;
        border-radius: 15px;
        text-align: center;
        font-size: 25px;
        font-weight: 700;
        margin-top: 20px;
    }

    .positive {
        background-color: #dcfce7;
        color: #166534;
    }

    .negative {
        background-color: #fee2e2;
        color: #991b1b;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 14px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load model
# -----------------------------
model = joblib.load("smart_review_svm_pipeline.pkl")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">🧠 Smart Review Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered Amazon Review Sentiment Analysis</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Information section
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "Linear SVM")

with col2:
    st.metric("Accuracy", "86.45%")

with col3:
    st.metric("Task", "Sentiment")

st.write("")

# -----------------------------
# Review input section
# -----------------------------
st.markdown('<div class="review-box">', unsafe_allow_html=True)

st.subheader("📝 Enter Your Product Review")

review = st.text_area(
    "Write your review below:",
    placeholder="Example: The product quality is excellent and worth the money...",
    height=150
)

predict_button = st.button(
    "🔍 Analyze Sentiment",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Prediction
# -----------------------------
if predict_button:
    if review.strip() == "":
        st.warning("Please enter a review before analyzing.")
    else:
        prediction = model.predict([review])[0]

        if prediction == "pos":
            st.markdown(
                '<div class="result-box positive">😊 Positive Review</div>',
                unsafe_allow_html=True
            )
            st.success("The model detected a positive sentiment.")
        else:
            st.markdown(
                '<div class="result-box negative">😞 Negative Review</div>',
                unsafe_allow_html=True
            )
            st.error("The model detected a negative sentiment.")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    '<div class="footer">Built with Python, TF-IDF, Linear SVM and Streamlit</div>',
    unsafe_allow_html=True
)