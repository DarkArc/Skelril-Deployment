from datetime import datetime

date = datetime.today()

print('{:%y.%m.%d.%H.%M}'.format(date))
