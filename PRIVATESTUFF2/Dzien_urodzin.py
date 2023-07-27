from datetime import datetime
import calendar

def translate_to_polish(day_name):
    match day_name:
        case 'Monday':
            return 'Poniedziałek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Środa'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'
        
date_of_birth = input('podaj datę urodzin w formacie dzień-miesiąc-rok (np. 6-1-2004): ')
day, month, year =date_of_birth.split('-')
date_of_birth = datetime(int(year),int(month),int(day))
day_name = calendar.day_name[date_of_birth.weekday()]
print(translate_to_polish(day_name))