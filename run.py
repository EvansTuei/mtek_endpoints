from src.factory import create_app

app = create_app(None, mode="DEVELOPMENT")
app.app_context().push()
app.config['JSON_SORT_KEYS'] = False



if __name__ == "__main__":
    app.run()
#print('run')