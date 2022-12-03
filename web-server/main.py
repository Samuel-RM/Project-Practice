import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get():
    return [1,2,3,4,5,]
 

@app.get('/contact', response_class=HTMLResponse)
def get():
    return """
        <h1>Hola Mundo</h1>
        <P>Hola soy una pagina creada por un weon</p>
    """



def run(): 
    store.get_categories()

if __name__ == '__main__':
    run()