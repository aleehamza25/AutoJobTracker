def clean_job_data(raw_jobs):
    cleaned = []
    for job in raw_jobs:
        cleaned.append({
            'Title': job['title'].strip(),
            'Company': job['company'].strip(),
            'Location': job['location'].strip(),
        })
    return cleaned