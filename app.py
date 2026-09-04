from flask import Flask, render_template, request

app = Flask(__name__)

skills = [
    "python",
    "java",
    "html",
    "css",
    "javascript",
    "sql",
    "flask",
    "react",
    "machine learning",
    "artificial intelligence",
    "data analysis",
    "numpy",
    "pandas"
]


@app.route("/", methods=["GET", "POST"])
def index():
    matched_skills = []
    missing_skills = []
    score = None

    if request.method == "POST":
        resume = request.form["resume"].lower()
        job_description = request.form["job_description"].lower()

        required_skills = []

        for skill in skills:
            if skill in job_description:
                required_skills.append(skill)

        for skill in required_skills:
            if skill in resume:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        if len(required_skills) > 0:
            score = round(
                (len(matched_skills) / len(required_skills)) * 100,
                2
            )
        else:
            score = 0

    return render_template(
        "index.html",
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)