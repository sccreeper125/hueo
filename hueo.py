from datetime import datetime
import random
from sense_hat import SenseHat
import os
import pygame
import sys
import time
from guizero import App, Picture, TextBox
import glob
import urllib.request
import socket
import subprocess
from pygame.locals import *
import pychromecast



pygame.init()
pygame.mixer.init()
fairydust = pygame.mixer.Sound("Fairydust.wav")
cymbal = pygame.mixer.Sound('CymbalCrash.wav')
dieroll = pygame.mixer.Sound('dieroll.wav')
cointoss = pygame.mixer.Sound('cointoss.wav')
computerbeeps = pygame.mixer.Sound('ComputerBeeps.wav')




sense = SenseHat()
def main():
     Q = ['Ask me anything', 'What do ya want?']
     r = input(random.choice(Q))
     if "date" in r:
          now = datetime.now()
          print ('%s/%s/%s' % (now.day, now.month, now.year))
          main()
     if "time" in r:
          now = datetime.now()
          print ('%s:%s:%s' % (now.hour, now.minute, now.second))
          main()
     if "temperature" in r:
          temp = sense.get_temperature()
          print(" %s°C" % (temp))
          main()
     if "pressure" in r:
          press = sense.get_pressure()
          print("%smillibars" % (press))
          main()
     if "humidity" in r:
          humid = sense.get_humidity()
          print("The humidity is %s%" % (humid))
          main()
     if "shutdown" in r:
          qa = input("Are you sure you want to shut down this PC? Y/N")
          if qa == "Y" or "y":
               os.system("sudo shutdown")
               print("This PC will shutdown in one minute")
               exit()
          if qa == "N" or"n":
               main()
     if "/show_message" in r:
          qa = input("text")
          sense.show_message(qa)
          main()
     if "calculator" in r:
          print("Use the number pad")
          num1 = input("1st number?")
          op = input("Operation?")
          num2 = input("2nd number?")
          num1 = int(num1)
          num2 = int(num2)
          if op == "*":
               no = num1 * num2
               print("%s * %s = %s" % (num1, num2, no))
               main()
          if op ==  "+":
               no = num1 + num2
               print("%s + %s = %s" % (num1, num2, no))
               main()
          if op == "-":
               no = num1 - num2
               print("%s - %s = %s" % (num1, num2, no))
               main()
          if op == "/":
               no = num1 / num2
               print("%s - %s = %s" % (num1, num2, no))
               main()
          
     if "crystal ball" in r:
          stupid = input("Ask me a yes or no question")
          yn = ['Yes', 'No']
          print("What does the ball say?")
          time.sleep(1)
          fairydust.play()
          print(random.choice(yn))
          main()
     if "joke" in r:
          jokes = ['What do vampires sing on New years eve? Old Fang Syne', 'Where does Tarzan by his clothes from? A jungle sale!', 'What do you call a dinosaur with one eye? A Do-you-think-he-saw-us!', 'Why is the sky so high? So birds wont bump their heads!', 'Whats green and only comes out on Febuary the 29th? A leapfrog!', 'Whats a cows favourite party game? Moosical chairs!', 'Whats the best birthday present in the world? A broken drum, you cant beat it!']  
          cymbal.play()
          print(random.choice(jokes))
          main()
     if "die" in r:
          print('Rolling a six sided dice')
          dieroll.play()
          time.sleep(1)
          print(random.randint(1, 6))
          main()
     if "toss a coin" in r:
          ht = ['Heads', 'Tails']
          print('Tossing a coin')
          cointoss.play()
          time.sleep(1)
          print(random.choice(ht))
          main()
     if "random number" in r:
          print('Generating random number')
          computerbeeps.play()
          time.sleep(1)
          print(random.randint(0, 1000))
          main()
     if "display a image" in r:
          imgsrc = input('Image name, include extension e.g. myimage.png') 
          imgsrctxt = imgsrc + ' - Hueo'
          white = (255, 255, 255)
          w = 640
          h = 480
          img  = pygame.image.load(imgsrc)
          screen = pygame.display.set_mode((w, h))
          screen.fill((white))
          pygame.display.set_caption(imgsrctxt)
          running = 1

          while running:
              screen.fill((white))
              screen.blit(img,(0,0))
              pygame.display.flip()
          while True: # main game loop
              for event in pygame.event.get():
                  if event.type == QUIT:
                      pygame.quit()
                      sys.exit()
                      main()

     if "list of files" in r:
          filext = input('Extension e.g. png')
          print(glob.glob("/home/pi/Documents/PythonProjects/HueoAI/*." + filext))
          main()
     if "ip adress" in r:
          ip = socket.gethostbyname(socket.getfqdn())
          print(ip)
          main()
     if "username" in r:
               verb = [ 'Annoying', 'Happy', 'Active','Calm','Obedient','Loud','Quiet','Wonderful','Beautiful','Sleepy','Swift']
               adjective = ['Purple','Orange','Red','Blue','Yellow','Turqoise','Green','Brown','Smiling','Frowning', 'Fat', 'Nerdy']
               noun = ['Cow','Chicken','Piegon','Magpie','Raspberry','Computer','Pencil','Lightbulb','Mouse','Meerkat','Teddy','Bunny','Flamingo','Seagull','Puppy']

               print('Generating username...')
               computerbeeps.play()
               time.sleep(1)
               print('%s%s%s' % (random.choice(verb),random.choice(adjective),random.choice(noun)))
               main()
     if "exit" in r:
          exit()
     if 'password' in r:
          chars = 'abcdefghijklmnopqrstuvwxyz12345678910'

          length = input('Password length?')
          length = int(length)
          password = ' '
          for i in range(length):
               password += random.choice(chars)
          print('Generating password...')
          computerbeeps.play()
          time.sleep(1)
          print(password)
          main()
     if "pi" in r:
          pi =  math.pi()
          print('This is pi:%s' % (pi))
     if "what can you do" in r:
          print("I can do lots of things!")
     if "edit" in r:
          print("What would you like to do?")
          print("1.Write to a file/create")
          print("2.Read a file")
          print("3.Exit")
          a = raw_input("1,2 or 3")

          if a == "1":
               name = raw_input("What would you like to call your file?")
               name = name + ".txt"
               text = raw_input("File text")
               f = open(name, "w")
               f.write(str(text))
               f.close()
               main()

          if a == "2":
               name = raw_input("What is your file's name?")
               f = open(name, "r")
               print(f.read())
               f.close()
               main()

          if a == "3":
               main()
     if "cast" in r:
          device_name_hueo = input("What device would you like to cast to?")
          audio_input_hueo = input("What audio would you like to cast e.g. https://example.com/example.mp3 (.mp3 only, only supports web urls)")
          chromecasts = pychromecast.get_chromecasts()
          cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_name_hueo)
          mc = cast.media_controller
          mc.play_media(audio_input_hueo, 'audio/mp3')
          mc.block_until_active
          main()
          mc.play()
     if "internet isn't working" in r:
          print(":(")
          
     
          
          
          
          
     else:
          print("I can't do that!")
          main()
          
main()
