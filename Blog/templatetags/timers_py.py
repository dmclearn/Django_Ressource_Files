from datetime import datetime
from django import template

register = template.Library()

def format_(timedelta):
    year = timedelta/(360*24*60*60)
    month = (year%1)*12
    days = (month%1)*30
    hours = (days%1)*24
    minutes = (hours%1)*60
    seconds = (minutes%1)*60
    if year>=1:
        return f"il ya {round(year)} ans"
    elif month>=1:
        return f"il ya {round(month)} mois"    
    elif days>=1:
        return f"il ya {round(days)} jours"    
    elif hours>=1:
        return f"il ya {round(hours)} heures"    
    elif minutes>=1:
        return f"il ya {round(minutes)} minutes"    
    else:
        return f"il ya {round(seconds)} secondes"
 

@register.simple_tag
def get_timer_(date:datetime):
    start = date.timestamp()
    end = datetime.now().timestamp()
    dif = end - start
    return format_(dif)