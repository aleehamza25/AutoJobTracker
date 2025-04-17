# 🚀 JobTrackr: Automated Job Scraping & Reporting Tool

JobTrackr is a Python-based end-to-end workflow automation system that scrapes job listings from websites like Indeed and LinkedIn, filters them by keyword or location, and generates PDF + Excel reports delivered straight to your inbox.

## 🔧 Features
- 🔍 Scrape jobs using Selenium & BeautifulSoup
- 📂 Organize results into Excel and PDF
- 📧 Email daily reports
- 📅 Run manually or schedule via Task Scheduler or cron
- ⚙️ Fully customizable keywords and filters

## 🛠 Stack
- Python 3
- Selenium
- BeautifulSoup
- pandas
- openpyxl
- fpdf
- smtplib / Gmail API

## 📦 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/jobtrackr.git
cd jobtrackr
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Email & Filters**
Edit `utils/config.py` and update:
- Email credentials
- Job keywords
- Location filters

4. **Run the script**
```bash
python main.py
```

## 🖼 Output
- `reports/job_report.xlsx`
- `reports/job_report.pdf`
- Email with attached reports

## 📅 Schedule Automation
Use Windows Task Scheduler or Linux cron to run `main.py` daily.

## 📜 License
MIT

## 🤝 Contribute
Pull requests welcome! Feel free to open issues to propose new features.
