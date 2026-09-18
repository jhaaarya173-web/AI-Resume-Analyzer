# from resume_parser import parse_resume
#
# data = parse_resume("resume.pdf.docx")
#
# print(data)

# from resume_parser import parse_resume
# from ai_analyzer import analyze_resume
#
# data = parse_resume("resume.pdf.docx")
#
# job_description = """
# Python Developer
#
# Skills Required:
# Python
# SQLite
# Pandas
# Machine Learning
# Tkinter
# """
#
# result = analyze_resume(
#     data["resume_text"],
#     job_description
# )
#
# print(result)
#
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Test Window")
# root.geometry("400x300")
#
# label = tk.Label(root, text="Tkinter Working")
# label.pack()
#
# root.mainloop

# import tkinter as tk
#
# class LoginWindow:
#
#     def __init__(self):
#
#         self.root = tk.Tk()
#         self.root.title("AI Resume Analyzer")
#         self.root.geometry("450x350")
#
#         tk.Label(
#             self.root,
#             text="AI Resume Analyzer",
#             font=("Arial",18,"bold")
#         ).pack()
#
#         self.root.mainloop()
#
#
# LoginWindow()


import database
print("Database loaded")