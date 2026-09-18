from tkinter import filedialog
from tkinter import messagebox


def export_report(report):

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt")
        ]
    )

    if file:

        with open(file, "w", encoding="utf-8") as f:
            f.write(report)

        messagebox.showinfo(
            "Success",
            "Report exported successfully"
        )