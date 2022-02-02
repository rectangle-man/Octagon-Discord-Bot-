#MODULES
import discord
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from discord.ext import commands
from keep_alive import keep_alive
import random
import json
from matplotlib import pyplot as plt
import numpy as np
import requests
import shutil
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from io import BytesIO
from pytube import YouTube
import re
import urllib.request




#PREFIX

def get_prefix(client,message):
  with open("prefix.json","r") as f:
    prefix=json.load(f)


  return prefix[str(message.guild.id)]


  
client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_guild_join(guild):
  with open("prefix.json","r") as f:
    prefix=json.load(f)

  prefix[str(guild.id)]=")"

  with open("prefix.json","w") as f:
    json.dump(prefix,f,indent=4)

@client.event
async def on_guild_remove(guild):
  with open("prefix.json","r") as f:
    prefix=json.load(f)

  prefix.pop(str(guild.id))

  with open("prefix.json","w") as f:
    json.dump(prefix,f,indent=4)

@client.command(aliases=["cp"])
async def changeprefix(ctx, prefix):
  with open("prefix.json","r") as f:
    prefixes=json.load(f)

  prefixes[str(ctx.guild.id)]=prefix

  with open("prefix.json","w") as f:
    json.dump(prefixes,f,indent=4)

  await ctx.send(f"prefix changed to: {prefix}")

async def on_message(message):
  if message.author==client.user:
    return
  await client.process_commands(message)

  if message.content.startswith("polyplothelp"):
    await message.channel.send("\nIn order to use this command, you shall:\n**FIRST** Enter the co-ordinates of x along with the number of points you desire in the graph separated by commas.\n**SECONDLY** After hitting a space, enter the coefficients of x^0, x^1, x^2,....x^n **RESPECTIVELY** separated by commas\nfor example: Let's say you want the graph of x^2 + 2x + 3 from x in [-10,10] that contains 100 points.\nYou shall enter: \*prefix\*polyplot -10,10,100 3,2,1)\n")

    
  if message.content.startswith("octagon get prefix"):
    with open("prefix.json","r") as f:
      prefixes=json.load(f)

      await message.channel.send(f"The current prefix for the server is: {prefixes[str(message.guild.id)]}") 


#STATUS:
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Your Commands"))

#COMMANDS
@client.command(aliases=["allcap","allup","capitalise","caps"])
async def allupcase(ctx,*text):
  user=ctx.author
  s=""
  for i in text:
    for j in i:
      s+=j.upper()
    s+=" "
    
  embed=discord.Embed(color=user.color)
  embed.add_field(name="Converted Text:",value=s)
  
  await ctx.send(embed=embed)

@client.command(aliases=["alllow"])
async def alllowcase(ctx,*text):

  user=ctx.author
  s=""
  for i in text:
    for j in i:
      s+=j.lower()
    s+=" "
  
  embed=discord.Embed(color=user.color)
  embed.add_field(name="Converted Text:",value=s)
  
  await ctx.send(embed=embed)

@client.command(aliases=["VAPORWAVE" , "VW", "vw", "vape","volkswagen","Volkswagen"])
async def vaporwave(ctx,*text):
  user=ctx.author
  s=""
  for i in text:
    for j in i:
      s+=j
      s+=" "
    s+=" "
  
  embed=discord.Embed(color=user.color)
  embed.add_field(name="Converted Text:",value=s)
  # await ctx.send(f"```\n{s}\n```")
  await ctx.send(embed=embed)

@client.command(aliases=["rock paper scissors"])
async def rps(ctx,u):

  user=ctx.author

  compliments=["WOW","Yay","Congratulations!","Congrats!!"]
  boos=["LMAO","YAYYYY","Lol","xD","loser"]
  draw=["mehhh","tf?","NOOOOOOOOOOOOOOOOOOOOOOOOOO"]
  choices=["Rock","Paper","Scissors"]
  if u=="rock" or u=="rck" or u=="r" or u=="R" or u==":8110rock:" or u=="cock" or u==":8110rock:918256642452242492":
    U="Rock"
  elif u=="scissors" or u=="scis" or u=="s" or u=="S":
    U="Scissors"
  elif u=="paper" or u=="pap" or u=="ppr" or u=="p" or u=="P":
    U="Paper"
  X=random.choice(choices)

  if U=="Rock" and X=="Scissors" or U=="Scissors" and X=="Paper" or U=="Paper" and X=="Rock":
    # await ctx.send(f"You chose: {U}\nI chose: {X}\n{random.choice(compliments)}, You WON!!!")
    res=f"You chose: {U}\nI chose: {X}\n{random.choice(compliments)}, You WON!!!"
  elif U=="Rock" and X=="Paper" or U=="Scissors" and X=="Rock" or U=="Paper" and X=="Scissors":
    # await ctx.send(f"```\nYou chose: {U}\nI chose: {X}\nYou LOST!!! {random.choice(boos)}\n```")
    res=f"You chose: {U}\nI chose: {X}\nYou LOST!!! {random.choice(boos)}"
  else:
    # await ctx.send(f"```\nYou chose: {U}\nI chose: {X}\n{random.choice(draw)} It was a DRAW :(\n```")
    res=f"You chose: {U}\nI chose: {X}\n{random.choice(draw)} It was a DRAW :("

  embed=discord.Embed(color=user.color)
  embed.add_field(name="Rock,Paper,Scissors\nResults:",value=res)

  await ctx.send(embed=embed)
  
