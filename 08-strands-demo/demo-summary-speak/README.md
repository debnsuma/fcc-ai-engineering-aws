# Demo Summary Speak

This project demonstrates the use of Strands AI to create a text-to-speech application that can read and summarize documents using Claude 3.7 Sonnet.

## Demo Recording

[![Demo Summary Speak](https://img.youtube.com/vi/J3JaXz8hOxM/0.jpg)](https://youtu.be/J3JaXz8hOxM)

## Features

- Read and summarize text files
- Convert summaries to Markdown format
- Text-to-speech functionality with natural voice output
- File management capabilities (read, write, list directories)

## Prerequisites

- Python 3.8 or higher
- Strands AI framework
- Bedrock access with Claude 3.7 Sonnet model
- Required Python packages (specified in pyproject.toml)

## Project Structure

```
demo-summary-speak/
├── app.py              # Main application file
├── docs/              # Directory containing input documents
└── results/           # Directory for output files (created automatically)
```

## Usage

1. Place your text files in the `docs` directory
2. Run the application:
   ```bash
   python app.py
   ```
3. The application will:
   - Read the specified file
   - Generate a summary
   - Save the summary in Markdown format
   - Speak the summary using natural voice

## Configuration

The application uses the following configuration:
- Model: Claude 3.7 Sonnet
- Max tokens: 64000
- Output format: Markdown
- Voice: Natural-sounding TTS

## Example

The application can process files like `chapter10.txt` and generate both a written summary in `results/chapter10.md` and an audio version of the summary.

## Demo Video

Watch the demo video to see the application in action:
[Demo Summary Speak Video](https://youtu.be/J3JaXz8hOxM)
