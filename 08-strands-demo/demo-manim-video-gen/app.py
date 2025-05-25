#!/usr/bin/env python3
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient
import os
import sys
import subprocess
from pathlib import Path

def check_and_install_packages():
    """Check and install required packages using uv"""
    required_packages = {
        "strands-agents": "latest",
        "manim": "latest",
        "mcp": "latest"
    }
    
    print("Checking and installing required packages...")
    for package, version in required_packages.items():
        try:
            # Check if package is installed
            subprocess.run(
                ["uv", "pip", "show", package],
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"Installing {package}...")
            subprocess.run(
                ["uv", "pip", "install", f"{package}=={version}"],
                check=True
            )
    print("Package installation complete!")

def print_help():
    print("\n=== Manim Video Generation Chat Interface ===")
    print("Available commands:")
    print("  /help     - Show this help message")
    print("  /example  - Show an example Manim animation")
    print("  /exit     - Exit the program")
    print("  /install  - Install required packages using uv")
    print("  /status   - Check MCP server status")
    print("\nYou can also:")
    print("  - Ask questions about Manim")
    print("  - Request specific animations")
    print("  - Get help with Manim code")
    print("  - Ask about the generated videos")
    print("\nExample questions:")
    print("  - 'How do I create a circle animation?'\n  - 'Can you show me how to animate text?'\n  - 'What's the difference between Create and Show?'\n  - 'Where are the videos saved?'")
    print("==========================================\n")

def get_example_animation():
    return """
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        self.play(Create(circle))
        self.wait(2)
"""

def ensure_output_directory():
    """Ensure the output directory exists"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def main():
    try:
        # Check and install required packages
        check_and_install_packages()
        
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        
        # Get the path to the manim_server.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        manim_server_path = os.path.join(current_dir, "src", "manim_server.py")
        os.chdir(current_dir)

        # Connect to the Manim MCP server using stdio transport
        manim_mcp_client = MCPClient(lambda: stdio_client(
            StdioServerParameters(command="uv", args=["run", manim_server_path])
        ))

        print("Checking MCP server status...")
        # Try to open the context to check if the server is running
        try:
            with manim_mcp_client:
                tools = manim_mcp_client.list_tools_sync()
        except Exception as e:
            print("\nError: MCP server is not running!")
            print("Please start the MCP server first using:")
            print("uv run start_mcp_server.py")
            sys.exit(1)

        print("Initializing Manim Video Generation Chat Interface...")
        # Now open the context for the actual chat loop
        with manim_mcp_client:
            tools = manim_mcp_client.list_tools_sync()
            agent = Agent(tools=tools)
            print("Initialization complete!")
            print_help()
            while True:
                try:
                    # Get user input
                    user_input = input("\nYou: ").strip()
                    # Handle commands
                    if user_input.lower() == '/exit':
                        print("Goodbye!")
                        break
                    elif user_input.lower() == '/help':
                        print_help()
                        continue
                    elif user_input.lower() == '/example':
                        print("\nHere's an example Manim animation:")
                        print(get_example_animation())
                        print("\nWould you like me to execute this example? (yes/no)")
                        if input().lower().startswith('y'):
                            result = agent(f"Please execute this Manim code to create a simple animation: {get_example_animation()}")
                            print("\nAgent:", result)
                        continue
                    elif user_input.lower() == '/install':
                        check_and_install_packages()
                        continue
                    elif user_input.lower() == '/status':
                        # Check status by trying to list tools
                        try:
                            manim_mcp_client.list_tools_sync()
                            print("MCP server is running")
                        except Exception:
                            print("MCP server is not running")
                        continue
                    # Process user input with the agent
                    print("\nAgent: Processing your request...")
                    result = agent(user_input)
                    print("\nAgent:", result)
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
                except Exception as e:
                    print(f"\nError: {str(e)}")
                    print("Please try again or type /help for assistance.")
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
