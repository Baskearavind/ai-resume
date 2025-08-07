from flask import Blueprint, render_template, request
from app.resume_parser import extract_text_from_resume
from app.job_matcher import match_resume_with_jobs

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['resume']
        if uploaded_file.filename != '':
            resume_text = extract_text_from_resume(uploaded_file)
            job_matches = match_resume_with_jobs(resume_text)
            return render_template('result.html', matches=job_matches)
    return render_template('index.html')
