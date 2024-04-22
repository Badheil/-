import datetime
import json
from apy import register_booking

def create_booking(room_name, start: datetime, end: datetime) -> str:
    print('Начинаем создание бронирования')
    booking = Booking(room_name, start, end)

    try:
        result = register_booking(booking)
    except KeyError:
        d = create_dict(booking, False, "Комната не найдена")
        return json.dumps(d, ensure_ascii=False)
    else:
        if result == True:
            d = create_dict(booking, True, "Бронирование создано")
            return json.dumps(d, ensure_ascii=False)
        
        if result == False:
            d = create_dict(booking, False, "Комната занята")
            return json.dumps(d, ensure_ascii=False)
    finally:
        print('Заканчиваем создание бронирования')


def create_dict(obj, create: bool(), msg: str())  -> dict():
    dict1 = {}
    d1 = {}

    dict1['created'] = create
    dict1['msg'] = msg
    d1['room_name'] = obj.room_name
    d1['start_date'] = obj.start_date
    d1['start_time'] = obj.start_time
    d1['end_date'] = obj.end_date
    d1['end_time'] = obj.end_time
    d1['duration'] = obj.duration
    dict1["booking"] = d1
    return dict1
    
class Booking:
    def __init__(self, room_name, start, end):
        if end < start:
            raise ValueError()
        self.room_name = room_name
        self.start = start
        self.end = end

    @property
    def start_date(self):
        return "{}-{:02}-{:02}".format(self.start.year, self.start.month, self.start.day)

    @property
    def end_date(self):
        return "{}-{:02}-{:02}".format(self.end.year, self.end.month, self.end.day)

    @property
    def start_time(self):
        return "{:02}:{:02}".format(self.start.hour, self.start.minute)

    @property
    def end_time(self):
        return "{:02}:{:02}".format(self.end.hour, self.end.minute)

    @property
    def duration(self):
        a = self.end.month * 30 * 24 * 60 + self.end.day * 24 * 60 + self.end.hour * 60 + self.end.minute
        b = self.start.month * 30 * 24 * 60 + self.start.day * 24 * 60 + self.start.hour * 60 + self.start.minute
        return a-b

a = Booking('Вагнер',   datetime.datetime(2022, 9, 1, 14),
            datetime.datetime(2022, 9, 1, 14, 15))
print(a.start_date)
print(a.end_date)
print(a.start_time)
print(a.end_time)
print(a.duration)
print(create_booking('Terrorblade',   datetime.datetime(2022, 9, 1, 14),
                     datetime.datetime(2022, 9, 1, 14, 48)))
# booking = Booking('Вагнер',   datetime.datetime(2022, 9, 1, 14),
#                  datetime.datetime(2022, 9, 1, 20, 15))


