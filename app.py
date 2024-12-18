from flask import Flask, render_template
import datetime
import subprocess
import os

app = Flask(__name__)


end_date = datetime.date(2024, 11, 30)

# @app.before_request
def check_for_updates():
    # Change to the directory where your app's code is located
    app_directory = r'D:\Harsha\git_update\update'
    os.chdir(app_directory)

    # Check for updates by pulling the latest code from Git
    try:
        subprocess.run(['git', 'fetch'], check=True)  # Fetch updates from remote
        subprocess.run(['git', 'pull'], check=True)  # Pull the latest changes
        subprocess.run(['git', 'commit', '-a', '-m', 'update'], check=True)
        subprocess.run(["git", "merge", "main", "--no-edit"], check=True)
        print("Running the updated application...")
        subprocess.run(['python', 'app.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error updating the application: {e}")


@app.before_request
def check_date():

    check_for_updates()
    print("inside check date")
    today = datetime.date.today()
    print(today)
    print(end_date)
    if datetime.date.today() > end_date:
        print(datetime.date.today())
        print(end_date)
        return "<h1>No Access to page</h1>"
        


@app.route("/")
def index():
    check_for_updates()
    return "<h1>My Name is Harsha </h1>"


if __name__ == "__main__":
    app.run(debug=True)
