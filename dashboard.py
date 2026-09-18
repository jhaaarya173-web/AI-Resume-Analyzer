import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from resume_parser import parse_resume
from ai_analyzer import analyze_resume
from history import show_history
import database
from export_report import export_report


class Dashboard:

    def __init__(self):

        self.file_path = ""

        self.root = tk.Tk()
        self.root.title("AI Resume Analyzer Dashboard")
        self.root.geometry("1200x750")
        self.root.resizable(True, True)

        # Open maximized
        self.root.state("zoomed")


        # Title
        title = tk.Label(
            self.root,
            text="AI Resume Analyzer Dashboard",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=15)


        # Upload Resume Button
        upload_btn = tk.Button(
            self.root,
            text="Upload Resume",
            width=20,
            command=self.upload_resume
        )
        upload_btn.pack(pady=10)


        # Resume Path
        self.resume_label = tk.Label(
            self.root,
            text="No Resume Selected",
            fg="blue"
        )
        self.resume_label.pack()



        # Job Description
        tk.Label(
            self.root,
            text="Paste Job Description",
            font=("Arial", 14)
        ).pack(pady=10)


        self.jd_text = tk.Text(
            self.root,
            width=90,
            height=10
        )
        self.jd_text.pack()



        # Analyze Button
        analyze_btn = tk.Button(
            self.root,
            text="Analyze Resume",
            width=20,
            command=self.analyze_resume
        )
        analyze_btn.pack(pady=15)



        # History Button
        history_btn = tk.Button(
            self.root,
            text="View History",
            width=20,
            command=show_history
        )
        history_btn.pack(pady=5)



        # Export Button
        export_btn = tk.Button(
            self.root,
            text="Export Report",
            width=20,
            command=self.export_data
        )
        export_btn.pack(pady=5)




        # Result Heading
        tk.Label(
            self.root,
            text="Analysis Result",
            font=("Arial", 14, "bold")
        ).pack()



        # Result Box
        self.result_box = tk.Text(
            self.root,
            width=90,
            height=15
        )
        self.result_box.pack()



        # Progress Bar
        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.progress.pack(pady=10)



        self.root.mainloop()



    def upload_resume(self):

        file = filedialog.askopenfilename(
            filetypes=[
                ("Resume Files", "*.pdf *.docx")
            ]
        )

        if file:

            self.file_path = file

            self.resume_label.config(
                text=file
            )



    def analyze_resume(self):

        if self.file_path == "":

            messagebox.showerror(
                "Error",
                "Please upload a resume."
            )

            return



        jd = self.jd_text.get(
            "1.0",
            tk.END
        ).strip()



        if jd == "":

            messagebox.showerror(
                "Error",
                "Please enter a Job Description."
            )

            return



        try:

            self.progress["value"] = 30
            self.root.update_idletasks()


            # Extract resume text
            data = parse_resume(
                self.file_path
            )


            self.progress["value"] = 60
            self.root.update_idletasks()


            # AI Analysis
            result = analyze_resume(
                data["resume_text"],
                jd
            )


            self.progress["value"] = 100



            output = f"""

====================================================

ATS SCORE : {result['ats_score']}/100

MATCH PERCENTAGE : {result['match_percentage']}%

----------------------------------------------------

TECHNICAL SKILLS

{", ".join(result["technical_skills"])}

----------------------------------------------------

MISSING SKILLS

{", ".join(result["missing_skills"])}

----------------------------------------------------

STRENGTHS

{result["strengths"]}

----------------------------------------------------

WEAKNESSES

{result["weaknesses"]}

----------------------------------------------------

RESUME SUMMARY

{result["resume_summary"]}

----------------------------------------------------

CANDIDATE LEVEL

{result["candidate_level"]}

----------------------------------------------------

SUGGESTIONS

{result["suggestions"]}

====================================================

"""


            self.result_box.delete(
                "1.0",
                tk.END
            )

            self.result_box.insert(
                tk.END,
                output
            )



            database.save_resume(
                data["name"],
                data["email"],
                data["phone"],
                ", ".join(
                    result["technical_skills"]
                ),
                result["ats_score"],
                result["match_percentage"],
                result["suggestions"],
                self.file_path
            )


            messagebox.showinfo(
                "Success",
                "Resume analyzed successfully!"
            )



        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )



    def export_data(self):

        report = self.result_box.get(
            "1.0",
            tk.END
        )


        if report.strip() == "":

            messagebox.showerror(
                "Error",
                "No analysis result available"
            )

            return



        export_report(report)


        messagebox.showinfo(
            "Success",
            "Report exported successfully"
        )




if __name__ == "__main__":

    Dashboard()