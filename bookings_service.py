from bookings_db import bookings_db 

def find_many(offset: int, limit: int):
    return list(bookings_db.values())

def find_one(id: str):
    bookings = bookings_db.get(str(id))
    return bookings if bookings else None

def create_one(new_booking):

    if(data_validation(new_booking) and all_fields(new_booking) and price_not_negative(new_booking) and room_type_is_valide(new_booking)):

        new_id = str(int(max(bookings_db.keys())) + 1)
        
        new_booking['bookings_id'] = new_id
        
        bookings_db[new_id] = new_booking

        return new_booking
    
    else:
        return {'message' : 'les données sont incorectes'}, 400

def update_one(id:str, booking):
  booking_in_db = bookings_db.get(id)

  if booking_in_db is None:
    return None
  
  if(data_validation(booking) and all_fields(booking) and price_not_negative(booking) and room_type_is_valide(booking)):

    booking['booking_id'] = id

    bookings_db[id] = booking

    return booking
  
  else: 
    return {'message' : 'les données sont incorectes'}, 400

def delete_one(id:str):
  booking = bookings_db.get(id)
  if booking is None:
    return None

  bookings_db.pop(id)

def get_room_type_statistics():
   
    room_type_counts = {
        "SINGLE": 0,
        "DELUXE": 0,
        "SUITE": 0
    }

    
    for booking in bookings_db.values():
        
        if not booking["is_cancelled"]:
            room_type = booking["room_type"]
            
            if room_type in room_type_counts:
                room_type_counts[room_type] += 1

    return room_type_counts
  

def data_validation(body):
    for key in body:
        if(key != 'user_id' and key != 'start_date' and key != 'end_date' and key != 'is_cancelled' and key != 'is_paid' and key != 'price' and key != 'room_type'):
            return False
        else:
            return True

def all_fields(body):
    fields = ['user_id', 'start_date', 'end_date', 'is_cancelled', 'is_paid', 'price', 'room_type']

    for field in fields:
        value = body.get(field)
        if value is None:
            return False
    
    return True

def price_not_negative(body):
    price = body.get('price')

    if price < 0:
        return False
    else:
        return True

def room_type_is_valide(body):
    room_type = body.get('room_type')

    if(room_type != "SINGLE" and room_type != "DELUXE" and room_type != 'SUITE'):
        return False
    else:
        return True
