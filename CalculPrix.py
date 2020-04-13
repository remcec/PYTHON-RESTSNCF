from flask import Flask, render_template

CalculPrix = Flask(__name__)

@CalculPrix.route('/')
def index():
    return render_template('index.html')

# On pourra interroger l'API en passant par ce lien et en mettant des valeurs a la place des '<>'.
@CalculPrix.route('/API/CalculPrix/distance/<string:distance>/devise/<string:devise>', methods=['GET'])
def get_prix(distance, devise):
    PRIXFIXEKM = 0.75
    totalsimple = float(distance) * PRIXFIXEKM
    totalfinal = 0

    # Conditions pour gérer différentes devises.
    if devise == 'EUR':
        totalfinal = totalsimple
    elif devise == 'MGA':
        totalfinal = totalsimple * 4105.20
    elif devise == 'CHF':
        totalfinal = totalsimple * 1.05
    elif devise == 'USD':
        totalfinal = totalsimple * 1.09
    else :
        # On retourne un message d'erreur en utilisant le format JSON.
        return {'totalfinal' : 'PRIX INDISPONIBLE POUR LA DEVISE:'}

    # On retourne le totalfinal au format JSON, round permet d'avoir 2 chiffres après la virgules.
    return {'totalfinal' : round(totalfinal, 2)}
