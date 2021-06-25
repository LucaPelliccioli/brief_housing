# coding: utf8
from flask import render_template, request, abort, redirect, url_for
import datetime
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from app import models

# C'est ici qu'on demande à notre appli flask d'acheminer toutes les demandes d'URL à la racine vers la fonction index()
# A chaque fois qu'on ouvrira un navigateur pour accéder à l'indexe, c'est cette fonction qui sera appelé
# @app.route est un décorateur de la varibale app qui va encapsuler la fonction index() et acheminer les demande vers cette fonction

def init_app(app):
    @app.route('/')
    def index():
        date = datetime.datetime.now().strftime("%x %X")
        return render_template( 'index.html', date=date)

    @app.route('/dashboard')
    def dashboard():
        models.graphique()
        date = datetime.datetime.now().strftime("%x %X")
        return render_template( 'dashboard.html', date=date)

    @app.route('/formulaire_predict')
    def formulaire_predict():
        date = datetime.datetime.now().strftime("%x %X")
        return render_template( 'formulaire_predict.html', date=date)

    @app.route('/predict', methods = ['POST', 'GET'])
    def predict():
        nop = request.form['ocean']
        mi = request.form['revenu']
        predict = models.predict(mi, nop)
        date = datetime.datetime.now().strftime("%x %X")
        return render_template( 'predict.html', date=date, nop=nop, mi=mi, predict=predict)

    @app.route('/ajout_bien', methods = ['POST', 'GET'])
    def ajout_bien():
        return render_template("Pages/formulaire_predict.html")
        
    @app.route('/modifier_bien', methods = ['POST', 'GET'])
    def modifier_bien():
        data = models.sqldata()
        return render_template("Pages/modifier_bien.html", d=data)
