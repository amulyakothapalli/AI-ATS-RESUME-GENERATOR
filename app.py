from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Generate Resume
@app.route('/generate', methods=['POST'])
def generate():

    name = request.form['name']
    job_role = request.form['job_role']
    skills = request.form['skills']
    education = request.form['education']
    projects = request.form['projects']
    experience = request.form['experience']

    resume = f"""
==================================================
                    {name.upper()}
==================================================

TARGET ROLE
--------------------------------------------------
{job_role}

PROFESSIONAL SUMMARY
--------------------------------------------------
Motivated and detail-oriented aspiring professional 
with strong knowledge in {skills}. Passionate about 
technology, problem-solving, and creating impactful 
projects. Quick learner with excellent communication 
and teamwork abilities.

TECHNICAL SKILLS
--------------------------------------------------
{skills}

EDUCATION
--------------------------------------------------
{education}

PROJECTS
--------------------------------------------------
{projects}

EXPERIENCE
--------------------------------------------------
{experience}

ACHIEVEMENTS
--------------------------------------------------
- Built ATS-Friendly Resume Generator using Python & Flask
- Developed responsive web application
- Worked on real-world projects and internships
- Strong understanding of Python development

DECLARATION
--------------------------------------------------
I hereby declare that the above information is true 
to the best of my knowledge.

==================================================
        ATS FRIENDLY RESUME GENERATED
==================================================
"""

    return render_template('result.html', resume=resume)

# Run App
if __name__ == '__main__':
    app.run(debug=True)