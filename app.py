from flask import Flask, request, render_template
import google.generativeai as palm

palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
model = {
    "model": "models/chat-bison-001",
}

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/palm", methods=["GET","POST"])
def palm_flask():
    q = request.form.get("q")
    print(q)
    r = palm.chat(
        **model,
        messages=q
    )
    print(r.last)
    return(render_template("reply.html",r=r.last))

if __name__ == "__main__":
    app.run()
