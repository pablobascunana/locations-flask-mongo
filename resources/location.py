from flasgger import swag_from
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from schemas.location import LocationSchema, MarkerSchema
from models.location import Location as LocationModel
from utils.constants import SWAGGER_PATH
from utils.responses import created, ok

location_schema = LocationSchema()
marker_schema = MarkerSchema()
SWAGGER_STATUS_PATH = SWAGGER_PATH + 'location/'


class Location(Resource):
    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STATUS_PATH + 'location-get.yml')
    def get(cls, user_uuid):
        locations = LocationModel.get_locations_by_user_id(user_uuid)
        return ok(location_schema.dump(locations))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STATUS_PATH + 'location-post.yml')
    def post(cls, user_uuid):
        location = location_schema.load(request.get_json(), partial=True)
        location = LocationModel.insert_or_update(location)
        return created(location_schema.dump(location))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STATUS_PATH + 'location-delete.yml')
    def delete(cls, user_uuid):
        marker = marker_schema.load(request.get_json(), partial=True)
        LocationModel.delete_marker(userId=user_uuid, marker=marker)
        return ok(location_schema.dump(LocationModel.get_locations_by_user_id(user_uuid)))
