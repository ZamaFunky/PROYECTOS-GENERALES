from fastapi import FastAPI, Path, Query

app=FastAPI()

@app.get("/")#decorador, sirve para definir la ruta
@app.get("/home")
def inicio():
    return {"Saludo":"hola"}
