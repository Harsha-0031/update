from flask import Flask, render_template
import datetime

app = Flask(__name__)

end_date = datetime.date(2024, 11, 14)

@app.before_request
def check_date():
    print("inside check date")
    today = datetime.date.today()
    print(today)
    print(end_date)
    if datetime.date.today() > end_date:
        print(datetime.date.today())
        return "<h1>No Access to page</h1>"

@app.route("/")
def index():
    return "<h1>Full access to web app</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)