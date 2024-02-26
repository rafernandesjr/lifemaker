from flask import Blueprint, jsonify
from models.character import Character  # Importando o modelo Character

character_bp = Blueprint('character', __name__)

characters = []  # Lista para armazenar personagens (apenas para exemplo)

@character_bp.route('/characters', methods=['GET'])
def list_characters():
    # Exemplo de uso do modelo Character
    if not characters:
        return jsonify({'message': 'Não há personagens cadastrados'}), 404
    return jsonify([vars(character) for character in characters])

@character_bp.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    # Procura o personagem pelo ID
    character = next((char for char in characters if char.id == id), None)
    if character:
        return jsonify(vars(character))
    else:
        return jsonify({'message': 'Personagem não encontrado'}), 404

@character_bp.route('/characters', methods=['POST'])
def create_character():
    # Exemplo de criação de um novo personagem
    new_character = Character(id=len(characters) + 1, name='Novo Personagem')
    characters.append(new_character)
    return jsonify(vars(new_character)), 201

@character_bp.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    for i, character in enumerate(characters):
        if character.id == id:
            character.name = 'Novo nome'
            characters[i].name = 'Novo nome'
            return jsonify(vars(character))
    return jsonify({'message': 'Personagem não encontrado'}), 404

@character_bp.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    for i, character in enumerate(characters):
        if character.id == id:
            characters.remove(character)
            return jsonify({'message': 'Personagem excluído'}), 200
    return jsonify({'message': 'Personagem não encontrado'}), 404
