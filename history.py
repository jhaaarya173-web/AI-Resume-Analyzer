import tkinter as tk
from tkinter import ttk
import database


def show_history():

    win = tk.Toplevel()

    win.title("Resume History")

    win.geometry("1000x500")

    tree = ttk.Treeview(
        win,
        columns=(
            "ID",
            "Name",
            "Email",
            "Phone",
            "Skills",
            "ATS",
            "Match",
            "Level"
        ),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Email", text="Email")
    tree.heading("Phone", text="Phone")
    tree.heading("Skills", text="Skills")
    tree.heading("ATS", text="ATS")
    tree.heading("Match", text="Match %")

    tree.column("ID", width=50)
    tree.column("Name", width=120)
    tree.column("Email", width=180)
    tree.column("Phone", width=120)
    tree.column("Skills", width=250)
    tree.column("ATS", width=70)
    tree.column("Match", width=80)

    tree.pack(fill="both", expand=True)

    rows = database.get_all()

    for row in rows:
        tree.insert(
            "",
            tk.END,
            values=(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )
        )