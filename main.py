import joblib
from flask import Flask, render_template, request, url_for

#Création d'objet de la classe Flask
app = Flask(__name__)

# Chargement du modèle
model = joblib.load('modele_foret_aleatoire.pkl')

# Exemple de valeurs pour les variables explicatives
exemple_variables = [[
    1,      # couple
    1,      # education
    25.5,   # revdispo
    150000000000, # montant
    30,     # age
    1,      # objet
    20.0,   # apport
    1,      # prt
    1,      # client
    2,      # enfant
    1,      # tempsplein
    5,      # duree
    2,      # type
    3.0,    # interet
    1,      # pel
    2,      # PCS
    3       # courant
]]


#Première route
@app.route('/')
def index():
    return render_template('index.html')

#Deuxième route
@app.route('/predict',methods=["post"])
def predict():
    # Récupérer les données du formulaire
    #request.form permet de recupérer les données du formulaires sous formre de dictionnaire
    features = [[
    int(request.form.get('couple', 0)),
    int(request.form.get('education', 0)),
    float(request.form.get('revdispo', 0.0)),
    float(request.form.get('montant', 0.0)),
    int(request.form.get('age', 0)),
    int(request.form.get('objet', 0)),
    float(request.form.get('apport', 0.0)),
    int(request.form.get('prt', 0)),
    int(request.form.get('client', 0)),
    int(request.form.get('enfant', 0)),
    int(request.form.get('tempsplein', 0)),
    int(request.form.get('duree', 0)),
    int(request.form.get('type', 0)),
    float(request.form.get('interet', 0.0)),
    int(request.form.get('pel', 0)),
    int(request.form.get('PCS', 0)),
    int(request.form.get('courant', 0))
    ]]

    prediction = model.predict(features)[0]
    prediction_proba = model.predict_proba(features)[0][1]#Proba de tombé sur 1

    return render_template('predict.html',prediction_classe = prediction,prob_defaut = prediction_proba)



if __name__=='__main__' :
    app.run(debug=True)