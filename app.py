from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    projects = [
        {"title": "Proyek A", "desc": "Deskripsi singkat proyek A", "link": "#"},
        {"title": "Proyek B", "desc": "Deskripsi singkat proyek B", "link": "#"},
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
