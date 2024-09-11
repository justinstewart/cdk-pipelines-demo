from flask import Blueprint, jsonify

from .schemas import IndexResponse

blueprint = Blueprint('index', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    return jsonify(IndexResponse(
        links=dict(
            pets='/pets',
            owners='/owners'
        )
    ).dict())
