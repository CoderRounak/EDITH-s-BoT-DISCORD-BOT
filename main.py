import os
import discord
import requests
import json
import random
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

pickup_lines=["I have lost my number. Can i have yours?","Will you be my homework, caz i wanna do you on a desk!"," I hope you know CPR, because you just took my breath away!","If you were a vegetable, you’d be a ‘cute-cumber.’","Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you.","I never believed in love at first sight, but that was before I saw you.","Are you a magician? It’s the strangest thing, but every time I look at you, everyone else disappears.","I think there’s something wrong with my phone. Could you try calling it to see if it works?","I always thought happiness started with an ‘h,’ but it turns out mine starts with ‘u.’","I believe in following my dreams. Can I have your Instagram?","If you were a song, you’d be the best track on the album.","Is your name Google? Because you have everything I’m searching for.","Your hand looks heavy—can I hold it for you?","Are you a time traveler? Because I absolutely see you in my future.","What does it feel like to be the most gorgeous girl in the room?","I don’t know your name, but I’m sure it’s as beautiful as you are. I’m Edith.","If beauty were time, you’d be eternity.","Would you mind giving me a pinch? You’re so cute, I must be dreaming.","Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.","Kiss me if I’m wrong but, dinosaurs still exist, right?"," I’m not currently an organ donor, but I’d be happy to give you my heart.","You must be a hell of a thief, because you managed to steal my heart from across the room.","Did it hurt when you fell from heaven?"]
sad_words = ["sad","sed","sedd","sadfife","sedlife", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
"Cheer up!Everything will be alright!",
"Hang in there. Its just time...it will pass by",
"You are a great person, have faith in yourself!"]

wassup_reply = ["Everything's alright","CLOUDS!","HEAVEN!","Your great great grandfather!","My bloodpressure caz am talking to you"]

quiz=["Which city is called the CITY OF JOY?","Which animals are ancestors of dog?","Which city is called the PINK CITY"]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg=message.content
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    
    if message.content.startswith("$help"):
        await message.channel.send("$help - command list \n $hello - hello back \n $wassup - diff answers to the question what's up\n $inspire - gives a motivational quote \n $pickupline - tells you a random pickup line")
    
    if message.content.startswith("$wassup"):
        await message.channel.send(random.choice(wassup_reply))
    if message.content.startswith("$askmeaquiz"):
        await message.channel.send(random.choice(quiz))


    if msg.startswith("$inspire"):
      quote=get_quote();
      await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith("$pickupline"):
        await message.channel.send(random.choice(pickup_lines))
keep_alive()
client.run(os.getenv('TOKEN'))


