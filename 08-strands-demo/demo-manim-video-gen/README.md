# Manim Video Generation with Strands Agents

This project demonstrates how to use Strands Agents with Manim to generate mathematical animations through an MCP (Model Context Protocol) server.

## Demo Recording

[![Demo Manim Video Generation](https://img.youtube.com/vi/QQmJlI4vR80/0.jpg)](https://youtu.be/QQmJlI4vR80)

## Prerequisites

Before running this project, ensure you have the following installed:

1. Python 3.8 or higher
2. uv (Python package manager)
3. Manim (with all its dependencies)
4. Strands Agents
5. MCP package

## Installation

1. Clone this repository:
```bash
git clone https://github.com/debnsuma/fcc-ai-engineering-aws.git
cd 08-strands-demo/demo-manim-video-gen
```

2. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install the required packages using uv:
```bash
uv pip install strands-agents manim mcp
```

## Project Structure

```
demo-manim-video-gen/
├── app.py              # Main application file (chat interface)
├── start_mcp_server.py # Script to start the MCP server
├── src/
│   └── manim_server.py # MCP server implementation
└── output/            # Directory for generated videos
    └── manim_tmp/     # Temporary directory for Manim files
```

## Usage

### 1. Start the MCP server (Terminal 1)
In your project directory, run:
```bash
uv run start_mcp_server.py
```
This will launch the Manim MCP server and keep it running.

### 2. Start the chat application (Terminal 2)
Open a new terminal in the same directory and run:
```bash
uv run app.py
```
The chat interface will check for the MCP server and connect to it.

### 3. Interact with the chat interface
- Use `/help` for available commands
- Use `/example` to see and run a sample Manim animation
- Use `/status` to check if the MCP server is running
- Use `/install` to (re)install required packages using uv
- Use `/exit` to quit

### 4. Find your generated videos
All generated videos will be saved in the `output/manim_tmp/` directory.

## Example Animation

The default example creates a simple animation of a blue circle. The Manim code is defined in `app.py`:

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        self.play(Create(circle))
        self.wait(2)
```

## Demo Video

Watch the demo video to see the application in action:
[Demo Manim Video Generation](https://youtu.be/QQmJlI4vR80)

## Customizing Animations

1. Make sure the MCP server is running:
```bash
uv run start_mcp_server.py
```
2. In a new terminal, start the application:
```bash
uv run app.py
```
3. Ask the agent to create specific animations or modify existing ones
4. Your custom animation will be generated in the output directory

## Troubleshooting

- If you encounter Manim-related errors:
  - Ensure Manim is properly installed: `uv pip install manim`
  - Check if all Manim dependencies are installed
  - Verify the MANIM_EXECUTABLE environment variable if using a custom Manim installation
- If you encounter MCP server errors:
  - Ensure the MCP package is installed: `uv pip install mcp`
  - Make sure the MCP server is running in a separate terminal
  - Use the `/status` command in the chat app to check server status
- If you encounter package installation issues:
  - Try running `/install` command in the application
  - Or manually install packages: `uv pip install strands-agents manim mcp`

## Cleanup

The application automatically creates temporary directories for Manim files. These are stored in the `output/manim_tmp` directory. You can safely delete this directory when you're done with the generated videos.

## Development

1. Make your changes to the code
2. Start the MCP server:
```bash
uv run start_mcp_server.py
```
3. In a new terminal, run the application:
```bash
uv run app.py
```

The application will automatically handle package dependencies and ensure everything is properly installed.

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 