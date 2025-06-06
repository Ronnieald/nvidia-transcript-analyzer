import streamlit as st
import os
import matplotlib.pyplot as plt
from collections import Counter

# Set app title
st.set_page_config(page_title="NVIDIA Earnings Call Analyzer", layout="wide")
st.title("🧠 NVIDIA Q1 2025 Earnings Call Analysis")
st.caption("Financial tone and strategic insights extracted from transcript prompt chunks.")

# Path to prompt chunk folder
CHUNKS_FOLDER = "prompts"

# Utility to parse each chunk into tone and insights
def parse_chunk(content):
    tone = []
    insights = []
    lines = content.strip().splitlines()
    current_section = None

    for line in lines:
        if line.strip().lower().startswith("tone:"):
            current_section = "tone"
            continue
        elif line.strip().lower().startswith("strategic insights:"):
            current_section = "insights"
            continue

        if current_section == "tone" and line.strip():
            tone.append(line.strip("-• "))
        elif current_section == "insights" and line.strip():
            insights.append(line.strip("-• "))

    return tone, insights

# List and sort all chunks
chunk_files = sorted([f for f in os.listdir(CHUNKS_FOLDER) if f.endswith(".txt")])

# Containers for all tones and insights
total_tones = []
all_insights = []

# Display each chunk in its own section
for chunk_file in chunk_files:
    with open(os.path.join(CHUNKS_FOLDER, chunk_file), "r", encoding="utf-8") as f:
        content = f.read()

    tone, insights = parse_chunk(content)
    total_tones.extend(tone)
    all_insights.extend(insights)

    with st.expander(f"📄 {chunk_file}", expanded=False):
        st.subheader("Tone")
        st.write(", ".join(tone) if tone else "No tone detected.")

        st.subheader("Strategic Insights")
        if insights:
            for insight in insights:
                st.markdown(f"- {insight}")
        else:
            st.write("No insights detected.")

# Display tone frequency chart
st.header("📊 Tone Frequency Across All Chunks")
tone_counts = Counter(total_tones)
if tone_counts:
    fig, ax = plt.subplots()
    ax.bar(tone_counts.keys(), tone_counts.values(), color="skyblue")
    ax.set_ylabel("Frequency")
    ax.set_xlabel("Tone")
    ax.set_title("Tone Distribution")
    st.pyplot(fig)
else:
    st.write("No tones found to chart.")

# Display summarized view of all strategic insights
st.header("🧾 Summary of Strategic Insights Across All Chunks")
if all_insights:
    for insight in all_insights:
        st.markdown(f"- {insight}")
else:
    st.write("No strategic insights found.")

