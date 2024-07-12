from flask import Flask, render_template, request
from transformers import pipeline
print("Starting.....")

app = Flask(__name__)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
