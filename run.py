from app import Config, create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=Config.PORT)
