#!/usr/bin/env python3
import sys
import pdb

def trace_lines(frame, event, arg):
    if event == 'line':
        # Specify the line number where you want to start the debugger
        target_lineno = 2  # Change this to the desired line number
        if frame.f_lineno == target_lineno:
            print(f"Breaking at line {target_lineno} in {frame.f_code.co_filename}")
            pdb.set_trace()  # Start the debugger shell
    return trace_lines

def run_script(script_path):
    # Compile the script
    with open(script_path, 'r') as f:
        script_code = f.read()
    code_object = compile(script_code, script_path, 'exec')

    # Set the trace function just before executing the compiled code
    sys.settrace(trace_lines)

    # Execute the compiled code object in the current global context
    exec(code_object, globals())

    # Remove the trace function after execution
    sys.settrace(None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python python_debugger <script_to_debug.py>")
        sys.exit(1)

    script_to_debug = sys.argv[1]
    run_script(script_to_debug)
