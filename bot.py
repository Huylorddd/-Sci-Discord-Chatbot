import discord
import requests
import json
import random

# There're 2 prefix that need to be ADDED [1] and [2] I've marked inside the code.

###########################################################
###################### FUNCTION PART ######################

def get_game():
  API_KEY = '// NEED TO PUT YOUR API KEY HERE //'  ## <<----------------- YOU NEED TO APPLY "RAWG_API_KEY" TO USE '$game' function !!  [1]
  # For more info, please check https://rawg.io/apidocs
  
  randompage = random.randint(1, 10000) # I think the number of games is more than this (btw i think this's good enough)
  response = requests.get(f'https://api.rawg.io/api/games?page={randompage}&page_size=1&key={API_KEY}')  
  json_data = json.loads(response.text)
  return '---' + json_data['results'][0]['name'] + '---\n' + 'Release Date: ' + json_data['results'][0]['released'] + '\n' + 'Rating: ' + str(json_data['results'][0]['rating']) + '\n' + json_data['results'][0]['background_image']

def get_wiki():
  response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
  json_data = json.loads(response.text)
  return '---' + json_data['title'] + '---\n' + json_data['extract']

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_anime():
  response = requests.get('https://api.jikan.moe/v4/random/anime')
  json_data = json.loads(response.text)
  return '---' + json_data['data']['title'] + '---\n' + '---' + json_data['data']['title_japanese'] + '---\n' + json_data['data']['synopsis'] + json_data['data']['url']

def guess_number():
  guess = (random.randint(1, 10))
  return guess

great_words = ['YEAH', 'YESSS', 'YESS', 'YES', 'DAMN', 'DAMNN', 'COOL']
great_words_back = ['Ohhh, what\'s up, Onii-chan?',
                   'How\'s it going, Onii-chan?',
                   'Eyyy, what\'s are you doing, Onii-chan?',
                   'Onii-chan, I am so proud of you!',
                   'Onii-chan, I am so happy for you!']

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'mad', 'upset']
encouragement = ['Don\'t worry, Onii-chan! I am here for you!',
                  'I am always here for you, Onii-chan!',
                  'Onii-chan, I think you are a great person!',       
                  'Onii-chan, I gonna eat all your problem >:P',
                  'Onii-chan, I love you!']

greetings = ['hello Sci', 'hi Sci', 'hey Sci', 'sup Sci', 'yo Sci']
greet_back = [', I miss youuuuuuu T.T', ', I\'m hereeeee :3', ', I wanna punch you in the faceee! hehe >:D']

goodbye = ['bye Sci', 'goodbye Sci', 'see you Sci', 'cya Sci', 'laters Sci']
goodbye_back = ['Sayounara, Onii-chan!',
                'Onii-chan, I will be waiting for you!',
                'Onii-chan, I will be here for you!']

############################################################
######################## MAIN PART #########################
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

##--------- FOR CHOICE EVENTS -----------## 
    if message.content.startswith('$help'):
      await message.channel.send('Onii-chan, I can help you with:\n\n' +
                                 '  $game - get a random game\n' +
                                 '  $anime - get a random anime\n' +
                                 '  $wiki - get a random topic from Wikipedia\n' +
                                 '  $meme - get a random meme\n' +
                                 '  $number - guess a number from 1 to 10')

    if message.content.startswith('$game'):
      await message.channel.send('Onii-chan, this game maybe proper for you :3\n\n' + get_game())
    
    if message.content.startswith('$anime'):
      await message.channel.send('Wanna watch some anime with me?\nI\'ve found this.\n\n' + get_anime())
    
    if message.content.startswith('$wiki'):
      await message.channel.send('Onii-chan, I think this topic is cool to read :3\n\n' + get_wiki())

    if message.content.startswith('$meme'):
      await message.channel.send('Onii-chan, I think this meme is kinda fun :3\n' + get_meme())
      
    if message.content.startswith('$number'):
      await message.channel.send('Onii-chan, this is my guess number: ' + str(guess_number()))

##--------- FOR CHATTING EVENTS -----------##  
    if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(encouragement))
      
    if any(word in message.content for word in greetings):
      await message.channel.send('Onii-chan' + random.choice(greet_back))
      
    if any(word in message.content for word in great_words):
      await message.channel.send(random.choice(great_words_back))
      
###########################################################
####################### CLIENT PART #######################
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('DISCORD BOT TOKEN') ## <<-------------------------- PUT YOUR DISCORD BOT TOKEN HERE (Discord Dev Portal)  [2]


## 'Sci' functions:
##     - $help:  get a list of commands
##     - $game:  automatically get a random game from RAWG API
##     - $wiki:  automatically get a random topic from Wikipedia API
##     - $meme:  automatically get a random meme from Meme API
##     - $anime: automatically get a random anime from Jikan API
##     - $number: guess a random number from 1 to 10

## 'Sci' talks:
##     - greetings:  (greetings, greet_back)
##     - encouragement: (sad_words, encouragement)
##     - goodbye: (goodbye, goodbye_back)

