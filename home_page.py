import streamlit as st
from PIL import Image

# Set page title and configuration
st.set_page_config(page_title="ADAPTIFY AI", page_icon="🎓", layout="wide")

# Navigation function
def navigate_to_upload():
    st.switch_page("pages/upload.py")

# Helper function to convert image to base64
def image_to_base64(image):
    from io import BytesIO
    import base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Apply custom CSS for modern UI aesthetics
st.markdown(
    """
    <style>
        /* Global Styles */
        .stApp {
            background-color: #0a0a0a;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }

        /* Hero Section Styles */
        .hero-container {
            text-align: center;
            padding: 100px 20px;
            background: linear-gradient(135deg, #1a1a1a, #0a0a0a);
            border-radius: 20px;
            margin-bottom: 40px;
            animation: fadeIn 2s ease-in-out;
        }

        .main-title {
            font-size: 64px;
            font-weight: bold;
            margin-bottom: 20px;
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
            animation: slideIn 1.5s ease-in-out;
        }

        .tagline {
            font-size: 28px;
            margin-bottom: 30px;
            font-family: 'Inter', sans-serif;
            color: #b3b3b3;
            animation: fadeIn 2.5s ease-in-out;
        }

        /* Button Styles */
        .stButton button {
            background-color: #ff4d4d;
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background-color: #ff1a1a;
            transform: scale(1.05);
        }

        /* Overview Section Styles */
        .overview-box {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            margin: 1px 0;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .overview-box:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 25px rgba(255, 77, 77, 0.4);
        }

        .overview-title {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 15px;
        }

        .overview-text {
            font-size: 18px;
            color: #b3b3b3;
            line-height: 1.6;
        }

        /* Image Container Styles */
        .image-container {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px;
            overflow: hidden;
        }

        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 15px;
        }

        /* Feature Box Styles */
        .feature-box {
            background-color: #1a1a1a;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            min-height: 200px;
            height: 100%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .feature-box:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 25px rgba(255, 77, 77, 0.4);
        }

        .feature-icon {
            font-size: 40px;
            margin-bottom: 15px;
            color: #ff4d4d;
        }

        /* Subscription Plan Styles */
        .plan-box {
            background-color: #1a1a1a;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            margin: 20px 0;
            text-align: center;
            min-height: 400px;
            height: 100%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .plan-box:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 25px rgba(255, 77, 77, 0.4);
        }

        .plan-title {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 20px;
        }

        .plan-price {
            font-size: 32px;
            font-weight: bold;
            color: #ff4d4d;
            margin-bottom: 20px;
        }

        .plan-features {
            list-style-type: none;
            padding: 0;
            margin-bottom: 20px;
            text-align: left;
        }

        .plan-features li {
            font-size: 16px;
            color: #b3b3b3;
            margin-bottom: 10px;
        }

        /* Footer Styles */
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #1a1a1a;
            margin-top: 40px;
            border-top: 1px solid #333;
        }

        .footer p {
            margin: 5px 0;
            color: #b3b3b3;
            font-size: 14px;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero-container">
        <h1 class="main-title">ADAPTIFY AI</h1>
        <p class="tagline">Revolutionize Your Learning Journey with AI-Powered Assessments</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Navigation button
if st.button("Start Your Assessment", type="primary", use_container_width=True):
    navigate_to_upload()

# Main content columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <div class="overview-box">
            <h2 class="overview-title">Transform Your Educational Experience</h2>
            <p class="overview-text">
                Adaptify uses cutting-edge AI technology to create personalized learning experiences 
                that evolve with you. Our intelligent assessment system adapts in real-time to your 
                unique learning style, ensuring optimal comprehension and retention.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    try:
        image = Image.open("image.jpg")
        st.markdown(
            """
            <div class="image-container">
                <img src="data:image/jpeg;base64,{}" alt="Adaptify AI">
            </div>
            """.format(image_to_base64(image)),
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("Image not found. Please ensure the image file 'image.jpg' is in the correct location.")

# Key Features Section
st.markdown("<h2 style='text-align: center; color: #ffffff; margin: 40px 0 20px;'>Why Choose Adaptify?</h2>", unsafe_allow_html=True)

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
        "title": "Rapid Progress in Learning",
        "description": "Accelerate your learning with targeted assessments and feedback"
    }
]

for col, feature in zip([col1, col2, col3], features):
    with col:
        st.markdown(
            f"""
            <div class="feature-box">
                <div class="feature-icon">{feature['icon']}</div>
                <h3 style="color: #ffffff; margin-bottom: 10px;">{feature['title']}</h3>
                <p style="color: #b3b3b3;">{feature['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Subscription Plans Section
st.markdown("<h2 style='text-align: center; color: #ffffff; margin: 40px 0 20px;'>Choose Your Plan</h2>", unsafe_allow_html=True)

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
        ]
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
        ]
    },
    {
        "title": "Researchers",
        "price": "₹20000/month",
        "features": [
            "Advanced data analytics",
            "Custom research tools",
            "Access to raw data",
            "Collaboration",
            "Priority support"
        ]
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
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(f"Get Started - {plan['title']}", key=f"plan_{plan['title']}", use_container_width=True):
            navigate_to_upload()

# Final CTA Section
st.markdown(
    """
    <div style="text-align: center; margin: 60px 0;">
        <h2 style="color: #ffffff; margin-bottom: 20px;">Ready to Transform Your Learning?</h2>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("Get Started Now", type="primary", use_container_width=True, key="final_cta"):
    navigate_to_upload()

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
