# Streamlit-GitHub-Actions
A repo with GitHub Actions enabled to keep a website awake.

This uses actions to setup a check every few hours running the python scripts to check if the website is online, and to wake it up if it wasn't using selenium in Python.

- Workflow "Check app": "check_app.yml", it triggers a check to see if the website is online using script "check_website.py"
- Workflow "Wake up": "wake_up.yml", it calls the site to bring it back online if it was offline, using script "wake_up_streamlit.py"
