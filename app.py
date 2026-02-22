import streamlit as st
from main_pipeline import run_analysis
import pandas as pd
import os

st.set_page_config(page_title="Climate Risk Intelligence", layout="wide")

st.title("🌍 Climate Disaster Risk Intelligence System")
st.markdown(
    "Interactive multi-agent climate risk modeling system integrating "
    "statistical validation and LLM-based interpretation."
)

# -----------------------------
# Sidebar Configuration
# -----------------------------
st.sidebar.header("⚙️ Analysis Configuration")

data_path = os.path.join("data", "emdat_raw.csv")
df = pd.read_csv(data_path, encoding="latin-1")

available_disasters = sorted(df["Disaster Type"].dropna().unique())
available_regions = sorted(df["Subregion"].dropna().unique())

region = st.sidebar.selectbox(
    "Select Region",
    available_regions
)

disaster_type = st.sidebar.selectbox(
    "Select Disaster Type",
    available_disasters
)

run_button = st.sidebar.button("Run Analysis")

# -----------------------------
# Main Execution
# -----------------------------
if run_button:

    try:
        with st.spinner("Running multi-agent climate analysis..."):
            result = run_analysis(region, disaster_type)

        st.success("Analysis Complete")

        # -----------------------------
        # Top Section: Risk + Confidence
        # -----------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Risk Assessment")
            st.markdown(f"##### 🚨 Risk Level: {result['risk_level']}")

            confidence = result.get("confidence_level", "Unknown")

            if confidence == "High":
                st.markdown("##### 🟢 Confidence: High")
            elif confidence == "Moderate":
                st.markdown("##### 🟡 Confidence: Moderate")
            elif confidence == "Low":
                st.markdown("##### 🔴 Confidence: Low")
            else:
                st.markdown("##### ⚪ Confidence: Not Available")

        # -----------------------------
        # Statistical Summary Table
        # -----------------------------
        with col2:
            st.subheader("📊 Statistical Summary")

            stats_df = pd.DataFrame({
                "Metric": [
                    "Linear Regression Slope",
                    "Linear Regression P-value",
                    "Mann-Kendall Trend",
                    "Mann-Kendall P-value",
                    "T-Test P-value"
                ],
                "Value": [
                    round(result["trend_slope"], 3) if result.get("trend_slope") is not None else None,
                    round(result["p_value"], 3) if result.get("p_value") is not None else None,
                    result.get("mk_trend"),
                    round(result["mk_p_value"], 3) if result.get("mk_p_value") is not None else None,
                    round(result["t_p_value"], 3) if result.get("t_p_value") is not None else None
                ]
            })

            st.table(stats_df)

        # -----------------------------
        # Visualization Section
        # -----------------------------
        st.subheader("📈 Trend Visualization")
        if result.get("plot_figure"):
            st.pyplot(result["plot_figure"])
        else:
            st.warning("Plot not available.")

        # -----------------------------
        # Reflection Section
        # -----------------------------
        st.subheader("🧠 Statistical Reflection")
        if result.get("reflection_notes"):
            st.write(result["reflection_notes"])
        else:
            st.info("No reflection notes available.")

        # -----------------------------
        # Final Interpretation
        # -----------------------------
        st.subheader("📌 Final Risk Interpretation")
        if result.get("interpretation"):
            st.write(result["interpretation"])
        else:
            st.info("No interpretation generated.")

    except Exception as e:
        st.error("An error occurred during analysis.")
        st.exception(e)