from flask import Blueprint, request
from flask_expects_json import expects_json
import bookings_service as bk 

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.get('/bookings')
def find_many_bookings():
    offset = request.args.get('offset', default=0)
    limit = request.args.get('limit', default=10)
    return bk.find_many(offset, limit)
    
@bookings_bp.get('/bookings/<int:id>')
def find_one(id):
    bookings = bk.find_one(str(id))
    if bookings is None: 
        return {'message': 'La reservation demandee n\'existe pas'}, 404
    
    return bookings

@bookings_bp.post('/bookings')
@expects_json()
def create_one():
    body = request.get_json()
    return bk.create_one(body)

@bookings_bp.put('/bookings/<int:id>')
@expects_json()
def update_one(id):
  body = request.get_json()
  updated_bookings = bk.update_one(str(id), body)

  if updated_bookings is None:
    return {'message': 'La reservation demandee n\'existe pas'}, 404

  return updated_bookings

@bookings_bp.delete('/bookings/<int:id>')
def delete_one(id):
  bk.delete_one(str(id))
  return {}, 204

@bookings_bp.get('/statistics/room_type')
def get_room_type_statistics():
    statistics = bk.get_room_type_statistics()
    
    return statistics