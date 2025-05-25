from flask import Flask, render_template, request, redirect
from mood import detect_mood
import csv
from datetime import datetime

app = Flask(__name__)

# Save journal entry to CSV
def save_entry(text, mood):
    with open('journal.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), text, mood])

# Load past entries
def load_entries():
    try:
        with open('journal.csv', newline='', encoding='utf-8') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['entry']
    mood = detect_mood(text)
    save_entry(text, mood)
    return render_template('index.html', mood=mood)

@app.route('/history')
def history():
    entries = load_entries()
    return render_template('history.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
