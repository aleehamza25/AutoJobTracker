# jobtrackr/main.py
from scraper.indeed_scraper import scrape_indeed_jobs
from parser.html_parser import clean_job_data
from reports.excel_report import create_excel_report
from reports.pdf_report import create_pdf_report
from automation.email_sender import send_email_with_attachment
from utils.config import config

def main():
    raw_jobs = scrape_indeed_jobs(config['query'], config['location'])
    jobs = clean_job_data(raw_jobs)

    excel_path = config['report_paths']['excel']
    pdf_path = config['report_paths']['pdf']

    create_excel_report(jobs, excel_path)
    create_pdf_report(jobs, pdf_path)

    send_email_with_attachment(
        subject='Daily Job Report',
        body='Attached are today’s scraped jobs.',
        to_email=config['recipient_email'],
        attachments=[excel_path, pdf_path],
        smtp_config=config['smtp']
    )

if __name__ == '__main__':
    main()