@client.command()
async def altcaps(ctx,*text):
  user=ctx.author
  s0=""
  s1=""
  for i in text:
    for j in i:
      s0+=j
    s0+=" "
  
  for i in range(len(s0)):
    if i%2==0:
      if type(s0[i])==str and s0[i]!=" ":
        s1+=s0[i].lower()
      if s0[i]==" ":
        s1+=" "
    else:
      if type(s0[i])==str and s0[i]!=" ":
        s1+=s0[i].upper()
      if s0[i]==" ":
        s1+=" "
  
  embed=discord.Embed(color=user.color)
  embed.add_field(name="Converted Text:",value=s1)
  await ctx.send(embed=embed)
  

@client.command(aliases=["peepee","dong","d","D","PENIS","PP","PEEPEE","penis"])
async def pp(ctx,user:discord.Member=None):

  if user==None:
    user=ctx.author

  s="8"
  a=random.randint(1,25)
  s+="="*a
  s+="D"


  embed=discord.Embed(color=user.color)
  embed.add_field(name=f"{user}\'s PP:", value=s)
  
  await ctx.send(embed=embed)

@client.command(aliases=["HoT","head/tails","h/t","ht","HT"])
async def headortails(ctx):
  ch=["Heads","Tails"]
  user=ctx.author 

  embed=discord.Embed(color=user.color)
  embed.add_field(name="Results:",value=f"You tossed the coin and you got:\n{random.choice(ch)}")

  await ctx.send(embed=embed)

@client.command(aliases=["repeater"])
async def repeat(ctx,*arg):
  s=""
  for i in arg:
    s+=i
    s+=" "
  
  await ctx.send(s)

