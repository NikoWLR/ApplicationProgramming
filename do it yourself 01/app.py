from flask import Flask, jsonify, request
from http import HTTPStatus

# defines app
app = Flask(__name__)

# instructions list
instructions = []

# get all instructions
@app.route('/instructions', methods=['GET'])
def get_instructions():
    return jsonify({'data': instructions})

# get a specific instruction by id
@app.route('/instructions/<int:instruction_id>', methods=['GET'])
def get_instruction(instruction_id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == instruction_id), None)

    if instruction:
        return jsonify(instruction)

    return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND

# add a new instruction
@app.route('/instructions', methods=['POST'])
def create_instruction():
    data = request.get_json() #input from user
    name = data.get('name')
    description = data.get('description')
    steps = data.get('steps')
    tools = data.get('tools')
    cost = data.get('cost')
    duration = data.get('duration')

    instruction = {
        'id': len(instructions) + 1, # id number depends on list length
        'name': name,
        'description': description,
        'steps': steps,
        'tools': tools,
        'cost': cost,
        'duration': duration
    }

    instructions.append(instruction) # add entry to list

    return jsonify(instruction), HTTPStatus.CREATED

@app.route('/instructions/<int:instruction_id>', methods=['PUT'])
def update_instruction(instruction_id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == instruction_id), None)
    # if instruction not found
    if not instruction:
        return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND
    # otherwise ask for input
    data = request.get_json()

    instruction.update(
        {
            'name': data.get('name'),
            'description': data.get('description'),
            'steps': data.get('steps'),
            'tools': data.get('tools'),
            'cost': data.get('cost'),
            'duration': data.get('duration')
        }
    )

    return jsonify(instruction)

# deleting an instruction
@app.route('/instructions/<int:instruction_id>', methods=['DELETE'])
def delete_instruction(instruction_id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == instruction_id), None)
    # if instruction not found return message
    if not instruction:
        return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND
    # otherwise delete
    instructions.remove(instruction)

    return '', HTTPStatus.NO_CONTENT

# run script
if __name__ == '__main__':
    app.run()