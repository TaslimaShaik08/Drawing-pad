# 🎨 Drawing Pad

A simple and fun drawing application built with **Python** and **Tkinter** as a micro project for the Python Programming course.

---

## 📌 Project Description

Drawing Pad is a GUI-based application that lets you draw freely on a digital canvas using your mouse. It supports multiple brush colors, adjustable brush sizes, an eraser tool, canvas clearing, and saving your artwork.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 Color Picker | Choose any color for your brush |
| 📏 Brush Size | Adjust brush thickness using a slider (1–40) |
| ✏️ Pen Tool | Draw smooth freehand lines |
| 🧹 Eraser Tool | Erase parts of your drawing |
| 🗑️ Clear Canvas | Wipe the canvas clean (with confirmation) |
| 💾 Save Drawing | Save your artwork as a PostScript (.ps) file |
| 📍 Status Bar | Shows current tool, size, and cursor coordinates |

---

## 🧠 Concepts Used

- **Canvas Widget** — Tkinter's `Canvas` is used as the drawing surface
- **Mouse Events** — `Button-1`, `B1-Motion`, `ButtonRelease-1` track press, drag, and release
- **Color Chooser** — `tkinter.colorchooser` opens a native color dialog
- **Object-Oriented Programming (OOP)** — The app is structured as a `DrawingPad` class
- **Event Binding** — `.bind()` connects mouse actions to drawing functions
- **Loops & State** — Previous coordinates are tracked to draw continuous lines

---

## 🗂️ Project Structure

```
drawing_pad/
│
├── drawing_pad.py     # Main application source code
└── README.md          # Project documentation
```

---

## ▶️ How to Run

### Requirements
- Python 3.x (Tkinter is built-in, no extra installation needed)

### Steps

```bash
# 1. Clone or download the project
git clone https://github.com/YOUR_USERNAME/drawing-pad.git

# 2. Navigate into the folder
cd drawing-pad

# 3. Run the application
python drawing_pad.py
```

---

## 🖥️ How to Use

1. **Draw** — Click and drag the mouse on the white canvas
2. **Change Color** — Click the 🎨 Color button and pick a color
3. **Resize Brush** — Move the Size slider left (thin) or right (thick)
4. **Erase** — Click 🧹 Eraser, then drag over areas to erase
5. **Switch back to Pen** — Click ✏️ Pen
6. **Clear all** — Click 🗑️ Clear (a confirmation dialog will appear)
7. **Save** — Click 💾 Save to export as a `.ps` file

---

## 📸 Screenshot

> *(Add a screenshot of your running app here after taking one)*  
> `![Drawing Pad Screenshot](screenshot.png)`

---

## 👨‍💻 Author

- **Name:** Shaik Taslima 
- **Roll No:** 2025DCSBT11069
- **Course:** Python Programming – I Year  
- **GitHub:** [github.com/TaslimaShaik08](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is created for educational purposes as part of a college micro project assignment.
