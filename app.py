import streamlit as st
import os
import re

# Path to prompt chunk folder
PROMPT_FOLDER = "prompts"

def parse_analysis(text):
    """Extract Tone and Strategic Insights from the analysis text."""
    tone_match = re.search(r"Tone:\n- (.*)", text)
    insights_match = re.search(r"Strategic Insights:\n-([\s\S]*)", text)
    
    tone = tone_match.group(1).strip() if tone_match else "N/A"
    insights_raw = insights_match.group(1).strip() if insights_match else ""
    
    # Split insights by line, remove empty entries
    insights = [line.strip("- ").strip() for line in insights_raw.splitlines() if line.strip()]
    return tone, insights

def load_prompt_chunks(folder):
    """Load all prompt chunk files and parse their content."""
    chunks = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                tone, insights = parse_analysis(content)
                chunks.append({
                    "filename": filename,
                    "tone": tone,
                    "insights": insights,
                })
    return chunks

def main():
    st.title("NVIDIA Q1 2025 Earnings Call Analysis")
    st.write("Analysis of tone and strategic insights from transcript prompt chunks.")

    chunks = load_prompt_chunks(PROMPT_FOLDER)
    for chunk in chunks:
        st.header(chunk["filename"])
        st.subheader("Tone")
        st.write(chunk["tone"])
        st.subheader("Strategic Insights")
        if chunk["insights"]:
            for i, insight in enumerate(chunk["insights"], 1):
                st.markdown(f"{i}. {insight}")
        else:
            st.write("No insights found.")
        st.markdown("---")

if __name__ == "__main__":
    main()
