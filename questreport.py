from discord_webhook import DiscordWebhook, DiscordEmbed
import mysql.connector as mariadb
import time



area = ''
webhookurl = 'https://discordapp.com/api/webhooks/'


#Pokemon 
def quest_mon(monid,mon,shiny,typeid,formid):
 mariadb_connection = mariadb.connect(user='', password='', database='', host='')
 cursor = mariadb_connection.cursor()
 query = ("select CONVERT(pokestop.name USING ascii) as pokestopname,pokestop.latitude,pokestop.longitude from pokestop inner join trs_quest on pokestop.pokestop_id = trs_quest.GUID where quest_pokemon_id ="+monid+" and quest_pokemon_form_id ="+typeid+" and ST_CONTAINS(ST_GEOMFROMTEXT('POLYGON(("+area+"))'), point(pokestop.latitude, pokestop.longitude))")
 cursor.execute(query)
 name = cursor.fetchall()
 
 if not name:
  print ("no quests for "+mon)
 else:
   
  #convert data into string
  res =[tuple(str(ele) for ele in sub) for sub in name]
 
  webhook = DiscordWebhook(url=webhookurl)
 
  # create embed object for webhook 
 
  research = ''
  for stop in res: 
 
   research += ('['+stop[0]+'](''https://www.google.com/maps/search/?api=1&query='''+stop[1]+','+stop[2]+')'+'\n') 
 
  embed = DiscordEmbed(title= shiny+mon+' Field Research'+shiny, description=research, color=16777011)
  embed.set_thumbnail(url='https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_'+monid+'_'+formid+'.png') 



  # add embed object to webhook
  webhook.add_embed(embed)
  webhook.execute()
  time.sleep(2)

#Items
def quest_item(itemid,item,sprite):
 mariadb_connection = mariadb.connect(user='', password='', database='', host='')
 cursor = mariadb_connection.cursor()
 query = ("select CONVERT(pokestop.name USING ascii) as pokestopname,pokestop.latitude,pokestop.longitude,trs_quest.quest_task,trs_quest.quest_item_amount from pokestop inner join trs_quest on pokestop.pokestop_id = trs_quest.GUID where quest_item_id = "+itemid+" and ST_CONTAINS(ST_GEOMFROMTEXT('POLYGON(("+area+"))'), point(pokestop.latitude, pokestop.longitude))")
 cursor.execute(query)
 name = cursor.fetchall()
 
 
 if not name:
  print ("no quests for "+item)
 else:
   
  #convert data into string

  res =[tuple(str(ele) for ele in sub) for sub in name]
  
  webhook = DiscordWebhook(url=webhookurl)
 
  # create embed object for webhook 
 
  research = ''
  new_str = ''

  for stop in res: 
   research += ('['+stop[0]+'](''https://www.google.com/maps/search/?api=1&query='''+stop[1]+','+stop[2]+')'+' - '+stop[3]+' - Amount:'+stop[4]+'\n')
   new_str = ('['+stop[0]+'](''https://www.google.com/maps/search/?api=1&query='''+stop[1]+','+stop[2]+')'+' - '+stop[3]+' - Amount:'+stop[4]+'\n')

   if len(research)> 1950:
    print ("larger then 2048 breaking up")
    nlines = research.count('\n')
    print (nlines)
    embed = DiscordEmbed(title= item+' Field Research', description=research, color=4390656)
    embed.set_thumbnail(url=sprite) 
    #add embed object to webhook
    webhook.add_embed(embed)
    webhook.execute()
    research = ''
    time.sleep(2)
  embed = DiscordEmbed(title= item+' Field Research', description=research, color=4390656)
  embed.set_thumbnail(url=sprite) 
  #add embed object to webhook
  webhook.add_embed(embed)
  webhook.execute()
  research = ''
  time.sleep(2)


