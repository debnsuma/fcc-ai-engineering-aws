# Strands Demo Projects

This repository contains a collection of demo projects showcasing the capabilities of Strands AI framework. Each project demonstrates different aspects of AI-powered automation and content generation.

## Projects

### 1. Demo Summary Speak

A text-to-speech application that uses Claude 3.7 Sonnet to read and summarize documents. The application can:
- Read and summarize text files
- Convert summaries to Markdown format
- Provide natural-sounding text-to-speech output
- Manage files and directories

[View Demo Summary Speak Documentation](demo-summary-speak/README.md)

#### Demo Recording
[![Demo Summary Speak](https://img.youtube.com/vi/J3JaXz8hOxM/0.jpg)](https://youtu.be/J3JaXz8hOxM)

### 2. Demo Manim Video Generation

A project that combines Strands Agents with Manim to generate mathematical animations through an MCP (Model Context Protocol) server. Features include:
- Interactive chat interface for animation generation
- Real-time video rendering
- Custom animation creation
- MCP server integration

[View Manim Video Generation Documentation](demo-manim-video-gen/README.md)

#### Demo Recording
[![Demo Manim Video Generation](https://img.youtube.com/vi/QQmJlI4vR80/0.jpg)](https://youtu.be/QQmJlI4vR80)

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/debnsuma/fcc-ai-engineering-aws.git
cd 08-strands-demo
```

2. Set up your Python environment:
```bash
python -m venv .venv
source .venv/bin/activate  
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Project Structure

```
08-strands-demo/
├── demo-summary-speak/     # Text-to-speech and summarization demo
├── demo-manim-video-gen/   # Mathematical animation generation demo
├── recording/             # Demo video recordings
│   ├── video_demo_summary_speak.mp4
│   └── video_demo_manim_video_gen.mp4
├── pyproject.toml         # Project dependencies
└── README.md             # This file
```

## Requirements

- Python 3.8 or higher
- uv (Python package manager)
- Strands AI framework
- Additional dependencies as specified in each project's README

## Contributing

Feel free to contribute to these demo projects by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

