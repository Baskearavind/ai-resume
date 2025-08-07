from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_jobs = [
    {"title": "Software Engineer", "description": "Python, Flask, REST APIs, SQL"},
    {"title": "Data Scientist", "description": "Python, Pandas, Machine Learning, TensorFlow"},
    {"title": "Frontend Developer", "description": "HTML, CSS, JavaScript, React"},
]

def match_resume_with_jobs(resume_text):
    jobs = [job['description'] for job in sample_jobs]
    corpus = [resume_text] + jobs
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    results = []
    for i, score in enumerate(scores):
        results.append({
            'title': sample_jobs[i]['title'],
            'score': round(score * 100, 2)
        })
    return sorted(results, key=lambda x: x['score'], reverse=True)
