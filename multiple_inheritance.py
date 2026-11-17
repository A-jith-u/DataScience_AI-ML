class Animal:
    def eat(self):
        print("Animal eat")

class Walks:
    def walks(self):
        print("walks")

class Dog(Animal,Walks):
    def bark(self):
        print("Barks..")

dog=Dog()
dog.eat()
dog.bark()
dog.walks()


class Camera:
    def take_photo(self):
        print("Capturing photos")

class Call:
    def make_call(self):
        print("Calling")

class Smart_phone(Camera,Call):
    def internet(self):
        print("Browsing Internet")

phone=Smart_phone()
phone.take_photo()
phone.internet()
phone.make_call()


class MediaPlayer:
    def play_video(self):
        print("Playing video")

class InternetDevice:
    def connect_wifi(self):
        print("Connected to wifi")

class SmartTv(MediaPlayer,InternetDevice):
    def change_channel(self):
        print("Changing TV channel")

tv=SmartTv()
tv.change_channel()
tv.connect_wifi()
tv.play_video()

