from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


@dataclass
class Reminder:
    EMAIL: str = "email"
    SYSTEM: str = "system"
    date_time: datetime
    type: str = EMAIL

    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"
@dataclass
class Event:
    title:str
    description:str
    date_:date
    start_at:time
    end_at:time 
    reminders:list[Reminder] = []
    id:str = field(default_factory=generate_unique_id())

    def add_reminder(self,email, system, date_time, type):
        self.reminders.append(Reminder(email, system, date_time, type))
    def delete_reminder (self,reminder_index:int):
        for i in range(len(self.reminders)):
            if reminder_index == self.reminders[i]:
                self.reminders.pop(i)