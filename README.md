# 🌍 Bluemap - SimpleShape

**Bluemap - SimpleShape** is a tiny Python tool that lets you build BlueMap `shape` markers from copied Minecraft teleport commands (`F3 + C`).  
Copy your locations one by one, then export the result as a properly formatted marker to paste into your `markers.json`.

> ⚠️ We are not affiliated with BlueMap or its developers. This is an independent community utility.

---

## ✨ Features

- ✅ Clipboard monitoring
- 🧠 Parses `/execute ... tp @s x y z` commands (from F3+C)
- 🔁 Collects points for your shape
- 🛑 Stops when you copy `quit`
- 🏷️ Lets you name your shape
- 🟩 Outputs a BlueMap-compatible shape marker in HOCON format

---

## 🧾 Output Format

```hocon
shape-1234abcd: {
    type: "shape"
    position: { x: 123, y: 64, z: -321 }
    label: "My Route"
    shape: [
        { x: 123, z: -321 }
        { x: 125, z: -322 }
        { x: 130, z: -325 }
    ]
    shape-y: 64
}
```

- The `y` level is fixed from the first copied position.
- Only the `x` and `z` are used for the shape points.

---

## 🚀 How to Use

1. Run:

   ```bash
   python simpleshape.py
   ```

2. In Minecraft, press `F3 + C` to copy your position.
3. Repeat to define multiple points.
4. Copy `"quit"` to finish.
5. Enter a label when prompted.
6. The result will be printed to the terminal — copy it into your `markers.json`.

---

## 🔧 Requirements

- Python 3.6+
- `pyperclip` module:

```bash
pip install pyperclip
```

---

## ⚖ License

This project is licensed under the **GNU Affero General Public License v3.0**.

You are free to use, study, share and improve it — as long as all changes remain free and open to the community under the same license.

> See [`LICENSE`](./LICENSE) for full details.

---

## 🙅 Not Affiliated

This tool is not affiliated with BlueMap.  
BlueMap is a separate project owned and maintained by [BlueMap's developers](https://github.com/BlueMap-Minecraft/BlueMap).  
All rights to BlueMap belong to its respective creators.