#Stardust
def quest_stardust(itemid,item,sprite):
 mariadb_connection = mariadb.connect(user='', password='', database='', host='')
 cursor = mariadb_connection.cursor()
 query = ("select CONVERT(pokestop.name USING ascii) as pokestopname,pokestop.latitude,pokestop.longitude,trs_quest.quest_task,if(trs_quest.quest_stardust>999,trs_quest.quest_stardust, null) from pokestop inner join trs_quest on pokestop.pokestop_id = trs_quest.GUID where quest_pokemon_id = "+itemid+" and DATE(FROM_UNIXTIME(trs_quest.quest_timestamp)) = CURDATE() and if(trs_quest.quest_stardust>999,trs_quest.quest_stardust, null) is not null and ST_CONTAINS(ST_GEOMFROMTEXT('POLYGON(("+area+"))'), point(pokestop.latitude, pokestop.longitude))")
 cursor.execute(query)
 name = cursor.fetchall()
 
 if not name:
  print ("no quests for "+item)
 else:
   
  #convert data into string
  res =[tuple(str(ele) for ele in sub) for sub in name]
 
  webhook = DiscordWebhook(url=webhookurl)
 
  # create embed object for webhook 
 
  research = ''
  for stop in res: 
 
   research += ('['+stop[0]+'](''https://www.google.com/maps/search/?api=1&query='''+stop[1]+','+stop[2]+')'+' - '+stop[3]+' - Amount:'+stop[4]+'\n') 

  embed = DiscordEmbed(title= item+' Field Research', description=research, color=16711931)
  embed.set_thumbnail(url=sprite) 
  # add embed object to webhook
  webhook.add_embed(embed)
  webhook.execute()
  time.sleep(2)




