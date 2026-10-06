import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "streamlit",
    "fastapi",
    "docker",
    "git",
    "github",
    "nlp",
    "natural language processing",
    "computer vision",
    "html",
    "css",
    "javascript",
]


def detect_skills(resume_text):
    detected_skills = []

    text = resume_text.lower()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            detected_skills.append(skill)

    return detected_skills


JOB_ROLES = {
    "Data Scientist": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "sql",
        "scikit-learn",
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "scikit-learn",
        "pytorch",
        "tensorflow",
        "docker",
    ],

    "Data Analyst": [
        "python",
        "pandas",
        "numpy",
        "sql",
    ],

    "NLP Engineer": [
        "python",
        "nlp",
        "natural language processing",
        "deep learning",
        "pytorch",
    ],

    "Backend / ML API Developer": [
        "python",
        "fastapi",
        "docker",
        "git",
        "github",
    ],

    "AI Engineer": [
        "python",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "pytorch",
        "tensorflow",
    ],
}


def suggest_roles(detected_skills):
    role_scores = {}

    detected_skills_lower = [
        skill.lower() for skill in detected_skills
    ]

    for role, required_skills in JOB_ROLES.items():

        matched_skills = 0

        for skill in required_skills:
            if skill.lower() in detected_skills_lower:
                matched_skills += 1

        score = matched_skills / len(required_skills) * 100

        role_scores[role] = round(score, 2)

    sorted_roles = sorted(
        role_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_roles




def get_missing_skills(detected_skills, role):
    detected_skills_lower = [
        skill.lower() for skill in detected_skills
    ]

    required_skills = JOB_ROLES.get(role, [])

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in detected_skills_lower:
            missing_skills.append(skill)

    return missing_skills