import streamlit as st
from PIL import Image

# Set page title and configuration
st.set_page_config(page_title="ADAPTIFY", page_icon="🎓", layout="wide")

# Apply custom CSS for modern UI aesthetics
st.markdown(
    """
    <style>
        .cta-button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 16px;
        }
        .cta-button:hover {
            background-color: #2980b9;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <h1 style="text-align: center; color: #2c3e50;">Welcome to Adaptify</h1>
    <p style="text-align: center; color: #34495e;">Transform the way you learn with personalized assessments and insights.</p>
    """,
    unsafe_allow_html=True
)

# Main content columns
col1, col2 = st.columns([6, 4])

with col1:
    st.markdown(
        """
        <h2 style="color: #2c3e50;">Your Personalized Learning Journey</h2>
        <p style="color: #34495e;">Adaptify helps you track and accelerate your learning with tailored assessments.</p>
        """,
        unsafe_allow_html=True
    )

with col2:
    # Image Section
    try:
        st.image("image.jpg", width=400)
    except FileNotFoundError:
        st.warning("Please check if the image file exists in the correct location")

# Key Features Section
st.markdown("<h2 style='text-align: center; color: #2c3e50; margin: 40px 0 20px;'>Why Choose Adaptify?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

features = [
    {
        "icon": "🎯",
        "title": "Personalized Learning",
        "description": "AI-powered assessments that adapt to your unique learning style and pace"
    },
    {
        "icon": "📊",
        "title": "Real-time Analytics",
        "description": "Detailed insights into your progress and areas for improvement"
    },
    {
        "icon": "🚀",
        "title": "Rapid Progress",
        "description": "Accelerate your learning with targeted assessments and feedback"
    }
]

for col, feature in zip([col1, col2, col3], features):
    with col:
        st.markdown(
            f"""
            <div class="feature-box">
                <div class="feature-icon">{feature['icon']}</div>
                <h3 style="color: #2c3e50; margin-bottom: 10px;">{feature['title']}</h3>
                <p style="color: #34495e;">{feature['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Subscription Plans Section
st.markdown("<h2 style='text-align: center; color: #2c3e50; margin: 40px 0 20px;'>Choose Your Plan</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

plans = [
    {
        "title": "Individual",
        "price": "₹5000/month",
        "features": [
            "Personalized learning paths",
            "Real-time progress tracking",
            "Access to basic analytics",
            "Monthly progress reports",
            "24/7 Customer support"
        ],
        "button": "Get Started"
    },
    {
        "title": "Educators",
        "price": "₹10000/month",
        "features": [
            "Classroom management tools",
            "Student performance analytics",
            "Customizable assessments",
            "Collaboration tools",
            "Dedicated support"
        ],
        "button": "Get Started"
    },
    {
        "title": "Researchers",
        "price": "₹20000/month",
        "features": [
            "Advanced data analytics",
            "Custom research tools",
            "Access to raw data",
            "Collaboration with other researchers",
            "Priority support"
        ],
        "button": "Get Started"
    }
]

for col, plan in zip([col1, col2, col3], plans):
    with col:
        st.markdown(
            f"""
            <div class="plan-box">
                <h3 class="plan-title">{plan['title']}</h3>
                <div class="plan-price">{plan['price']}</div>
                <ul class="plan-features">
                    {''.join(f'<li>{feature}</li>' for feature in plan['features'])}
                </ul>
                <a href="#" class="cta-button">{plan['button']}</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Final CTA Section
st.markdown(
    """
    <div style="text-align: center; margin: 60px 0;">
        <h2 style="color: #2c3e50; margin-bottom: 20px;">Ready to Transform Your Learning?</h2>
        <a href="#" class="cta-button">Get Started Now</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>&copy; 2025 Adaptify. All rights reserved.</p>
        <p>Terms of Service | Privacy Policy</p>
    </div>
    """,
    unsafe_allow_html=True
)
