import tkinter as tk
from tkinter import messagebox


class MathItem:
    def get_text(self):
        return ""


class TextItem(tk.Entry, MathItem):
    def __init__(self, parent, app, width=4, font_size=18, default_text=""):
        super().__init__(
            parent,
            width=width,
            font=("Cambria Math", font_size),
            justify="center",
            relief="solid",
            bd=1
        )
        self.app = app
        if default_text:
            self.insert(0, default_text)

        self.bind("<FocusIn>", self.on_focus)
        self.bind("<Button-1>", self.on_focus)

    def on_focus(self, event=None):
        self.app.set_active_slot(self.master)

    def get_text(self):
        return self.get()


class MathSlot(tk.Frame):
    def __init__(self, parent, app, bg="white"):
        super().__init__(parent, bg=bg, bd=0, highlightthickness=0)
        self.app = app
        self.items = []

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event=None):
        self.app.set_active_slot(self)

    def add_item(self, widget):
        self.items.append(widget)
        widget.pack(in_=self, side="left", padx=3, pady=3)
        self.app.focus_first_entry(widget)

    def clear_highlight(self):
        self.config(bg="white")

    def highlight(self):
        self.config(bg="#dff1ff")

    def get_text(self):
        return "".join(
            item.get_text() if hasattr(item, "get_text") else ""
            for item in self.items
        )


class FractionItem(tk.Frame, MathItem):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        self.num_slot = MathSlot(self, app)
        self.line = tk.Frame(self, bg="black", height=2, width=70)
        self.den_slot = MathSlot(self, app)

        self.num_slot.pack(pady=(2, 1))
        self.line.pack(fill="x", padx=4)
        self.den_slot.pack(pady=(1, 2))

        self.bind("<Button-1>", lambda e: app.set_active_slot(self.num_slot))

    def get_text(self):
        return f"({self.num_slot.get_text()})/({self.den_slot.get_text()})"


class RootItem(tk.Frame, MathItem):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        self.symbol = tk.Label(self, text="√", font=("Cambria Math", 28), bg="white")
        self.content_slot = MathSlot(self, app)

        self.symbol.pack(side="left")
        self.content_slot.pack(side="left", padx=2)

        self.bind("<Button-1>", lambda e: app.set_active_slot(self.content_slot))

    def get_text(self):
        return f"sqrt({self.content_slot.get_text()})"


class PowerItem(tk.Frame, MathItem):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        self.base_slot = MathSlot(self, app)
        self.exp_slot = MathSlot(self, app)

        self.base_slot.pack(side="left", pady=(8, 0))
        self.exp_slot.pack(side="left", anchor="n")

        self.bind("<Button-1>", lambda e: app.set_active_slot(self.exp_slot))

    def get_text(self):
        return f"{self.base_slot.get_text()}^({self.exp_slot.get_text()})"


class IndexItem(tk.Frame, MathItem):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        self.base_slot = MathSlot(self, app)
        self.sub_slot = MathSlot(self, app)

        self.base_slot.pack(side="left", pady=(0, 8))
        self.sub_slot.pack(side="left", anchor="s")

        self.bind("<Button-1>", lambda e: app.set_active_slot(self.sub_slot))

    def get_text(self):
        return f"{self.base_slot.get_text()}_({self.sub_slot.get_text()})"


class EditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Math Editor")
        self.root.geometry("1300x700")
        self.root.configure(bg="white")

        self.active_slot = None
        self.all_slots = []

        title = tk.Label(root, text="Visual Math Editor", font=("Arial", 20, "bold"), bg="white")
        title.pack(pady=10)

        toolbar = tk.Frame(root, bg="white")
        toolbar.pack(pady=8)

        tk.Button(toolbar, text="Text", width=10, command=self.add_text).pack(side="left", padx=4)
        tk.Button(toolbar, text="Fraction", width=10, command=self.add_fraction).pack(side="left", padx=4)
        tk.Button(toolbar, text="Root", width=10, command=self.add_root).pack(side="left", padx=4)
        tk.Button(toolbar, text="Power", width=10, command=self.add_power).pack(side="left", padx=4)
        tk.Button(toolbar, text="Index", width=10, command=self.add_index).pack(side="left", padx=4)

        for sym in ["+", "-", "×", "÷", "=", "(", ")", "α", "β", "γ", "θ"]:
            tk.Button(toolbar, text=sym, width=5, command=lambda s=sym: self.add_symbol(s)).pack(side="left", padx=2)

        tk.Button(toolbar, text="Show Text", width=12, command=self.show_text).pack(side="left", padx=8)

        self.workspace = tk.Frame(root, bg="#f7f7f7", bd=1, relief="solid")
        self.workspace.pack(fill="both", expand=True, padx=20, pady=20)

        self.main_slot = MathSlot(self.workspace, self, bg="#f7f7f7")
        self.main_slot.pack(anchor="w", padx=20, pady=30)

        self.register_slot(self.main_slot)
        self.set_active_slot(self.main_slot)

    def register_slot(self, slot):
        self.all_slots.append(slot)

    def set_active_slot(self, slot):
        self.active_slot = slot
        for s in self.all_slots:
            s.clear_highlight()
        slot.highlight()

    def focus_first_entry(self, widget):
        if isinstance(widget, tk.Entry):
            widget.focus_set()
            return True
        for child in widget.winfo_children():
            if self.focus_first_entry(child):
                return True
        return False

    def ensure_active_slot(self):
        if self.active_slot is None:
            self.set_active_slot(self.main_slot)
        return self.active_slot

    def add_text(self):
        slot = self.ensure_active_slot()
        slot.add_item(TextItem(slot, self, width=5))

    def add_symbol(self, sym):
        slot = self.ensure_active_slot()
        slot.add_item(TextItem(slot, self, width=3, default_text=sym))

    def add_fraction(self):
        slot = self.ensure_active_slot()
        item = FractionItem(slot, self)
        self.register_slot(item.num_slot)
        self.register_slot(item.den_slot)
        slot.add_item(item)
        self.set_active_slot(item.num_slot)

    def add_root(self):
        slot = self.ensure_active_slot()
        item = RootItem(slot, self)
        self.register_slot(item.content_slot)
        slot.add_item(item)
        self.set_active_slot(item.content_slot)

    def add_power(self):
        slot = self.ensure_active_slot()
        item = PowerItem(slot, self)
        self.register_slot(item.base_slot)
        self.register_slot(item.exp_slot)
        slot.add_item(item)
        self.set_active_slot(item.base_slot)

    def add_index(self):
        slot = self.ensure_active_slot()
        item = IndexItem(slot, self)
        self.register_slot(item.base_slot)
        self.register_slot(item.sub_slot)
        slot.add_item(item)
        self.set_active_slot(item.base_slot)

    def show_text(self):
        txt = self.main_slot.get_text()
        messagebox.showinfo("Generated Text", txt if txt else "(empty)")


if __name__ == "__main__":
    root = tk.Tk()
    app = EditorApp(root)
    root.mainloop()