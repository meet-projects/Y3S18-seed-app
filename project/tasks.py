from celery import Celery
from twilio.rest import Client
import time

#Mahd's phone:
ACC_SID = "ACefef234a7dcd3cb22413db1ecab742a5"
AUTH_TOKEN = "4a6cd830f3a7b69ec5cae4fde76e34b9"
FROM = "+18647546228"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"


app = Celery('tasks', broker='redis://localhost' )

@app.task
def alert(number, flag, phone1, phone2, phone3):
	print('here')
	dest = number
	while True:
		client = Client(ACC_SID, AUTH_TOKEN)
		if flag == 2 and phone1:
			dest = phone1
		elif flag == 3 and phone2:
			dest = phone2
		elif flag == 4 and phone3:
			dest = phon3
		elif flag == 5:
			flag = 1
			dest = number
		client.messages.create(to=dest, from_=FROM, body=BODY)
		flag+=1
		time.sleep(30)

def revoke(task_id):
	app.control.revoke(task_id, terminate=True)