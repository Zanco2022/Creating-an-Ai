prompt = f"""
You are a professional resume writer. Here is a candidate’s resume data:

{json.dumps(resume_data, indent=2)}

And here is the job description:

{job_description}

Your task is to rewrite the candidate’s resume to best match the job description. Emphasize relevant experience, match keywords, and keep it concise and professional. Output the new resume as plain text, formatted with headers like SUMMARY, EXPERIENCE, SKILLS, etc.
"""
