#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    # Get the path to the manim_server.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    manim_server_path = os.path.join(current_dir, "src", "manim_server.py")

    # Ensure we're in the correct working directory
    os.chdir(current_dir)

    print("Starting Manim MCP Server...")
    print(f"Server path: {manim_server_path}")
    print("Press Ctrl+C to stop the server")
    
    try:
        # Start the MCP server
        subprocess.run(["uv", "run", manim_server_path])
    except KeyboardInterrupt:
        print("\nStopping MCP Server...")
        sys.exit(0)

if __name__ == "__main__":
    main() 