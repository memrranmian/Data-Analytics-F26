import mistune
import os
import subprocess
import shutil

md_path = 'MSDSF25A007_markdown_assignment.md'
html_path = 'MSDSF25A007_markdown_assignment.html'
pdf_path = 'MSDSF25A007_markdown_assignment.pdf'

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Enable plugins if available or use basic mistune parser
markdown = mistune.create_markdown(plugins=['table', 'task_lists', 'strikethrough'])
body_html = markdown(md_content)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>RollNo_markdown_assignment</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
    @page {{
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
    }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        line-height: 1.6;
        color: #24292e;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
    }}
    h1 {{
        font-size: 26px;
        border-bottom: 2px solid #eaecef;
        padding-bottom: 8px;
        color: #1a1e22;
        margin-top: 10px;
    }}
    h2 {{
        font-size: 20px;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 6px;
        color: #2b3137;
        margin-top: 24px;
    }}
    h3 {{
        font-size: 16px;
        color: #3f4448;
        margin-top: 16px;
    }}
    hr {{
        border: none;
        border-top: 1px solid #e1e4e8;
        margin: 24px 0;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 16px 0;
    }}
    th, td {{
        border: 1px solid #dfe2e5;
        padding: 8px 12px;
        text-align: left;
    }}
    th {{
        background-color: #f6f8fa;
        font-weight: 600;
    }}
    tr:nth-child(even) {{
        background-color: #fbfcfd;
    }}
    code {{
        background-color: #f6f8fa;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 88%;
        color: #d73a49;
    }}
    blockquote {{
        margin: 16px 0;
        padding: 8px 16px;
        color: #57606a;
        border-left: 4px solid #0366d6;
        background-color: #f1f8ff;
        border-radius: 0 4px 4px 0;
    }}
    blockquote p {{
        margin: 4px 0;
    }}
    ul, ol {{
        padding-left: 24px;
    }}
    li {{
        margin-bottom: 4px;
    }}
    input[type="checkbox"] {{
        margin-right: 6px;
    }}
    img {{
        max-width: 100%;
        height: auto;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        display: block;
        margin: 16px auto;
    }}
    a {{
        color: #0366d6;
        text-decoration: none;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    .task-list-item {{
        list-style-type: none;
        margin-left: -20px;
    }}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated HTML successfully.")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
browser_path = edge_path if os.path.exists(edge_path) else chrome_path

abs_html = os.path.abspath(html_path)
abs_pdf = os.path.abspath(pdf_path)

cmd = [
    browser_path,
    '--headless',
    '--disable-gpu',
    f'--print-to-pdf={abs_pdf}',
    '--no-pdf-header-footer',
    abs_html
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Browser exit code:", res.returncode)
if os.path.exists(abs_pdf):
    print("PDF generated successfully:", abs_pdf, "Size:", os.path.getsize(abs_pdf))
else:
    print("PDF generation failed.")