@client.command(aliases=["ui","info"])
async def userinfo(ctx,user:discord.Member=None):


  a=random.randint(0,255)
  b=random.randint(0,255)
  c=random.randint(0,255)
  d=random.randint(0,255)

  s=str(a)+"."+str(b)+"."+str(c)+"."+str(d)
    




  if user==None:
    user=ctx.author

  embed=discord.Embed(color=user.color,timestamp=ctx.message.created_at)
  embed.set_author(name=f"User: {user}")
  embed.set_thumbnail(url=user.avatar_url),
  embed.set_footer(text=f'Requested by - {ctx.author}',  icon_url=ctx.author.avatar_url)

  embed.add_field(name="ID: ",value=user.id,inline=False)
  embed.add_field(name="IP Address: ",value=s,inline=False)
  # embed.add_field(name="",value="(as you can see this is *very true*)",inline=True)
  embed.add_field(name="Nick Name: ",value=user.display_name,inline=False)
  embed.add_field(name="Created at: ", value=user.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"), inline=False)
  embed.add_field(name="Joined at: ",value=user.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"),inline=False)

  await ctx.send(embed=embed)


@client.command()                   #polynomial plot 
async def polyplot(ctx,x,cof):
  
  x=x.split(",")
  cof=cof.split(",")

  x=list(map(int,x))
  cof=list(map(int,cof))

  greet=['Hold up','Hang in there','Kindly wait','Hol\'up a min','Please wait','Pls wait']

  await ctx.send(f"{random.choice(greet)}, your graph is being processed.")
  

  

  def pplot(x,cofe):
    c = len(cofe)
    y = 0
    for i in range(c):
        y += cof[i]*(x**i)
    return y

  x1 = np.linspace(x[0],x[1],x[2])
  f1=pplot(x1,cof)

  def fname(cof):
    t=''
    for i in range(len(cof)):
        c=str(cof[i])
        ex="x^"
        pow=str(i)
        s=c+ex+pow
        t+=s
        t+=" "
        if i!= len(cof)-1:
            t+='+'
            t+=" "
    return t


  


  
  plt.plot(x1,f1)
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
  plt.title(f"Graph of {fname(cof)}")
  # a="".join(random.shuffle(['a','b','c','d','e'])
  # l=['a','b','c','d','e']
  # random.shuffle(l)
  # b="".join(l)

  plt.savefig("graph.png") 

  
  with open("graph.png",'rb') as f:
    picture = discord.File(f)   
    await ctx.send(file=picture)
  os.remove("graph.png")
  x1=None
  f1=None
  plt.clf()

  return


@client.command()
async def gay(ctx,user: discord.Member=None):



  if user==None:
    user=ctx.author

  await ctx.send("This is going to be gay in 3... 2... 1...")

  try:
    url = ctx.message.attachments[0].url
  except IndexError:
    asset=user.avatar_url_as(size=512)
    data=BytesIO(await asset.read())
    pfp=Image.open(data)
    size=pfp.size
    Gay=Image.open("gay.jpg")
    Gay=Gay.resize(size)
    Image.blend(pfp,Gay,0.45).save("BlendedImage.png")



  else:
    if url[0:26] == "https://cdn.discordapp.com":
      r=requests.get(url, stream=True)
      with open("UserImage.png",'wb') as out:
        shutil.copyfileobj(r.raw,out)
  
    I1=Image.open("UserImage.png")
    Gay=Image.open("gay.jpg")

    # I1=I1.convert("P", palette=Image.ADAPTIVE, colors=24)

    size=I1.size
    Gay=Gay.resize(size)

    Image.blend(I1,Gay,0.4).save("BlendedImage.png")


  with open("BlendedImage.png",'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)

  os.remove("BlendedImage.png")
  os.remove("UserImage.png")
  
@client.command(aliases=["grey","gr"])
async def gray(ctx,user:discord.Member=None):


  if user==None:
    user=ctx.author
  
  try:
    url = ctx.message.attachments[0].url
  except IndexError:
    asset=user.avatar_url_as(size=512)
    data=BytesIO(await asset.read())
    pfp=Image.open(data)
    ImageOps.grayscale(pfp).save("GreyImage.png")

  else:
    if url[0:26] == "https://cdn.discordapp.com":
      r=requests.get(url, stream=True)
      with open("UserImage.png",'wb') as out:
        shutil.copyfileobj(r.raw,out)
      
      I1=Image.open("UserImage.png")
      ImageOps.grayscale(I1).save("GreyImage.png")
    
  with open("GreyImage.png",'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
  
  os.remove("GreyImage.png")
  os.remove("UserImage.png")

@client.command()
async def deepfry(ctx,user:discord.Member=None):

  await ctx.send("The image is being deep-fried...")

  if user==None:
    user=ctx.author
  
  try:
    url = ctx.message.attachments[0].url
  except IndexError:
    asset=user.avatar_url_as(size=512)
    data=BytesIO(await asset.read())
    pfp=Image.open(data)
    pfp=ImageEnhance.Color(pfp)
    pfp.enhance(2).save("im1.png")
    I1=Image.open("im1.png")
    I1=ImageEnhance.Contrast(I1)
    I1.enhance(12.0).save("im2.png")
    I2=Image.open("im2.png")
    ImageOps.posterize(I2,8).save("im3.png")
    I3=Image.open("im3.png")
    I3=ImageEnhance.Sharpness(I3)
    I3.enhance(4).save("im4.png")
    I4=Image.open("im4.png")
    I4.filter(ImageFilter.EDGE_ENHANCE).save("DeepFry.png")

    
    
    
    

  else:
    if url[0:26] == "https://cdn.discordapp.com":
      r=requests.get(url, stream=True)
      with open("UserImage.png",'wb') as out:
        shutil.copyfileobj(r.raw,out)
      
      I1=Image.open("UserImage.png")
      I1=ImageEnhance.Color(I1)
      I1.enhance(2).save("im1.png")
      I1=Image.open("im1.png")
      I1=ImageEnhance.Contrast(I1)
      I1.enhance(12.0).save("im2.png")
      I2=Image.open("im2.png")
      I2=ImageEnhance.Sharpness(I2)
      I2.enhance(4).save("im3.png")
      I3=Image.open("im3.png")
      I3.filter(ImageFilter.EDGE_ENHANCE).save("DeepFry.png")


      
    
  with open("DeepFry.png",'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
  
  os.remove("DeepFry.png")
  os.remove("im1.png")
  os.remove("im2.png")
  os.remove("im3.png")
  os.remove("UserImage.png")
  os.remove("im4.png")
  
  
@client.command(aliases=["rotim","rota","rot"])
async def rotate(ctx,angle):

  # if angle==None:
  #   angle=90
 
  angle=int(angle)
  try:
    url = ctx.message.attachments[0].url
  except IndexError:
    await ctx.send("No attachments found :(")
  
  else:
    if url[0:26] == "https://cdn.discordapp.com":
      r=requests.get(url, stream=True)
      with open("UserImage.png",'wb') as out:
        shutil.copyfileobj(r.raw,out)

      await ctx.send(f"Your image is being rotated by {angle} degrees...")

      I1=Image.open("UserImage.png")
      height, width=I1.size
      I1.rotate(angle,expand=True).save("RotatedImage.png")

  with open("RotatedImage.png",'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
  
  os.remove("UserImage.png")
  os.remove("RotatedImage.png")

@client.command()
async def yttomp3(ctx,*text):
  #GETTING USER INPUT
  str=""
  for i in text:
      str=str+i+"+"

  #GETTING URL
  pattern=r"watch\?v=(\S{11})"
  html=urllib.request.urlopen(f"https://www.youtube.com/results?search_query={str}")
  videoID=re.findall(pattern,html.read().decode())

  url=f"https://www.youtube.com/watch?v={videoID[0]}"
  myvid=YouTube(url)
  streams=myvid.streams.filter(only_audio=True)
  myvid=myvid.streams.get_by_itag(140)

  myvid.download(filename=f"{myvid.title}.mp3")
 
  if(myvid.filesize<=8388608):
    with open(f"{myvid.title}.mp3",'rb') as f:
      audio = discord.File(f)
      await ctx.send(file=audio)
  else:
    await ctx.send("File too large :(\n(pls buy me nitro ;) )")
  
  os.remove(f"{myvid.title}.mp3")

@client.command()
async def yttomp4(ctx,*text):
  #GETTING USER INPUT
  str=""
  for i in text:
      str=str+i+"+"

  #GETTING URL
  pattern=r"watch\?v=(\S{11})"
  html=urllib.request.urlopen(f"https://www.youtube.com/results?search_query={str}")
  videoID=re.findall(pattern,html.read().decode())

  url=f"https://www.youtube.com/watch?v={videoID[0]}"
  myvid=YouTube(url)
  myvid=myvid.streams.get_lowest_resolution()
  # myvid=myvid.streams.get_by_itag(140)

  myvid.download(filename=f"{myvid.title}.mp4")
 
  if(myvid.filesize<=8388608):
    with open(f"{myvid.title}.mp4",'rb') as f:
      audio = discord.File(f)
      await ctx.send(file=audio)
  else:
    await ctx.send("File too large :(\n(pls buy me nitro ;) )")
  
  os.remove(f"{myvid.title}.mp4")

@client.command()
async def hlp(ctx):
  hlp=" **COMMAND LIST**\n**allupcase:** converts all the text to uppercase\n**alllowcase:** converts all the text to lowercase\n**vaporwave:** converts the text in v a p o r w a v e format\n**altcaps:** converts all the text in aLteRnAtElY cApPeD tExT\n**headortails:** returns randomly generated head or tails\n**pp:** retrieves a potential pictorial representation of your penis\n**repeat:** repeats the text written after the command\n**changeprefix:** changes the bot's prefix to the entered symbol\n**userinfo:** gives the information about the user\n**rps:** play a game of rock, paper and scissors\n**polyplot:** use this command to plot a polynomial of any degree on a cartesian plane (type polyplothelp to get more specifics)\n**gay:** converts the attached image to gay (The attached image should have a bit depth of 24). If no picture is attached, it will convert the mentioned user to gay. If no user is mentioned, it will convert you to gay O_O\n**gray:** this will convert the attached image to a greyscale image. If no image is attached, it will convert ur pfp to a greyscale image. If a user is mentioned, it will convert his/her pfp to a greyscale image\n**deepfry:** this will deepfry the attached image. If no image is attached, it will deepfry the user's pfp. If a user is mentioned, it will deepfry the mentioned user's pfp\n**rotate:** this will rotate the attached image by the angle that you have mentioned (in degrees)\n**yttomp3:** This will convert a youtube video to an mp3 file. You have to type the search query and the first video in the result will be converted.\n(more commands to come in the future)\n**yttomp4:** This will convert a youtube video to an mp4 file. You have to type the search query and the first video in the result will be converted\n**FIND THE BOT'S PREFIX BY TYPING \"gravy get prefix\"**"

  await ctx.send(hlp)






keep_alive()
client.run(os.environ['TOKEN'])

