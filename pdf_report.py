from fpdf import FPDF

def create_pdf_report(jobs, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Job Report", ln=True, align='C')
    for job in jobs:
        pdf.cell(200, 10, txt=f"{job['Title']} at {job['Company']} ({job['Location']})", ln=True)
    pdf.output(file_path)