# Markdown Language Assignment-01: Personal Data Science Profile

**Course:** Data Analytics (MS Data Science - 2025)  
**Institution:** Punjab University College of Information Technology (PUCIT), University of the Punjab, Lahore  
**Student Name:** Muhammad Imran Mian  
**Roll Number:** `MSDSF25A007`  

---

## 📌 Project Overview & Assignment Objectives

This repository contains the complete submission for **Markdown Language Assignment-01**. The purpose of this assignment is to produce a personal Data Science portfolio document demonstrating mastery of standard and extended Markdown syntax, structured technical communication, and document formatting.

### What Was Asked to Do

As outlined in the official assignment specification (`MARKDOWN LANGUAGE ASSIGNMENT-01.pdf`), the task required creating a personal Data Science profile document following strict requirements across 9 distinct sections:

1. **Submission Format:** A source Markdown file named `<RollNo>_markdown_assignment.md` (`MSDSF25A007_markdown_assignment.md`) and an exported formatted PDF (`MSDSF25A007_markdown_assignment.pdf`).
2. **Part A — My Personal Profile (About Me):**
   - At least 100 words covering full name, degree/program, semester, university (PUCIT), hometown (Lahore), personal interests, reasons for pursuing Data Science, and future career goals.
   - Demonstration of Markdown headings, **bold text**, *italic text*, and `inline code`.
3. **Part B — My Technology Skills:**
   - A structured Markdown table containing at least 8 technologies with columns: `Technology`, `My Level`, `Experience`, and `I Use It For`.
4. **Part C — My Learning Journey:**
   - An ordered list with at least 8 chronological learning milestones.
   - A multi-tier nested list categorizing skill areas (Programming, Data Science, Machine Learning, MLOps).
5. **Part D — My Favorite Technologies:**
   - In-depth descriptions of 5 favorite technologies (Name, Why liked, Where used, and valid hyperlinks to official documentation).
6. **Part E — Project Checklist:**
   - A task list (`- [x]` and `- [ ]`) showcasing actual project phases for an applied Data Science project (*Predictive Equipment Maintenance & Quality Assurance Pipeline*).
7. **Part F — Mathematical Expressions:**
   - At least 2 formatted mathematical expressions (Arithmetic Mean formula and Classification Accuracy matrix formula with parameter definitions).
8. **Part G — Blockquotes:**
   - At least 2 inspirational quotations on Data Science, Big Data, and AI formatted with Markdown blockquote syntax (`>`).
9. **Part H — Image:**
   - Embedding of a relevant, high-resolution visual figure representing modern Data Science dashboards with descriptive alt text (`![Alt](url)`).
10. **Part I — Checklist of Markdown Features Practiced:**
    - A comprehensive checklist verifying at least 12 distinct Markdown features practiced throughout the assignment.

---

## 📂 Repository File Structure

```text
├── MSDSF25A007_markdown_assignment.md    # Primary assignment Markdown file
├── MSDSF25A007_markdown_assignment.pdf   # Exported, publication-ready PDF document
├── MSDSF25A007_markdown_assignment.html  # Intermediate HTML file with MathJax styling
├── data_science_dashboard.png           # Visual asset embedded in Part H
├── convert_to_pdf.py                    # Python automation script for Markdown-to-PDF rendering
├── requirements.txt                     # Project dependencies and environment packages
└── README.md                            # Project documentation and assignment walkthrough
```

---

## 🛠️ How to Re-generate the PDF

If you make any updates to `MSDSF25A007_markdown_assignment.md`, you can automatically re-render the styled PDF by executing:

```bash
python convert_to_pdf.py
```

This uses `mistune` for parsing the Markdown content and runs headless Microsoft Edge/Chrome to compile an A4-sized PDF with LaTeX MathJax equation rendering.

---

## 👤 Author Profile & Social Links

- **GitHub:** [@memrranmian](https://github.com/memrranmian)
- **Hugging Face:** [@mimranmian](https://huggingface.co/mimranmian)
- **Program:** MS Data Science (Fall 2025 Entry), PUCIT, Lahore
