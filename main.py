from fasthtml.common import *

app, rt = fast_app()


@rt("/")
def get():
    return Div(
        P(r'{
            "Description": "Fichier de vérification de la propriété du domaine pour Microsoft 365 : placer dans la racine du site web",
            "Domain": "dsgsdgsdgsd.up.railway.app",
            "Id": "f58a1e05-6512-4491-9510-7b16670249fe"
        }'), hx_get="/change")


serve()
