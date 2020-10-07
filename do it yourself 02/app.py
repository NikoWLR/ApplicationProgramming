
from flask import Flask
from flask_restful import Api

from resources.instruction import InstructionListResource
from resources.instruction import InstructionResource
from resources.instruction import InstructionPublishResource

app = Flask(__name__)
api = Api(app)

# API connections
api.add_resource(InstructionListResource, '/instructions')
api.add_resource(InstructionResource, '/instructions/<int:instruction_id>')
api.add_resource(InstructionPublishResource, '/instructions/<int:instruction_id>/publish')

# run script
if __name__ == '__main__':
    app.run(port=5000, debug=True)
