import store
# import FastAPI
from fastapi import FastAPI
# import resource to return HTML templates
from fastapi.responses import HTMLResponse

# create app
app = FastAPI()

# define route to execute get_list function
@app.get('/')
def get_list():
    return [1, 2, 3]

# define route to execute another get_list function
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>This is a web page</title>
        </head>
        <body>
            <h1>This is a web page</h1>
            <p>Hi from paragraph</p>
        </body>
    </html>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()