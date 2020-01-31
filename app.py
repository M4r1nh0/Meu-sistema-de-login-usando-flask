# coding: utf-8

from flask import Flask, render_template, request

app = Flask("projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="Daniel Marinho"),200

@app.route("/tipoget")
def ir_get():
	return render_template("get.html"), 200
@app.route("/tipopost")
def ir_post():	
	return render_template("post.html"), 200

@app.route("/receber/", methods=['GET', 'POST'])
def receber():
	if request.method == "GET":
		return u"Estou no tipo GET!<br>Nome: {}<br>Idade: {}".format(request.args.get("nome"),request.args.get("idade")), 200
	elif request.method == "POST":
		return u"Estou no tipo POST!<br>Nome: {}<br>Idade: {}".format(request.form["nome"],request.form["idade"]), 200

@app.route("/informacao/")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def info(nome = None, idade = None):
    return u"Nome: {}<br>idade: {}".format(nome, idade),200

app.run(host="0.0.0.0",port=5000,debug=True)