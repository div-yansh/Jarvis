import datetime
import os
import psutil
import pyautogui as pag
import pyjokes
import pyttsx3
import smtplib
import speech_recognition as sr
import sys
import webbrowser as wb
import wikipedia


def speak(audio):
	engine = pyttsx3.init()
	engine.say(audio)
	engine.runAndWait()


def time():
	time = datetime.datetime.now().strftime("%I:%M:%S")
	speak("The time right now is")
	speak(time)


def date():
	year = str(datetime.datetime.now().year)
	month = str(datetime.datetime.now().month)
	day = str(datetime.datetime.now().day)
	speak("Today's date is")
	speak(year+" "+month+" "+day)


def wishme():
	hour = datetime.datetime.now().hour
	wish = ""
	if hour >= 6 and hour < 12:
		wish = "Good Morning"
	elif hour >= 12 and hour < 18:
		wish = "Good Afternoon"
	elif hour >= 18 and hour < 24:
		wish = "Good Evening"
	speak(wish + "Sir")
	speak("Jarvis always at your service")


def take_command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recogninzing...")
		query = r.recognize_google(audio, language="en-in")
		print(query)
		return query.lower()
	except Exception as e:
		print("Say that again please...")
		speak("Say that again please...")
		return None


def acknowledge():
	speak("Yes sir")

	
def wiki_search(query):
	query = query.replace("wikipedia", "")
	query = query.replace("search", "")
	query = query.replace("who is", "")
	query = query.replace("what is", "")
	query = query.replace("tell me about", "")

	result = wikipedia.summary(query, sentences=1)
	print(result)
	speak(result)


def get_content_email():
	speak("What shoul I write in email?")
	content = take_command()
	print(content)
	speak("Whom should I send it?")
	to = take_command()
	content = take_command()
	return content, to


def send_email(to, content):
	server = smtplib.SMTP("smtp.gmail.com", 574)
	server.ehlo()
	server.starttls()
	server.login("your mail id", "your mail password")
	server.sendmail("your mail id", to, content)
	speak("Main sent to " + to)
	print("Main sent to " + to)
	server.close()


def get_content_chrome():
	speak("which website should I open?")
	topic = take_command().lower()
	return topic


def search_chrome(topic):
	cp = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
	wb.get(cp).open_new_tab(topic+".com")
	print("Opening" + topic + ".com")
	speak("Opening" + topic + ".com")


def close():
	speak("Have a nice day sir. I am going offline")
	sys.exit()


def logout():
	print("Logging off")
	speak("Logging off")
	os.system("shutdown -l")


def restart():
	print("Restarting")
	speak("Restarting")
	os.system("shutdown /r /t 1")


def shutdown():
	print("Shutting down")
	speak("Shutting down")
	os.system("shutdown /s /t 1")


def play_song():
	song_dir = "C:\\songs"
	songs = os.listdir(song_dir)
	song = os.path.join(song_dir, songs[0])
	os.startfile(song)

def remember():
	speak("What should I remember?")
	data = take_command()
	file = open("remember.txt", 'w')
	file.write(data)
	file.close()
	speak("Okay sir, I will remember that")


def recall():
	file = open("remember.txt", 'r')
	data = file.read()
	file.close()
	speak("You told me that " + data)
	print(data)


def screenshot():
	ss_dir = os.getcwd()
	ss_name = "ss.png"
	path = os.path.join(ss_dir, ss_name)
	ss = pag.screenshot()
	ss.save(path)
	print("Screenshot taken")
	speak("screenshot taken")


def cpu():
	usage = str(psutil.cpu_percent())
	print("CPU is at "+usage+"%")
	speak("CPU is at "+usage+"%")


def battery():
	usage = str(psutil.sensors_battery().percent)
	print("Battery is at "+usage+"%")
	speak("Battery is at "+usage+"%")


def jokes():
	joke = pyjokes.get_joke()
	print(joke)
	speak(joke)
	

def main():
	wishme()
	while True:
		query = None
		while query == None:
			query = take_command()
		query = query.lower()
		query.replace("jarvis", "")

		if query == "jarvis":
			acknoledge()

		elif "date" in query and "time" in query:
			date()
			time()

		elif "date" in query:
			date()

		elif "time" in query:
			time()

		elif "offline" in query or "close" in query or "quit" in query:
			close()

		elif "wikipedia" in query or "search" in query or "who" in query \
			or "what" in query or "tell me about" in query:
			wiki_search(query)

		elif "send email" in query or "send email" in query:
			content, to = get_content_email()
			send_email(to, content)

		elif "website" in query or "chrome" in query:
			topic = get_content_chrome()
			search_chrome(topic)

		elif "logout" in query:
			logout()

		elif  "restart" in query or "start again" in query:
			restart()

		elif "shut" in query or "shutdown" in query:
			shutdown()

		elif "play song" in query:
			play_song()

		elif "remember" in query or "memorise" in query or "note" in query:
			remember()

		elif "recall" in query or "i told" in query:
			recall()

		elif "screenshot" in query:
			screenshot()

		elif "cpu" in query:
			cpu()

		elif "battery" in query or "power" in query:
			battery()

		elif "jokes" in query or "funny" in query or "comedy" in query:
			jokes()


if __name__ == "__main__":
	main()
