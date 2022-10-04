from app import app, db, Autor
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import datetime

@app.route("/autor/add", methods=["POST"])
def autor_add():
    data = request.get_json()

    autor= Autor(
        nome = data["nome"],
        nascimento = datetime.strptime(data["nascimento"], "%Y-%m-%d")
    )
    db.session.add(autor)
    try:
        db.session.commit()
    except(IntegrityError):
        return jsonify({"error": True, "message": "Ocorreu um erro ao salvar os dados"})

    return jsonify({"error": False, "message": "Autor criado com sucesso!"})

    print(data)
    
    return jsonify({"sucesso": True})