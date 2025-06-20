# the 'entry point' for the app

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(app.config['PORT']), debug=True)
