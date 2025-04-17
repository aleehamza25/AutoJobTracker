import pandas as pd

def create_excel_report(jobs, file_path):
    df = pd.DataFrame(jobs)
    df.to_excel(file_path, index=False)