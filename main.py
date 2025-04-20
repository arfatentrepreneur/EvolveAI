from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message["content"]
    return render_template("index.html", user_message=user_message, ai_response=reply)

if __name__ == "__main__":
    app.run(debug=True)
