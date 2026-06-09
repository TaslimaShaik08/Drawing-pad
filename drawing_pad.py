import tkinter as tk
from tkinter import colorchooser, messagebox


class DrawingPad:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Drawing Pad")
        self.root.resizable(True, True)

        # Drawing state
        self.prev_x = None
        self.prev_y = None
        self.brush_color = "#000000"
        self.brush_size = 5
        self.tool = "pen"  # pen or eraser

        self.setup_ui()
        self.bind_events()

    # ──────────────────────────────────────────────
    # UI Setup
    # ──────────────────────────────────────────────
    def setup_ui(self):
        """Build toolbar and canvas."""
        # ── Toolbar ──
        toolbar = tk.Frame(self.root, bg="#2b2b2b", pady=6)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Color picker button
        self.color_btn = tk.Button(
            toolbar, text="🎨 Color", bg=self.brush_color, fg="white",
            font=("Arial", 11, "bold"), relief=tk.FLAT,
            padx=10, pady=4, cursor="hand2",
            command=self.choose_color
        )
        self.color_btn.pack(side=tk.LEFT, padx=8)

        # Brush size label + slider
        tk.Label(toolbar, text="Size:", bg="#2b2b2b", fg="white",
                 font=("Arial", 10)).pack(side=tk.LEFT, padx=(10, 2))
        self.size_slider = tk.Scale(
            toolbar, from_=1, to=40, orient=tk.HORIZONTAL,
            bg="#2b2b2b", fg="white", highlightthickness=0,
            troughcolor="#555", sliderrelief=tk.FLAT,
            command=self.update_size
        )
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT, padx=4)

        # Pen / Eraser toggle
        self.pen_btn = tk.Button(
            toolbar, text="✏️ Pen", bg="#4caf50", fg="white",
            font=("Arial", 11, "bold"), relief=tk.FLAT,
            padx=10, pady=4, cursor="hand2",
            command=self.use_pen
        )
        self.pen_btn.pack(side=tk.LEFT, padx=8)

        self.eraser_btn = tk.Button(
            toolbar, text="🧹 Eraser", bg="#2b2b2b", fg="white",
            font=("Arial", 11, "bold"), relief=tk.FLAT,
            padx=10, pady=4, cursor="hand2",
            command=self.use_eraser
        )
        self.eraser_btn.pack(side=tk.LEFT, padx=4)

        # Clear button
        tk.Button(
            toolbar, text="🗑️ Clear", bg="#e53935", fg="white",
            font=("Arial", 11, "bold"), relief=tk.FLAT,
            padx=10, pady=4, cursor="hand2",
            command=self.clear_canvas
        ).pack(side=tk.LEFT, padx=8)

        # Save button
        tk.Button(
            toolbar, text="💾 Save", bg="#1976d2", fg="white",
            font=("Arial", 11, "bold"), relief=tk.FLAT,
            padx=10, pady=4, cursor="hand2",
            command=self.save_canvas
        ).pack(side=tk.RIGHT, padx=8)

        # ── Status bar ──
        self.status_var = tk.StringVar(value="Ready — start drawing!")
        status_bar = tk.Label(
            self.root, textvariable=self.status_var,
            bg="#1e1e1e", fg="#aaaaaa",
            font=("Arial", 9), anchor=tk.W, padx=8
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # ── Canvas ──
        self.canvas = tk.Canvas(
            self.root, bg="white", cursor="crosshair",
            width=900, height=600
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

    # ──────────────────────────────────────────────
    # Event Bindings
    # ──────────────────────────────────────────────
    def bind_events(self):
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.update_status)

    # ──────────────────────────────────────────────
    # Drawing Logic
    # ──────────────────────────────────────────────
    def on_press(self, event):
        """Record starting point."""
        self.prev_x = event.x
        self.prev_y = event.y

    def on_drag(self, event):
        """Draw a smooth line as the mouse moves."""
        if self.prev_x is None:
            return

        color = "white" if self.tool == "eraser" else self.brush_color
        size = self.brush_size * 2 if self.tool == "eraser" else self.brush_size

        self.canvas.create_line(
            self.prev_x, self.prev_y, event.x, event.y,
            fill=color, width=size,
            capstyle=tk.ROUND, smooth=True
        )
        self.prev_x = event.x
        self.prev_y = event.y

    def on_release(self, event):
        """Reset previous position on mouse release."""
        self.prev_x = None
        self.prev_y = None

    def update_status(self, event):
        tool_label = "Eraser" if self.tool == "eraser" else "Pen"
        self.status_var.set(
            f"{tool_label}  |  Size: {self.brush_size}  |  X: {event.x}, Y: {event.y}"
        )

    # ──────────────────────────────────────────────
    # Toolbar Actions
    # ──────────────────────────────────────────────
    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Brush Color",
                                      color=self.brush_color)
        if color[1]:
            self.brush_color = color[1]
            self.color_btn.config(bg=self.brush_color)
            self.use_pen()

    def update_size(self, val):
        self.brush_size = int(val)

    def use_pen(self):
        self.tool = "pen"
        self.pen_btn.config(bg="#4caf50")
        self.eraser_btn.config(bg="#2b2b2b")
        self.canvas.config(cursor="crosshair")

    def use_eraser(self):
        self.tool = "eraser"
        self.eraser_btn.config(bg="#ff7043")
        self.pen_btn.config(bg="#2b2b2b")
        self.canvas.config(cursor="dotbox")

    def clear_canvas(self):
        if messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the canvas?"):
            self.canvas.delete("all")
            self.status_var.set("Canvas cleared — start fresh!")

    def save_canvas(self):
        """Save the canvas drawing as a PostScript file."""
        try:
            filename = "my_drawing.ps"
            self.canvas.postscript(file=filename, colormode="color")
            messagebox.showinfo(
                "Saved!",
                f"Drawing saved as '{filename}'\n(Open with any PostScript viewer or Inkscape)"
            )
            self.status_var.set(f"Drawing saved as {filename}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingPad(root)
    root.mainloop()
