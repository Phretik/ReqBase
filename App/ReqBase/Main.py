from __init__ import create_app

app = create_app()   ##Creates the app

if __name__ == '__main__':
    app.run(debug=True)   ##Runs the app
