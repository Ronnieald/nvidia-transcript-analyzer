// api/chunks.js
import fetch from 'node-fetch';

export default async function handler(req, res) {
  const baseURL = 'https://raw.githubusercontent.com/Ronnieald/nvidia-transcript-analyzer/main/prompts/';
  const files = [
    'prompt_chunk_1.txt',
    'prompt_chunk_2.txt',
    'prompt_chunk_3.txt',
    'prompt_chunk_4.txt',
    'prompt_chunk_5.txt',
    'prompt_chunk_6.txt'
  ];

  const parseAnalysis = (text) => {
    const toneMatch = text.match(/Tone:\\n- (.*)/);
    const insightsMatch = text.match(/Strategic Insights:\\n-([\\s\\S]*)/);

    const tone = toneMatch ? toneMatch[1].trim() : 'N/A';
    const insightsRaw = insightsMatch ? insightsMatch[1].trim() : '';
    const insights = insightsRaw.split('\\n').map(line => line.replace(/^-\\s*/, '').trim()).filter(Boolean);

    return { tone, insights };
  };

  try {
    const data = await Promise.all(files.map(async (file) => {
      const response = await fetch(baseURL + file);
      const text = await response.text();
      const { tone, insights } = parseAnalysis(text);
      return { file, tone, insights };
    }));

    res.status(200).json(data);
  } catch (error) {
    console.error('Error fetching chunk files:', error);
    res.status(500).json({ error: 'Failed to fetch or parse prompt chunks.' });
  }
}
