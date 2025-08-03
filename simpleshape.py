#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later

import time
import pyperclip
import re
import uuid

shape_points = []
y_value = None  # Will be set from the first copied point

def extract_coords(text):
    """
    Extract x y z coordinates from a /execute ... tp @s x y z command
    """
    match = re.search(r'tp\s+@s\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)', text)
    if not match:
        return None
    x, y, z = map(float, match.groups())
    return {"x": x, "y": y, "z": z}

def format_shape_marker(label, shape, y, marker_id=None):
    """
    Format the collected shape into a BlueMap HOCON marker
    """
    marker_id = marker_id or f"shape-{uuid.uuid4().hex[:8]}"
    first = shape[0]
    
    shape_lines = "\n        ".join(f"{{ x: {p['x']}, z: {p['z']} }}" for p in shape)
    
    return f"""{marker_id}: {{
    type: "shape"
    position: {{ x: {first['x']}, y: {y}, z: {first['z']} }}
    label: "{label}"
    shape: [
        {shape_lines}
    ]
    shape-y: {y}
}}"""

def monitor_clipboard():
    print("📋 Copy Minecraft F3+C teleport commands to define a shape.")
    print("⛔ Copy 'quit' to stop and export the shape.")

    last_clipboard = pyperclip.paste()

    global y_value

    while True:
        time.sleep(0.5)
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard:
            last_clipboard = current_clipboard.strip()

            if last_clipboard.lower() == "quit":
                print("\n🛑 Stopped input.")
                break

            coords = extract_coords(last_clipboard)
            if coords:
                if y_value is None:
                    y_value = coords["y"]
                shape_points.append(coords)
                print(f"✅ Added point: x={coords['x']} z={coords['z']}")
            # silently ignore invalid entries

    if shape_points:
        label = input("\n🏷️ Enter label for the shape: ").strip() or "Unnamed Shape"
        output = format_shape_marker(label, shape_points, y_value)
        print("\n🟢 Generated BlueMap Shape Marker:\n")
        print(output)
    else:
        print("❌ No valid points collected.")

if __name__ == "__main__":
    monitor_clipboard()
