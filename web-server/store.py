import requests

"""Usaremos Platzi FAke Store API como Api de pruebas y requets como libreria
para para interactuar con las APIs"""

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)

    """
    Aqui solicitamos a un api su contenido en formato de texto, este nos dara
    como resultaod un uotput en formato de strig
    """

    print(type(r.text))
    # Verificamos que efectivamente con r.text nos decuelve en fonmato de string lo solicitado a la api

    categoria = r.json()
    
    """
    Nosotros ocumapos la informacion como una lista, algo
    que nos permita pasarle filtos de contenido y la funcion 
    r.json() lo obtenemos en formato de lista con diccionarios dentro
    """

    for cate in categoria:
        print(cate['name'])

