import re

def parse_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Lowercase for searching without case issues
    lower_content = content.lower()

    # Find the start of the Q&A section (try multiple variants)
    qa_start = None
    for marker in ["question and answer", "questions and answers", "q&a", "q & a"]:
        idx = lower_content.find(marker)
        if idx != -1:
            qa_start = idx
            break

    # Find the end of the Operator section
    operator_end = None
    operator_match = re.search(r"operator\s*\n", content, re.IGNORECASE)
    if operator_match:
        operator_end = operator_match.end()

    # Extract Q&A and Prepared Remarks based on those indexes
    if qa_start:
        prepared = content[operator_end:qa_start].strip() if operator_end else content[:qa_start].strip()
        qa = content[qa_start:].strip()
    else:
        # fallback if no Q&A found
        prepared = content[operator_end:].strip() if operator_end else content.strip()
        qa = "Q&A section not found."

    return {
        "prepared": prepared if prepared else "Prepared Remarks not found.",
        "qa": qa
    }

if __name__ == "__main__":
    file_path = "transcripts/nvda_q1_2025.txt"

    result = parse_transcript(file_path)

    print("\n=== Prepared Remarks Preview ===\n")
    print(result["prepared"][:1000])

    print("\n=== Q&A Section Preview ===\n")
    print(result["qa"][:1000])


