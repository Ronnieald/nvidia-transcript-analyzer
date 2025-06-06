import os
import textwrap

def read_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_into_chunks(text, max_words=400):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

def format_prompt(chunk_text):
    prompt = f"""
You are an expert financial analyst and communication specialist.

I will provide you a transcript excerpt from NVIDIA's Q1 2025 earnings call.

Please analyze the excerpt and provide:

1. The overall tone of the speaker(s) — choose up to three descriptive words (e.g., confident, cautious, optimistic).

2. Key strategic insights conveyed in the remarks — bullet point format preferred.

Do not repeat the transcript. Focus only on tone and strategic business insights.

Transcript excerpt:
\"\"\"
{chunk_text}
\"\"\"

Your analysis:
Tone:
- 

Strategic Insights:
- 
"""
    return prompt.strip()

def main():
    transcript_path = "nvda_q1_2025.txt"  # Replace with your file path
    transcript_text = read_transcript(transcript_path)
    chunks = split_into_chunks(transcript_text, max_words=400)

    # Save prompts to files or print
    output_dir = "prompts"
    os.makedirs(output_dir, exist_ok=True)

    for i, chunk in enumerate(chunks, start=1):
        prompt_text = format_prompt(chunk)
        prompt_file = os.path.join(output_dir, f"prompt_chunk_{i}.txt")
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt_text)
        print(f"Saved prompt chunk {i} to {prompt_file}")

if __name__ == "__main__":
    main()
