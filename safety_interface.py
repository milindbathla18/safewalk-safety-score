import streamlit as st

# -------------------------------
# Safety Score Calculation
# -------------------------------
def calculate_safety_score(lighting, path_length, security, footfall):
    # Normalize inputs
    lighting_norm = lighting / 10
    security_norm = security / 10
    footfall_norm = footfall / 10

    # Normalize path length (assume max 2000m)
    path_norm = 1 - min(path_length / 2000, 1)

    # Weights
    score = (
        lighting_norm * 0.30 +
        security_norm * 0.30 +
        footfall_norm * 0.20 +
        path_norm * 0.20
    )

    return round(score * 100, 2)


# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="SafeWalk - Safety Score", layout="centered")

st.title("🚶 SafeWalk – Route Safety Score")
st.subheader("Safety-aware navigation prototype")

# Location inputs
start_location = st.text_input("📍 Start Location")
end_location = st.text_input("🎯 Destination")

st.markdown("### Route Safety Factors")

lighting = st.slider("💡 Lighting Quality (0 = dark, 10 = very bright)", 0, 10, 5)
path_length = st.number_input("📏 Path Length (meters)", min_value=50, max_value=2000, value=500)
security = st.slider("👮 Security Presence (0 = none, 10 = high)", 0, 10, 5)
footfall = st.slider("👥 Footfall (0 = isolated, 10 = crowded)", 0, 10, 5)

if st.button("🔍 Calculate Safety Score"):
    if start_location and end_location:
        score = calculate_safety_score(lighting, path_length, security, footfall)

        st.markdown("---")
        st.metric("🔐 Safety Score", f"{score} / 100")

        # Risk category
        if score >= 70:
            st.success("🟢 Low Risk Route")
        elif score >= 40:
            st.warning("🟡 Medium Risk Route")
        else:
            st.error("🔴 High Risk Route")

    else:
        st.error("Please enter both start and destination locations.")