quest_mon("001","Bulbasaur",":sparkles:","0","00")
quest_mon("004","Charmander",":sparkles:","0","00")
quest_mon("007","Squirtle",":sparkles:","0","00")
quest_mon("009","Blastoise",":sparkles:","0","00")
quest_mon("016","Pidgey",":sparkles:","0","00")
quest_mon("027","Sandshrew",":sparkles:","0","00")
quest_mon("029","Nidoran",":sparkles:","0","00")
quest_mon("030","Nidorina",":sparkles:","0","00")
quest_mon("031","Nidoqueen",":sparkles:","0","00")
quest_mon("032","Nidoran",":sparkles:","0","00")
quest_mon("033","Nidorino",":sparkles:","0","00")
quest_mon("034","Nidoking",":sparkles:","0","00")
quest_mon("037","Vulpix","","0","00")
quest_mon("037","Alolan Vulpix",":sparkles:","56","61")
quest_mon("041","Ditto","","0","00")
quest_mon("056","Mankey",":sparkles:","0","00")
quest_mon("058","Growlithe",":sparkles:","0","00")
quest_mon("059","Arcanine",":sparkles:","0","00")
quest_mon("060","Poliwag",":sparkles:","0","00")
quest_mon("066","Machop",":sparkles:","0","00")
quest_mon("070","Weepinbell","","0","00")
quest_mon("072","Tentacool",":sparkles:","0","00")
quest_mon("073","Tentacruel",":sparkles:","0","00")
quest_mon("074","Geodude",":sparkles:","0","00")
quest_mon("077","Ponyta",":sparkles:","0","00")
quest_mon("081","Magnemite",":sparkles:","0","00")
quest_mon("084","Doduo","","0","00")
quest_mon("085","Dodrio","","0","00")
quest_mon("086","Seel",":sparkles:","0","00")
quest_mon("087","Dewgong",":sparkles:","0","00")
quest_mon("088","Grimer",":sparkles:","0","00")
quest_mon("090","Shellder",":sparkles:","0","00")
quest_mon("092","Gastly",":sparkles:","0","00")
quest_mon("095","Onix",":sparkles:","0","00")
quest_mon("096","Drowzee",":sparkles:","0","00")
quest_mon("100","Voltorb","","0","00")
quest_mon("102","Exeggcute","","0","00")
quest_mon("103","Exeggutor","","0","00")
quest_mon("104","Cubone",":sparkles:","0","00")
quest_mon("113","Chansey","","0","00")
quest_mon("121","Starmie","","0","00")
quest_mon("124","Jynx",":sparkles:","0","00")
quest_mon("125","Electabuzz",":sparkles:","0","00")
quest_mon("126","Magmar",":sparkles:","0","00")
quest_mon("129","Magikarp",":sparkles:","0","00")
quest_mon("131","Lapras",":sparkles:","0","00")
quest_mon("133","Eevee",":sparkles:","0","00")
quest_mon("138","Omanyte",":sparkles:","0","00")
quest_mon("140","Kabuto",":sparkles:","0","00")
quest_mon("142","Aerodactyl",":sparkles:","0","00")
quest_mon("147","Dratini",":sparkles:","0","00")
quest_mon("191","Sunkern",":sparkles:","0","00")
quest_mon("220","Swinub",":sparkles:","0","00")
quest_mon("209","Snubbull",":sparkles:","0","00")
quest_mon("215","Sneasel",":sparkles:","797","00")
quest_mon("216","Teddiursa","","0","00")
quest_mon("227","Skarmory",":sparkles:","0","00")
quest_mon("228","Houndour",":sparkles:","0","00")
quest_mon("234","Stantler",":sparkles:","0","00")
quest_mon("246","Larvitar",":sparkles:","0","00")
quest_mon("252","Treecko",":sparkles:","0","00")
quest_mon("261","Poochyena",":sparkles:","0","00")
quest_mon("270","Lotad",":sparkles:","0","00")
quest_mon("286","Breloom","","0","00")
quest_mon("287","Slakoth",":sparkles:","0","00")
quest_mon("294","Loudred","","0","00")
quest_mon("296","Makuhita",":sparkles:","0","00")
quest_mon("302","Sableye",":sparkles:","0","00")
quest_mon("307","Meditite",":sparkles:","0","00")
quest_mon("310","Manectric",":sparkles:","0","00")
quest_mon("311","Plusle",":sparkles:","0","00")
quest_mon("312","Minun",":sparkles:","0","00")
quest_mon("317","Swalot","","0","00")
quest_mon("325","Spoink",":sparkles:","0","00")
quest_mon("327","Spinda Number 7",":sparkles:","0","00")
quest_mon("335","Zangoose",":sparkles:","0","00")
quest_mon("336","Seviper",":sparkles:","0","00")
quest_mon("345","Lileep",":sparkles:","0","00")
quest_mon("347","Anorith",":sparkles:","0","00")
quest_mon("353","Shuppet",":sparkles:","0","00")
quest_mon("359","Absol",":sparkles:","0","00")
quest_mon("361","Snorunt",":sparkles:","0","00")
quest_mon("362","Glalie","","0","00")
quest_mon("366","Clamperl",":sparkles:","0","00")
quest_mon("399","Bidoof","","0","00")
quest_mon("408","Cranidos","","0","00")
quest_mon("410","Shieldon","","0","00")
quest_mon("425","Drifloon",":sparkles:","0","00")
quest_mon("427","Buneary",":sparkles:","0","00")
quest_mon("436","Bronzor",":sparkles:","0","00")
quest_mon("459","Snover",":sparkles:","0","00")
quest_mon("562","Yamask",":sparkles:","0","00")
quest_mon("607","Litwick","","0","00")
quest_mon("613","Cubchoo","","0","00")
quest_mon("622","Golett","","0","00")
quest_item('202',"Max Revive","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_0202.png")
quest_item('502',"Glacial Lure","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/TroyKey_glacial.png")
quest_item('503',"Mossy Lure","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/TroyKey_moss.png")
quest_item('504',"Magnetic Lure","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/TroyKey_magnetic.png")
quest_item('706',"Golden Razz","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_0706.png")
quest_item('708',"Silver Pinap","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_0707.png")
quest_item('1101',"Sun Stone","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Sun_Stone_Sprite.png")
quest_item('1102',"Kings Rock","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_King's_Rock_Sprite.png")
quest_item('1103',"Metal Coat","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Metal_Coat_Sprite.png")
quest_item('1104',"Dragon Scale","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Dragon_Scale_Sprite.png")
quest_item('1105',"Up-Grade","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Up-Grade_Sprite.png")
quest_item('1106',"Sinnoh Stone","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Sinnoh_Stone_Sprite.png")
quest_item('1107',"Unova Stone","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Bag_Unova_Stone_Sprite.png")
quest_item('1201',"Fast TM","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_1201.png")
quest_item('1202',"Charged TM","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_1202.png")
quest_item('1301',"Rare Candy","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/Item_1301.png")
quest_stardust('0',"Stardust Over 1000","https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/static_assets/png/stardust_painted.png")