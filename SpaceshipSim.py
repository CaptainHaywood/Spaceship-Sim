
#Program 12 by James Haywood
import time
import sys
import shelve
import random
from pygame import mixer
from random import randrange, uniform
import os
global fuel
global fuelcap
global hullcap
global star
global planet
global station
global cash
global docked
global hull
global shiptype
global cargospace
global cargousage
global railgunammo
global hyperdrive
global inertiadrive
global fuelscoop
global lifecargo
global concargo
global indcargo
global luxcargo
global liqcargo
global piratechance #1 out of 100 chance changes with system being travelled in
piratechance = 0
lifecargo = 0
concargo = 0
indcargo = 0
luxcargo = 0
liqcargo = 0
fuelscoop = 0
hyperdrive = 0 
inertiadrive = 0
railgunammo = 10
shields = 0
cargousage = 0
cargospace = 500
shiptype = "Frontier Corp Shuttle"
hull = 100
hullcap = 100
docked = "No"
cash = 1000
fuel = 5000
fuelcap = 5000
star = "Sol"
planet = "Earth"
station = "Earth Starport"
safety = "0" #Nothing can harm you when safety is 0. 3 is maximum danger
print ("Welcome to Spaceship Sim. (C) 2017 James Haywood.")
print ("1 Play game")
print ("2 Quick Introduction")
print ("3 Credits")
print ("4 Quit")
startmenu = input("> ")
if startmenu == "2":
   print("Welcome to Spaceship Sim! It's the 24th century, the year 2350 AD. Humanity has spread to nearby stars via hyperspace gates, and now runs multiple colony worlds under the authority of the United Terran Authority. You are a random citizen who has scraped together enough cash to purchase a relatively large shuttle, and now you set off into the universe to make a profit. Meanwhile, something strange is happening at Saturn and in the Polaris system. The communications link with the team overseeing the construction of the Polaris hypergate has gone silent, and a private research station on Daphnis is showing strange energy fluctuations. What could it mean?")
   print("Ready to restart program?")
   restartp = input("> ")
   sys.exit()
elif startmenu == "3":
   print("A game by James Haywood")
   print("Credit to FTL: Faster Than Light for the hyperspace gate sound effect")
   print("Credit to James S.A. Corey and The Expanse for inspiring much of this game")
   print("Credit to acardnell24 on Stack Exchange for originally creating the battle code")
   print("Credit to Clinton Shorter for music (I made it with clips from The Expanse soundtrack)s")
   print("Thanks for playing!")
   print("Ready to restart program?")
   restartp = input("> ")
   sys.exit()
elif startmenu == "4":
   sys.exit()
elif startmenu == "1":
   print("")
print ("ShipBIOS activated. (C) BIOSCorp 2345")
time.sleep(0.6)
print ("REACTOR...OK.")
time.sleep(0.6)
print ("MAIN DRIVE.....OK.") 
time.sleep(0.6)
print ("COMPUTER SYSTEMS...OK.")
time.sleep(0.6)
print ("LIFE SUPPORT...OK.")
time.sleep(0.6)
print ("COMMS SYSTEMS...OK")
time.sleep(0.6)
print ("NON-ESSENTIAL SYSTEMS...OK.")
time.sleep(0.6)
print ("Boot complete! Have a nice day. (Type HELP for commands.)")
def run():
   global DEST
   global shiptype
   global hyperdrive
   global inertiadrive
   global fuelscoop
   global hull
   global docked
   global railgunammo
   global DESTDESC
   global fuel
   global planet
   global star
   global station
   global cash
   global hullcap
   global fuelcap
   global cargospace
   global cargousage
   global lifecargo
   global concargo
   global indcargo
   global luxcargo
   global liqcargo
   global piratechance
   global cargo
   global shields
   commandline = input("> ")
   if commandline == "HELP":
       print("---HELP MENU---")
       print("NAV - Displays navigation info and allows you to plot and execute a course.")
       print("JUMP - Only usable when at a hyperspace gate  - allows you to jump to other nearby star systems.")
       print("DOCK - Docks at a nearby station, if there is one.")
       print("LINK - Access station services and facilites, if docked.")
       print("STATUS - Displays current status.")
       print("DATA - Display encylopedia of commonly needed facts.")
       print("SIM - Launch a simulated battle.")
       print("SAVE - Save current system data.")
       print("LOAD - Load saved system data.")
       print("SHUTDOWN - Shutdown the system.")
       run()
   elif commandline == "SIM":
      print ("Simulation engaged!")
      sim()
   elif commandline == "DATA":
      print("1 Market prices by system")
      print("2 Ships and Ship Upgrades")
      print("3 Quit")
      data = input("> ")
      if data == "1":
         print ("---SOL---")
         print("Life Support Package: 10 CR")
         print("Commerical Goods: 20 CR")
         print("Industrial Goods: 30 CR")
         print("Luxury Goods: 40 CR")
         print("Liquor: 50 CR")
         print("")
         print ("---ALPHA CENTAURI---")
         print("Life Support Package: 15 CR")
         print("Commerical Goods: 5 CR")
         print("Industrial Goods: 30 CR")
         print("Luxury Goods: 50 CR")
         print("Liquor: 55 CR")
         print("")
         print ("---BARNARD'S STAR---")
         print("Life Support Package: 20 CR")
         print("Commerical Goods: 5 CR")
         print("Industrial Goods: 5 CR")
         print("Luxury Goods: 50 CR")
         print("Liquor: 5 CR")
         print("")
         print ("---SIRIUS---")
         print("Life Support Package: 1 CR")
         print("Commerical Goods: 1 CR")
         print("Industrial Goods: 1 CR")
         print("Luxury Goods: 1 CR")
         print("Liquor: 75 CR")
         print("")
         print ("---FOMALHAUT---")
         print("Life Support Package: 0 CR")
         print("Commerical Goods: 25 CR")
         print("Industrial Goods: 40 CR")
         print("Luxury Goods: 100 CR")
         print("Liquor: 100 CR")
         print("")
         print ("---TAU CETI---")
         print("Life Support Package: 0 CR")
         print("Commerical Goods: 30 CR")
         print("Industrial Goods: 35 CR")
         print("Luxury Goods: 5 CR")
         print("Liquor: 60 CR")
         print("")
         print ("---TRAPPIST-1--")
         print("Life Support Package: 0 CR")
         print("Commerical Goods: 25 CR")
         print("Industrial Goods: 35 CR")
         print("Luxury Goods: 45 CR")
         print("Liquor: 150 CR")
         print("")
         run()
      elif data == "2":
         print("--Far Horizons Long-Range Craft--")
         print ("Hull: 250")
         print ("Fuel Cap: 10000")
         print ("Cargo Space: 1000")
         print ("Cost: 500000 CR")
         print("--Tradesman Cargo Freighter--")
         print ("Hull: 250")
         print ("Fuel Cap: 7500")
         print ("Cargo Space: 10000")
         print ("Cost: 750000 CR")
         print("--Nucleonus Combat Fighter--")
         print ("Hull: 500")
         print ("Fuel Cap: 600")
         print ("Cargo Space: 250")
         print ("Cost: 250000 CR")
         print("--Frontier Corp Shuttle--")
         print ("Hull: 100")
         print ("Fuel Cap: 1000")
         print ("Cargo Space: 500")
         print ("Cost: 100000 CR")
         run()
      elif data == "3":
         run()
      else:
         print ("INVALID OPTION. RESETTING...")
         run()
         
   elif commandline == "2056":
      if planet != "Haywood's Claim":
         print("INVALID OPTION. RESETTING...")
         run()
      elif planet == "Haywood's Claim":
         print ("Welcome, Mr. Haywood. Activating ELITE HAX0RZ menu...")
         print("---ELITE HAX0RZ MENU---")
         print("1 Set credit amount to 999 billion")
         print("2 Set fuel amount to 999 billion")
         print("3 Set hull amount to 999 billion")
         print("4 Install inertia drive")
         print("5 Install fuel scoop")
         print("6 Install 10,000 shields")
         print("7 Undock")
         hax = input("> ")
         if hax == "1":
            print ("Done.")
            cash = 999999999999
            run()
         elif hax == "2":
            print ("Done.")
            fuel = 999999999999
            run()
         elif hax == "3":
            print ("Done.")
            hull = 999999999999
            run()
         elif hax == "4":
            print ("Done.")
            inertiadrive = 1
            run()
         elif hax == "5":
            print("Done.")
            fuelscoop = 1
            run()
         elif hax == "6":
            print ("Done.")
            shields = 10000
            run()
         elif hax == "7":
            print("Undocked!")
            run()
         else:
            print("INVALID OPTION. RESETTING...")
            run()
         
   elif commandline == "SHUTDOWN":
       print ("Goodbye.")
       time.sleep(1)
       sys.exit()
   elif commandline == "SAVE":
      shelfFile = shelve.open('save')
      shelfFile['fuelVariable'] = fuel
      shelfFile['hullVariable'] = hull
      shelfFile['starVariable'] = star
      shelfFile['planetVariable'] = planet
      shelfFile['cashVariable'] = cash
      shelfFile['fuelcapVariable'] = fuelcap
      shelfFile['hullcapVariable'] = hullcap
      shelfFile['stationVariable'] = station
      shelfFile['dockedVariable'] = docked
      shelfFile['ammoVariable'] = railgunammo
      shelfFile['cargospaceVariable'] = cargospace
      shelfFile['cargousageVariable'] = cargousage
      shelfFile['shipVariable'] = shiptype
      shelfFile['inertiaVariable'] = inertiadrive
      shelfFile['scoopVariable'] = fuelscoop
      shelfFile['lifeVariable'] = lifecargo
      shelfFile['conVariable'] = concargo
      shelfFile['indVariable'] = indcargo
      shelfFile['luxVariable'] = luxcargo
      shelfFile['liqVariable'] = liqcargo
      shelfFile.close()
      print ("System data saved!")
      run()
   elif commandline == "LOAD":
      shelfFile = shelve.open('save')
      fuel = shelfFile ['fuelVariable']
      hull = shelfFile ['hullVariable']
      star = shelfFile ['starVariable']
      planet = shelfFile ['planetVariable']
      cash = shelfFile ['cashVariable']
      fuelcap = shelfFile ['fuelcapVariable']
      hullcap = shelfFile ['hullcapVariable']
      station = shelfFile ['stationVariable']
      docked = shelfFile ['dockedVariable']
      railgunammo = shelfFile ['ammoVariable']
      cargospace = shelfFile ['cargospaceVariable']
      cargousage = shelfFile ['cargousageVariable']
      shiptype = shelfFile ['shipVariable']
      inertiadrive = shelfFile ['inertiaVariable']
      fuelscoop = shelfFile ['scoopVariable']
      lifecargo = shelfFile['lifeVariable']
      concargo = shelfFile['conVariable']
      indcargo = shelfFile['indVariable']
      luxcargo = shelfFile['luxVariable']
      liqcargo = shelfFile['liqVariable']
      shelfFile.close()
      print ("System data loaded!")
      run()
   elif commandline == "STATUS":
      print ("---STATUS---")
      print ("Hull:", hull, "")
      print ("Fuel:", fuel, "")
      print ("Cargo Usage:", cargousage, "/", cargospace, "")
      print ("Life Support Package Cargo:", lifecargo, "")
      print ("Consumer Goods Cargo:", concargo, "")
      print ("Industrial Goods Cargo:", indcargo, "")
      print ("Luxury Goods Cargo:", luxcargo, "")
      print ("Liquor Cargo:", liqcargo, "")
      print ("Current star system:", star, "")
      print ("Current celestial body:", planet, "")
      print ("Chance of hostile enounter in current system:", piratechance, "/ 100")
      print ("Nearby Station:", station, "")
      print ("Docked?", docked, "")
      print ("Credits:", cash, "")
      print ("Ship:", shiptype, "")
      print ("Railgun slugs:", railgunammo, "")
      print ("---STATUS---")
      run()
   elif commandline == "JUMP":
     if planet in("SolGate", "AlphaGate", "BarnardGate", "SiriusGate", "FomalhautGate", "TauGate", "TRAPPISTGate"):
       print ("Querying hypergate for jump clearance...")
       time.sleep(1)
       print ("Clearance granted.")
       print ("1 Sol")
       print ("2 Alpha Centauri")
       print ("3 Barnard's Star")
       print ("4 Sirius")
       print ("5 Fomalhaut")
       print ("6 Tau Ceti")
       print ("7 TRAPPIST-1")
       gatechoice = input("> ")
       if gatechoice == "1":
         if star == "Sol":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Sol...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Sol"
         planet = "SolGate"
         piratechance = 0
         run()
       elif gatechoice == "2":
         if star == "Alpha Centauri":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Alpha Centauri...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Alpha Centauri"
         planet = "AlphaGate"
         piratechance = 15
         run()
       elif gatechoice == "3":
         if star == "Barnard's Star":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Barnard's Star...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Barnard's Star"
         planet = "BarnardGate"
         piratechance = 15
         run()
       elif gatechoice == "4":
         if star == "Sirius":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Sirius...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Sirius"
         planet = "SiriusGate"
         piratechance = 5
         run()
       elif gatechoice == "5":
         if star == "Fomalhaut":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Fomalhaut...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Fomalhaut"
         planet = "FomalhautGate"
         piratechance = 1
         run()
       elif gatechoice == "6":
         if star == "Tau Ceti":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to Tau Ceti...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "Tau Ceti"
         planet = "TauGate"
         piratechance = 20
         run()
       elif gatechoice == "7":
         if star == "TRAPPIST-1":
           print ("Already at specified destination!")
           run()
         print ("Jumping through hypergate to TRAPPIST-1...")
         mixer.init()
         mixer.music.load('jump.mp3')
         mixer.music.play()
         time.sleep(2)
         print ("Jump complete!")
         star = "TRAPPIST-1"
         planet = "TRAPPISTGate"
         piratechance = 30
         run()
     print("No hypergate nearby!")
     run()
   
   elif commandline == "DOCK":
     if station == "none":
       print ("No station nearby!")
       run()
     print ("Docking successful!")
     docked = "Yes"
     run()
   elif commandline == "LINK":
     if docked == "No":
        print ("Not docked!")
        run()
     print ("---LINK---")
     print ("Linking...")
     time.sleep(2)
     print ("Link successful.")
     if station != "none":
         print("1 Repair")
         print("2 Refuel")
         print("3 Order Ship")
         print("4 Order upgrades")
         print("5 Market")
         print("6 Undock")
         link = input("> ")
         if link == "1":
            damage = abs(hullcap - hull)
            repaircost = int(damage) * int(10)
            print("Cost to repair hull will be, in credits,", repaircost, "")
            print("Begin repairs? (Y/N)")
            repairyn = input("> ")
            if cash < repaircost:
              print("Not enough credits!")
              run()
            if repairyn in ("Y", "y"):
              print("Hull repaired!")
              cash = cash - repaircost
            elif repairyn in ("N", "n"):
              print("Aborted.")
              run()
            else:
              print ("INVALID OPTION. RESETTING...")
              run()
              
         elif link == "5":
           market()
           
         elif link == "6":
           print ("Undocking successful!")
           docked = "No"
         elif link == "4":
           print ("---UPGRADES---")
           print ("1 Cargo Expansion - 25000 credits. Expands cargo capacity by 200. One per vessel, non-transferrable.")
           print ("2 Railgun Slugs (10) - 250 credits. Ammunition for railguns.")
           print ("3 Inertia Drive - 1000000 credits. This cutting edge drive allows rapid travel at thousands of gravities at no fuel cost.")
           print ("4 Fuel Scoop - 35000 credits. Allows you to refuel from the coronas of certain stars.")
           upgradesmenu = input("> ")
           if upgradesmenu == "1":
             if cash < 25000:
               print ("Not enough credits!")
               run()
             if hyperdrive == 1:
               print ("Already purchased!")
               run()
             print ("Cargo Expansion installed!")
             cargocap = cargocap + 200
             run()
           elif upgradesmenu == "2":
             if cash < 250:
               print ("Not enough credits!")
               run()
             print ("Slugs purchased.")
             railgunammo = railgunammo + 10
             cash = cash - 250
           elif upgradesmenu == "3":
             if cash < 1000000:
               print ("Not enough credits!")
               run()
             if inertiadrive == 1:
               print ("Already purchased!")
               run()
             print ("Inertia drive installed.")
             inertiadrive = 1
             run()
           elif upgradesmenu  == "4":
             if cash < 35000:
               print ("Not enough credits!")
               run()
             if fuelscoop == 1:
               print ("Already purchased!")
               run()
             print ("Fuel scoop installed.")
             cash = cash - 35000
             fuelscoop = 1
         elif link == "2":
          print("Refuel complete!")
          fuel = fuelcap
          run()
          
         elif link == "3":
            print("---SHIP CATALOG---")
            print("You have a:", shiptype, "")
            print("AVAILABLE:")
            print("1 Far Horizons Long-Range Craft")
            print("2 Tradesman Cargo Freighter")
            print("3 Nucleonus Combat Fighter")
            print("4 Frontier Corp Shuttle")
            shipcatalog = input("> ")
            if shipcatalog == "1":
              if shiptype == "Far Horizons Long-Range Craft":
                print ("You alredy own this ship!")
                run()
              print ("Hull: 250")
              print ("Fuel Capacity: 10000")
              print ("Cargo Space: 1000")
              print ("Cost: 500000 Credits")
              print ("Purchase? (Y/N)")
              shipyn = input("> ")
              shipcost = 500000
              if shipyn in ("Y", "y"):
                if cash < shipcost:
                  print ("Not enough credits!")
                  run()
                print ("Ship purchased!")
                cash = cash - shipcost
                shiptype = "Far Horizons Long-Range Craft"
                fuelcap = 10000
                cargospace = 1000
                hull = 250
                run()
            if shipcatalog == "2":
              if shiptype == "Tradesman Cargo Freighter":
                print ("You alredy own this ship!")
                run()
              print ("Hull: 250")
              print ("Fuel Capacity: 7500")
              print ("Cargo Space: 10000")
              print ("Cost: 750000 Credits")
              print ("Purchase? (Y/N)")
              shipyn = input("> ")
              shipcost = 750000
              if shipyn in ("Y", "y"):
                if cash < shipcost:
                  print ("Not enough credits!")
                  run()
                print ("Ship purchased!")
                cash = cash - shipcost
                shiptype = "Tradesman Cargo Freighter"
                fuelcap = 7500
                cargospace = 10000
                hull = 500
                run()
            if shipcatalog == "3":
              if shiptype == "Nucleonus Combat Fighter":
                print ("You alredy own this ship!")
                run()
              print ("Hull: 500")
              print ("Fuel Capacity: 600")
              print ("Cargo Space: 250")
              print ("Cost: 250000 Credits")
              print ("Purchase? (Y/N)")
              shipyn = input("> ")
              shipcost = 250000
              if shipyn in ("Y", "y"):
                if cash < shipcost:
                  print ("Not enough credits!")
                  run()
                print ("Ship purchased!")
                cash = cash - shipcost
                shiptype = "Nucleonus Combat Fighter"
                fuelcap = 600
                cargospace = 250
                hull = 500
                shields = 5
                run()
            if shipcatalog == "4":
              if shiptype == "Frontier Corp Shuttle":
                print ("You already own this ship!")
                run()
              print ("Hull: 100")
              print ("Fuel Capacity: 1000")
              print ("Cargo Space: 500")
              print ("Cost: 100000 Credits")
              print ("Purchase? (Y/N)")
              shipyn = input("> ")
              shipcost = 100000
              if shipyn in ("Y", "y"):
                if cash < shipcost:
                  print ("Not enough credits!")
                  run()
                print ("Ship purchased!")
                cash = cash - shipcost
                shiptype = "Frontier Corp Shuttle"
                fuelcap = 600
                cargospace = 250
                hull = 500
                run()
         else:
             run()
   elif commandline == "NAV":
       print ("---NAVIGATION MENU---")
       print ("1 LOCAL SYSTEM")
       print ("2 STARMAP")
       navmenu = input("> ")
       if navmenu == "2":
          print("---STARMAP---")
          print("* SOL")
          print("|")
          print("* ALPHA CENTAURI")
          print("|")
          print ("* BARNARD'S STAR")
          print("|")
          print("* SIRIUS")
          print("|")
          print("* FOMALHAUT")
          print("|")
          print("* TAU CETI")
          print("|")
          print("* TRAPPIST-1")
          print("|")
          print("* POLARIS (GATE UNDER CONSTRUCTION, NOT OPEN TO THE PUBLIC)")
          run()
       elif navmenu == "1":
          if star == "Sol":
              print ("---SOL SYSTEM---")
              print ("")
              print ("1 SOL (CLASS G STAR)")
              print ("|")
              print ("2 MERCURY (BARREN ROCK WORLD)")
              print ("|")
              print ("3 VENUS (HOT HELL WORLD)")
              print ("|")
              print ("4 EARTH AND LUNA (THE CRADLE OF HUMANITY)")
              print ("|")
              print ("5 MARS (TERRAFORMED COLONY WORLD)")
              print ("|")
              print ("6 THE BELT")
              print ("|")
              print ("7 JUPITER (GAS GIANT)")
              print ("|")
              print ("8 SATURN (GAS GIANT)")
              print ("|")
              print ("9 URANUS (ICE GIANT)")
              print ("|")
              print ("10 NEPTUNE (ICE GIANT)")
              print ("|")
              print ("11 PLUTO (ROCKY DWARF PLANET)")
              print ("|")
              print ("12 SOL HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Sol is a Class G main sequence star with 8 official planets, one of which is the cradle of humanity. This star can be fuel scooped."
                 DEST = "Sol"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Mercury is a barren rock that is of absolutely no use to anyone besides as a base for automated solar mining operations."
                 DEST = "Mercury"
                 station = "none"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Venus is a hot hell world with crushing pressures, sulfuric acid instead of water, and high winds. Don't even think about landing. There are scoopable fuel isotopes and common minerals in the upper atmosphere, however."
                 DEST = "Venus"
                 station = "Venus Fuel Depot" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Earth is humanity's home planet, temperate and perfect for life. It also has a single moon. However, since the advent of hypergates, it has developed an economy around being a nostalgic tourist trap."
                 DEST = "Earth"
                 station = "Earth Starport" 
                 insystem()
              elif sysmenu == "5": 
                 DESTDESC = "Mars used to be a cold, dead world only explored by rovers launched from Earth. However, with the creation of fusion technology, the planet was terraformed with relative ease into a second Earth."
                 DEST = "Mars"
                 station = "Mars Station" 
                 insystem()
              elif sysmenu == "6": 
                 DESTDESC = "Sol's asteroid belt is the dividing line between the inner terrestrial planets and the outer gas giants. Due to it's abundance of Duranium-rich asteroids, it is a perfect location for mining and manufacturing."
                 DEST = "Belt"
                 station = "Ceres Shipyards" 
                 insystem()
              elif sysmenu == "7": 
                 DESTDESC = "Jupiter is Sol's largest planet and has many useful gases in it's upper atmosphere, making it Sol's prime gas refinery. Its' many moons also carry a host of colonies."
                 DEST = "Jupiter"
                 station = "Jupiter Refinery" 
                 insystem()
              elif sysmenu == "8": 
                 DESTDESC = "Saturn is a beautiful gas giant with enourmous rings that provide for almost all of Sol's water needs. Its' moons are peppered with colonies."
                 DEST = "Saturn"
                 station = "Saturn Science Base" 
                 insystem()
              elif sysmenu == "9": 
                 DESTDESC = "Uranus is a featureless world with a faint ring system in an equatorial orbit. Possibly even less useful than Mercury."
                 DEST = "Uranus"
                 station = "none" 
                 insystem()
              elif sysmenu == "10": 
                 DESTDESC = "Neptune is a gorgeous blue planet that has attracted many a tourist. Unfortunately, like Uranus, it is useless."
                 DEST = "Neptune"
                 station = "none" 
                 insystem()
              elif sysmenu == "11": 
                 DESTDESC = "Pluto is a dwarf planet on the fringes of Sol's gravity well. It is semi-abundant in almost all of the materials used in ships, and as such a repair station operates in orbit."
                 DEST = "Pluto"
                 station = "Pluto Repair Station" 
                 insystem()
              elif sysmenu == "12": 
                 DESTDESC = "The Sol Hyperspace Gate was mankind's first Faster-Than-Light device, and was an enourmous success, allowing one way travel to all nearby stars where more gates could be built."
                 DEST = "SolGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "Alpha Centauri":
              print ("---ALPHA CENTAURI SYSTEM---")
              print ("")
              print ("1 ALPHA CENTAURI A (CLASS G STAR)")
              print ("|")
              print ("2 ALPHA CENTAURI B (NEUTRON STAR)")
              print ("|")
              print ("3 ALPHA CENTAURI I (SUPER-JUPITER)")
              print ("|")
              print ("4 ALPHA CENTAURI II (HUMAN COLONY WORLD)")
              print ("|")
              print ("5 ALPHA CENTAURI III (NON-NEWTONIAN ELEMENT RICH DWARF PLANET)")
              print ("|")
              print ("6 ALPHA CENTAURI C (RED DWARF STAR)")
              print ("|")
              print ("7 ALPHA CENTAURI HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Alpha Centauri A is one of three stars in the Alpha Centauri system. It is a Class G star and can be fuel scooped."
                 DEST = "Alpha Centuari A"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Alpha Centauri B is one of three stars in the Alpha Centauri system. It is a neutron star, and as a result the planets in the system are rich in non-Newtonian elements."
                 DEST = "Alpha Centauri B"
                 station = "none"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Alpha Centauri I is a gas giant ten times the size of Jupiter, with massive amounts of fuel isotopes in it's atmosphere that are refined on the orbiting station."
                 DEST = "Alpha Centauri I"
                 station = "SuperJovian Fuel Depot" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Alpha Centuari II is man's first interstellar colony, created before the first hypergate. The colonists crossed the void at near-lightspeed with a Bussard drive, and upon arrival found a perfectly habitable world that had no pre-exisiting life."
                 DEST = "Alpha Centauri II"
                 station = "Pioneer Spaceport" 
                 insystem()
              elif sysmenu == "5": 
                 DESTDESC = "This seemingly barren dwarf planet is saturated in non-Newtonian elements due to the resident neutron star. These elements are essential for modern spaceflight, and the body has enough to run civilization for the next few million years."
                 DEST = "Alpha Centauri III"
                 station = "Nucleonus non-Newtonian Element Mining Station" 
                 insystem()
              elif sysmenu == "6": 
                 DESTDESC = "Alpha Centauri C is one of three stars in the Alpha Centauri system. As a red dwarf it is practically useless, and being over 0.21 LY away from the main binary pair, only ships with the largest engines can reach it."
                 DEST = "Alpha Centauri C"
                 station = "none" 
                 insystem()
              elif sysmenu == "7": 
                 DESTDESC = "The Alpha Centuari Hyperspace Gate was mankind's first gate to be built outside of the Sol system."
                 DEST = "AlphaGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "Barnard's Star":
              print ("---BARNARD'S STAR SYSTEM---")
              print ("")
              print ("1 BARNARD'S STAR (CLASS M RED STAR)")
              print ("|")
              print ("2 BARNARD'S STAR I (BARREN ROCK)")
              print ("|")
              print ("3 BARNARD'S STAR II (GAS GAINT)")
              print ("|")
              print ("4 BARNARD'S STAR III (ICE GIANT)")
              print ("|")
              print ("5 BARNARD'S STAR IV (UNDERGROUND COLONY WORLD)")
              print ("|")
              print ("6 BARNARD'S STAR HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Barnard's Star is a Class M Red Star. It cannot be fuel scooped due to high concentrations of helium."
                 DEST = "Barnard's Star"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Barnard's Star I is a barren rock. That's it."
                 DEST = "Barnard's Star I"
                 station = "none"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Barnard's Star II is a roughly Saturn-sized gas giant with beautiful rainbow rings that stretch for almost 0.10 astronomical units."
                 DEST = "Barnard's Star II"
                 station = "Barnard's Star II Rest Station" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Barnard's Star III is an irregularity - an ice giant roughly the size of Pluto. It is also a shocking shade of yellow, which is caused by high sulfur concentrations."
                 DEST = "Barnard's Star III"
                 station = "none" 
                 insystem()
              elif sysmenu == "5": 
                 DESTDESC = "Barnard's Star IV is in a perfect orbit that always puts it behind Barnard's Star II, which protects it from much of the star's radiation. A mining colony has been established under the surface of the body."
                 DEST = "Barnard's Star IV"
                 station = "Colony Port" 
                 insystem()
              elif sysmenu == "6": 
                 DESTDESC = "This is the hyperspace gate for Barnard's Star."
                 DEST = "BarnardGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "Sirius":
              print ("---SIRIUS SYSTEM---")
              print ("")
              print ("1 SIRIUS A (TYPE A HOT WHITE STAR)")
              print ("|")
              print ("2 SIRIUS B (WHITE DWARF STAR)")
              print ("|")
              print ("3 VULCAN (TINY LAVA WORLD)")
              print ("|")
              print ("4 SIRIUS C (BLACK HOLE)")
              print ("|")
              print ("5 SIRIUS HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Sirius A is a type A hot white star that cannot be fuel scooped due to overheating issues. It is in a trinary orbit with Sirius B and C."
                 DEST = "Sirius A"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Sirius B is a white dwarf star that cannot even be approached due to gravity. It is in a trinary orbit with Sirius A and C."
                 DEST = "Sirius B"
                 station = "none"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Vulcan is a tiny lava world that spews natrually-made militairy grade fuel and rare elements like it's Christmas. It also manages to avoid being eaten by a black hole. A militairy station is in orbit, but it is open to civilians."
                 DEST = "Vulcan"
                 station = "Vulcan Militairy Outpost" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Sirius C is a 10-solar-mass black hole in a trinary orbit with Sirius A and B. Don't even think about getting within 20 AU."
                 DEST = "Sirius C"
                 station = "none" 
                 insystem()
              elif sysmenu == "5": 
                 DESTDESC = "This is the hyperspace gate for Sirius."
                 DEST = "SiriusGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "Fomalhaut":
              print ("---FOMALHAUT SYSTEM---")
              print ("")
              print ("1 FOMALHAUT (TYPE C BLUE STAR)")
              print ("|")
              print ("2 CONVERSION (TERRAFROMED COLONY WORLD)")
              print ("|")
              print ("3 FOMALHAUT II (ROGUE MOON)")
              print ("|")
              print ("4 TRANSFORMATION (TERRAFROMED COLONY WORLD)")
              print ("|")
              print ("5 FOMALHAUT HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Fomalhaut is a type C blue star that can be fuel scooped. It harbors two successfully terraformed worlds."
                 DEST = "Fomalhaut"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Conversion is a terraformed colony world with a large human population."
                 DEST = "Conversion"
                 station = "Conversion Station"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Fomalhaut II is a rogue moon that was captured in a polar orbit around Fomalhaut. There is a science base in orbit and on the surface."
                 DEST = "Fomalhaut II"
                 station = "Fomalhaut Science Outpost" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Transformation is a colony world that was terraformed by the inhabitants of Conversion. In the words of one colonist: 'We wanted a vacation spot.'"
                 DEST = "Transformation"
                 station = "Transformation Resort" 
                 insystem()
              elif sysmenu == "5": 
                 DESTDESC = "This is the hyperspace gate for Fomalhaut."
                 DEST = "FomalhautGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "Tau Ceti":
              print ("---TAU CETI SYSTEM---")
              print ("")
              print ("1 TAU CETI (TYPE G YELLOW STAR)")
              print ("|")
              print ("2 LIFE (COLONY WORLD WITH INDIGENOUS ANIMAL AND PLANT LIFE)")
              print ("|")
              print ("3 VENUS: THE NEXT GENERATION (HOT HELL WORLD)")
              print ("|")
              print ("4 HAYWOOD'S CLAIM (DWARF PLANET)")
              print ("|")
              print ("5 ICE PACK (GIANT ICE BALL)")
              print ("|")
              print ("6 TAU CETI HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "Tau Ceti is a type G yellow star that can be fuel scooped."
                 DEST = "Tau Ceti"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "Life is a colony world with indigenous plant and animal life, all of which are herbivores. One species, the perfle, has been adopted as a common and very cuddly household pet."
                 DEST = "Life"
                 station = "Life Port"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "Venus: The Next Generation is a humorously named body that is almost exactly like Venus in the Sol system."
                 DEST = "Venus: The Next Generation"
                 station = "none" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "Haywood's Claim is an asteroidal body claimed by James Haywood in 2317. No one objected."
                 DEST = "Haywood's Claim"
                 station = "none" 
                 insystem()
              elif sysmenu == "5":
                 DESTDESC = "Ice Pack is an unexplained giant ball of ice flying through space."
                 DEST = "Ice Pack"
                 station = "none"
                 insystem()
              elif sysmenu == "6": 
                 DESTDESC = "This is the hyperspace gate for Tau Ceti."
                 DEST = "TauGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()
          elif star == "TRAPPIST-1":
              print ("---TRAPPIST-1 SYSTEM---")
              print ("")
              print ("1 TRAPPIST-1 (COOL DWARF STAR)")
              print ("|")
              print ("2 TRAPPIST-1 I (COLONY WORLD WITH INDIGENOUS PLANT LIFE)")
              print ("|")
              print ("3 TRAPPIST-1 II (HABITABLE WORLD WITH STONE-AGE INTELLIGENT LIFE)")
              print ("|")
              print ("4 TRAPPIST-1 III (HABITABLE WORLD WITH LATE INUDSTRIAL AGE INTELLIGENT LIFE)")
              print ("|")
              print ("5 TRAPPIST-1 IV (HABITABLE WORLD WITH EARLY SPACE AGE INTELLIGENT LIFE)")
              print ("|")
              print ("6 TRAPPIST-1 V (GAS GIANT) ")
              print ("|")
              print ("7 TRAPPIST-1 VI (PREVIOUSLY HABITABLE WORLD IN NUCLEAR WINTER)")
              print ("|")
              print ("8 TRAPPIST-1 VII (TERRESTRIAL BODY WITH HELIUM/OXYGEN ATMOSPHERE)")
              print ("|")
              print ("9 TRAPPIST-1 HYPERSPACE GATE")
              sysmenu = input("> ")
              if sysmenu == "1": 
                 DESTDESC = "TRAPPIST-1 is a cool dwarf star with seven bodies orbiting it. This star cannot be fuel scooped."
                 DEST = "TRAPPIST-1"
                 station = "none"
                 insystem()
              elif sysmenu == "2": 
                 DESTDESC = "TRAPPIST-1 I is a colony world with indigenous plant life."
                 DEST = "TRAPPIST-1 I"
                 station = "TRAPPIST-1 Outpost"
                 insystem()
              elif sysmenu == "3": 
                 DESTDESC = "TRAPPIST-1 II is a habitable world with stone-age intelligent life. Do not interfere."
                 DEST = "TRAPPIST-1 II "
                 station = "none" 
                 insystem()
              elif sysmenu == "4": 
                 DESTDESC = "TRAPPIST-1 III is a habitable world with late industrial age life. In terms of human progress, they are currently around the technological capabilities of 1920."
                 DEST = "TRAPPIST-1 III"
                 station = "none" 
                 insystem()
              elif sysmenu == "5":
                 DESTDESC = "TRAPPIST-1 IV, named Kerbin by it's inhabitants (the Kerbals), houses an early space age civilization. They have landed on both of the planet's moons. The physiology is humanoid, but they are shorter, have fairly small limbs, and green skin. Their cylinder-shaped head is also unique."
                 DEST = "TRAPPIST-1 IV or KERBIN"
                 station = "none"
                 insystem()
              elif sysmenu == "6":
                 DESTDESC = "TRAPPIST-1 V is a gas giant with a strange green coloration."
                 DEST = "TRAPPIST-1 V"
                 station = "none"
                 insystem()
              elif sysmenu == "7":
                 DESTDESC = "TRAPPIST-1 VI appeared to house a once advanced civilization until they self-annihilated in a war over their own version of hypergate technology. A single gate lays intact and active on the surface, with no partner gates to link to."
                 DEST = "TRAPPIST-1 VI"
                 station = "Orbital Precursor Civilization Research Facility (OPCRF)"
                 insystem()
              elif sysmenu == "8":
                 DESTDESC = "TRAPPIST-1 VII is a terrestrial body with a helium oxygen atmosphere. The planet is too small to be useful, but the planet can harbor human life without protection. As such, it makes for a legendary party location, especially because it makes you squeaky."
                 DEST = "TRAPPIST-1 VII"
                 station = "Squeak Planetary Party Space Rentals"
                 insystem()
              elif sysmenu == "9": 
                 DESTDESC = "This is the hyperspace gate for TRAPPIST-1."
                 DEST = "TRAPPISTGate"
                 station = "none" 
                 insystem()
              else:
                 print ("INVALID OPTION. RESETTING...")
                 run()

       else:
         print ("INVALID OPTION. RESETTING...")
         run()
   else:
      print ("INVALID OPTION. RESETTING...")
      run()
def market():
   global cash
   global cargospace
   global cargousage
   global lifecargo
   global concargo
   global indcargo
   global luxcargo
   global liqcargo
   if star == "Sol":
      lifeworth = 10
      conworth = 20
      indworth = 30
      luxworth = 40
      liqworth= 50
   elif star == "Alpha Centauri":
      lifeworth = 15
      conworth = 5
      indworth = 30
      luxworth = 50
      liqworth = 55
   elif star == "Barnard's Star":
      lifeworth = 20
      conworth = 5
      indworth = 5
      luxworth = 50
      liqworth = 5
   elif star == "Sirius":
      lifeworth = 1
      conworth = 1
      indworth = 1
      luxworth = 1
      liqworth = 75
   elif star == "Fomalhaut":
      lifeworth = 0
      conworth = 25
      indworth = 40
      luxworth = 100
      liqworth = 100
   elif star == "Tau Ceti":
      lifeworth = 0
      conworth = 30
      indworth = 35
      luxworth = 5
      liqworth = 60
   elif star == "TRAPPIST-1":
      lifeworth = 0
      conworth = 25
      indworth = 35
      luxworth= 45
      liqworth = 150
   print ("---MARKET---")
   print ("1 Buy")
   print ("2 Sell")
   print ("3 Cancel")
   buysell = input("> ")
   if buysell == "2":
           print ("1 Life Support Packages in hold:", lifecargo, "")
           print ("2 Consumer Goods in hold:", concargo, "")
           print ("3 Industrial Goods in hold:", indcargo, "")
           print ("4 Luxury Goods in hold:", luxcargo, "")
           print ("5 Liquor in hold:", liqcargo, "")
           print ("6 Cancel")
           sell = input("> ")
           if sell == "1":
                  print ("How many tons do you want to sell?")
                  selling = int(input("> "))
                  if selling > lifecargo:
                     print ("You don't have that much!")
                     run()
                  lifecargo = lifecargo - selling
                  cargousage = cargousage - selling
                  earned = int(selling) * int(lifeworth)
                  cash = cash + earned
                  print ("Cargo sold. Credits earned:", earned, "")
                  run()
           elif sell == "2":
                  print ("How many tons do you want to sell?")
                  selling = int(input("> "))
                  if selling > concargo:
                     print ("You don't have that much!")
                     run()
                  concargo = concargo - selling
                  cargousage = cargousage - selling
                  earned = int(selling) * int(conworth)
                  cash = cash + earned
                  print ("Cargo sold. Credits earned:", earned, "")
                  run()
           elif sell == "3":
                  print ("How many tons do you want to sell?")
                  selling = int(input("> "))
                  if selling > indcargo:
                     print ("You don't have that much!")
                     run()
                  indcargo = indcargo - selling
                  cargousage = cargousage - selling
                  earned = int(selling) * int(indworth)
                  cash = cash + earned
                  print ("Cargo sold. Credits earned:", earned, "")
                  run()
           elif sell == "4":
                  print ("How many tons do you want to sell?")
                  selling = int(input("> "))
                  if selling > luxcargo:
                     print ("You don't have that much!")
                     run()
                  luxcargo = luxcargo - selling
                  cargousage = cargousage - selling
                  earned = int(selling) * int(luxworth)
                  cash = cash + earned
                  print ("Cargo sold. Credits earned:", earned, "")
                  run()
           elif sell == "5":
                  print ("How many tons do you want to sell?")
                  selling = int(input("> "))
                  if selling > liqcargo:
                     print ("You don't have that much!")
                     run()
                  liqcargo = liqcargo - selling
                  cargousage = cargousage - selling
                  earned = int(selling) * int(liqworth)
                  cash = cash + earned
                  print ("Cargo sold. Credits earned:", earned, "")
                  run()
           else:
              print("Invalid choice. Going back to select...")
              market()
              
   elif buysell == "1":
           print ("1 Life Support Package ", lifeworth,"CR)")
           print ("2 Consumer Goods ", conworth,"CR")
           print ("3 Industrial Goods ", indworth,"CR")
           print ("4 Luxury Goods ", luxworth,"CR")
           print ("5 Liquor ", liqworth,"CR")
           print ("6 Cancel")
           market = input("> ")
           if market == "1":
              print ("You have", cargospace, "tons available.")
              print ("Enter how many tons you want to purchase.")
              tonnage = int(input("> "))
              if tonnage > cargospace:
                 print ("Cannot hold that much cargo!")
                 run()
              elif cargousage == cargospace:
                 print ("Cargo hold full!")
                 run()
              cost = int(lifeworth) * int(tonnage)
              if cost > cash:
                 print ("Not enough credits!")
                 run()
              cash = cash - cost
              cargousage = cargousage + tonnage
              lifecargo = tonnage
              print ("Cargo Loaded!")
              run()
           elif market == "2":
              print ("You have", cargospace, "tons available.")
              print ("Enter how many tons you want to purchase.")
              tonnage = int(input("> "))
              if tonnage > cargospace:
                 print ("Cannot hold that much cargo!")
                 run()
              elif cargousage == cargospace:
                 print ("Cargo hold full!")
                 run()
              cost = int(conworth) * int(tonnage)
              if cost > cash:
                 print ("Not enough credits!")
                 run()
              cash = cash - cost
              cargousage = cargousage + tonnage
              concargo = tonnage
              print ("Cargo Loaded!")
              run()
           elif market == "3":
              print ("You have", cargospace, "tons available.")
              print ("Enter how many tons you want to purchase.")
              tonnage = int(input("> "))
              if tonnage > cargospace:
                 print ("Cannot hold that much cargo!")
                 run()
              elif cargousage == cargospace:
                 print ("Cargo hold full!")
                 run()
              cost = int(indworth) * int(tonnage)
              if cost > cash:
                 print ("Not enough credits!")
                 run()
              cash = cash - cost
              cargousage = cargousage + tonnage
              indcargo = tonnage
              print ("Cargo Loaded!")
              run()
           elif market == "4":
              print ("You have", cargospace, "tons available.")
              print ("Enter how many tons you want to purchase.")
              tonnage = int(input("> "))
              if tonnage > cargospace:
                 print ("Cannot hold that much cargo!")
                 run()
              elif cargousage == cargospace:
                 print ("Cargo hold full!")
                 run()
              cost = int(luxworth) * int(tonnage)
              if cost > cash:
                 print ("Not enough credits!")
                 run()
              cash = cash - cost
              cargousage = cargousage + tonnage
              luxcargo = tonnage
              print ("Cargo Loaded!")
              run()
           elif market == "5":
              print ("You have", cargospace, "tons available.")
              print ("Enter how many tons you want to purchase.")
              tonnage = int(input("> "))
              if tonnage > cargospace:
                 print ("Cannot hold that much cargo!")
                 run()
              elif cargousage == cargospace:
                 print ("Cargo hold full!")
                 run()
              cost = int(liqworth) * int(tonnage)
              if cost > cash:
                 print ("Not enough credits!")
                 run()
              cash = cash - cost
              cargousage = cargousage + tonnage
              liqcargo = tonnage
              print ("Cargo Loaded!")
              run()
           elif market == "6":
              run()
           
           else:
               print("Not a valid choice! Going back to select...")
               market()
def sim():
        global hull
        global simhull
        computer_health = randrange(0, 250)
        winner = None
        simhull = hull
        player_health = simhull
        music = randrange(1, 3)
        if music == 1:
         mixer.init()
         mixer.music.load('battle1.mp3')
         mixer.music.play()
        elif music == 2:
         mixer.init()
         mixer.music.load('battle2.mp3')
         mixer.music.play()
        elif music == 3:
         mixer.init()
         mixer.music.load('battle3.mp3')
         mixer.music.play()
        turn = random.randint(1,2) 
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("You will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("Enemy will go first.")


        print("\nYour hull: ", player_health, "Enemy hull: ", computer_health)

        while (player_health != 0 or computer_health != 0):

            heal_up = False 
            miss = False 

           
            moves = {"Laser": random.randint(5, 15),
                     "Railgun": random.randint(30, 50),
                     "Repair": random.randint(15, 25)}

            if player_turn:
                print("\nPlease select a move:\n1. Laser (Deal damage between 5-15)\n2. Railgun - USES SLUG AMMO (Deal damage between 30-50)\n3. Repair (Restore between 15-25 hull)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1, 10) 
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 
                    print("You missed!")
                else:
                    if player_move in ("1", "laser"):
                        player_move = moves["Laser"]
                        print("\nYou fired the Laser. It dealt ", player_move, " hull damage.")
                    elif player_move in ("2", "railgun"):
                       if railgunammo == 0:
                          print ("Out of railgun slugs!")
                          player_move = moves["Laser"]
                          print("\nYou fired the Laser. It dealt ", player_move, " hull damage.")
                       else:
                        player_move = moves["Railgun"]
                        print("\nYou fired the Railgun. It dealt ", player_move, " hull damage.")
                    elif player_move in ("3", "repair"):
                        heal_up = True 
                        player_move = moves["Repair"]
                        print("\nYou activated the repair drones. They healed ", player_move, " hull damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 
                    print("The computer missed!")
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["Laser"]
                            print("\nThe enemy fired his laser. It dealt ", computer_move, " hull damage.")
                        elif player_health > 35 and player_health <= 75:
                            imoves = ["Laser", "Railgun"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe enemy fired his ", imoves, ". It dealt ", computer_move, " hull damage.")
                        elif player_health <= 35:
                            computer_move = moves["Railgun"] 
                            print("\nThe enemy fired his Railgun. It dealt ", computer_move, "hull damage.")                       
                    else: 
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Repair"]
                            print("\nThe enemy deployed his repair drones. It repaired ", computer_move, " hull damage.")
                        else:
                            if player_health > 75:
                                computer_move = moves["Laser"]
                                print("\nThe enemy fired his Laser. It dealt ", computer_move, " hull damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Laser", "Railgun"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe enemy fired his ", imoves, ". It dealt ", computer_move, " hull damage.")
                            elif player_health <= 35:
                                computer_move = moves["Railgun"] 
                                print("\nThe enemy fired his Railgun. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > hull:
                        player_health = hull 
                else:
                    computer_health += computer_move
                    if computer_health > 250:
                        computer_health = 250
            else:
                if player_turn:
                    computer_health -= player_move

                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "You"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Enemy"
                        break

            print("\nYour hull: ", player_health, "Enemy hull: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn


        if winner == "You":
            print("\nYour health: ", player_health, "Enemy health: ", computer_health)
            print("\nEnemy destroyed!")
            mixer.music.stop()
            run()
        else:
            print("\nYour health: ", player_health, "Enemy health: ", computer_health)
            print("\nYou have been destroyed. GAME OVER.")
            mixer.music.stop()
            battlelost = input("")
            run()
      
              
def battle():
        global hull
        global railgunammo
        computer_health = randrange(0, 250)
        winner = None
        player_health = hull
        music = randrange(1, 3)
        if music == 1:
         mixer.init()
         mixer.music.load('battle1.mp3')
         mixer.music.play()
        elif music == 2:
         mixer.init()
         mixer.music.load('battle2.mp3')
         mixer.music.play()
        elif music == 3:
         mixer.init()
         mixer.music.load('battle3.mp3')
         mixer.music.play()
        turn = random.randint(1,2) 
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("You will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("Enemy will go first.")


        print("\nYour hull: ", player_health, "Enemy hull: ", computer_health, "Railgun slugs: ", railgunammo)

        while (player_health != 0 or computer_health != 0):

            heal_up = False 
            miss = False 

           
            moves = {"Laser": random.randint(5, 15),
                     "Railgun": random.randint(30, 50),
                     "Repair": random.randint(15, 25)}

            if player_turn:
                print("\nPlease select a move:\n1. Laser (Deal damage between 5-15)\n2. Railgun - USES SLUG AMMO (Deal damage between 30-50)\n3. Repair (Restore between 15-25 hull)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1, 10) 
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 
                    print("You missed!")
                else:
                    if player_move in ("1", "laser"):
                        player_move = moves["Laser"]
                        print("\nYou fired the Laser. It dealt ", player_move, " hull damage.")
                    elif player_move in ("2", "railgun"):
                       if railgunammo == 0:
                          print ("Out of railgun slugs!")
                          player_move = moves["Laser"]
                          print("\nYou fired the Laser. It dealt ", player_move, " hull damage.")
                       else:
                        player_move = moves["Railgun"]
                        railgunammo = railgunammo - 1
                        print("\nYou fired the Railgun. It dealt ", player_move, " hull damage.")
                    elif player_move in ("3", "repair"):
                        heal_up = True 
                        player_move = moves["Repair"]
                        print("\nYou activated the repair drones. They healed ", player_move, " hull damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 
                    print("The computer missed!")
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["Laser"]
                            print("\nThe enemy fired his laser. It dealt ", computer_move, " hull damage.")
                        elif player_health > 35 and player_health <= 75:
                            imoves = ["Laser", "Railgun"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe enemy fired his ", imoves, ". It dealt ", computer_move, " hull damage.")
                        elif player_health <= 35:
                            computer_move = moves["Railgun"] 
                            print("\nThe enemy fired his Railgun. It dealt ", computer_move, "hull damage.")                       
                    else: 
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Repair"]
                            print("\nThe enemy deployed his repair drones. It repaired ", computer_move, " hull damage.")
                        else:
                            if player_health > 75:
                                computer_move = moves["Laser"]
                                print("\nThe enemy fired his Laser. It dealt ", computer_move, " hull damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Laser", "Railgun"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe enemy fired his ", imoves, ". It dealt ", computer_move, " hull damage.")
                            elif player_health <= 35:
                                computer_move = moves["Railgun"] 
                                print("\nThe enemy fired his Railgun. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > hull:
                        player_health = hull 
                else:
                    computer_health += computer_move
                    if computer_health > 250:
                        computer_health = 250
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "You"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Enemy"
                        break

            print("\nYour hull: ", player_health, "Enemy hull: ", computer_health, "Railgun slugs:", railgunammo)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn


        if winner == "You":
            print("\nYour health: ", player_health, "Enemy health: ", computer_health)
            print("\nEnemy destroyed!")
            mixer.music.stop()
            run()
        else:
            print("\nYour health: ", player_health, "Enemy health: ", computer_health)
            print("\nYou have been destroyed. GAME OVER.")
            mixer.music.stop()
            battlelost = input("")
            sys.exit()            
           

def insystem():
   global planet
   global star
   global fuel
   global station
   global docked
   global piratechance
   print (DESTDESC)
   print ("1 Plot and execute course")
   print ("2 Leave")
   bodymenu = input("> ")
   if bodymenu == "2":
     run()
   elif bodymenu == "1":
     docked = "No"
     if fuel == 0:
         print("No fuel!")
         run()
     if DEST == planet:
         print ("Already at specified destination!")
         run()
     print("Calculating course to", DEST, "...")
     time.sleep(2)
     print ("Course plotted successfully. 200 units of fuel will be consumed to execute this course. Confirm? (Y/N)")
     burnexe = input("> ")
     if burnexe in ("Y", "y"):
         print ("Executing burn. Prepare for hypersleep.")
         mixer.init()
         mixer.music.load('swoosh.mp3')
         mixer.music.play()
         pirate = randrange(0, 100)
         if pirate <= piratechance:
            print("Alert! Hostile vessel detected on intercept course - prepare for engagement!")
            battle()
         print ("Course complete. Now in orbit around ", DEST,".")
         planet = DEST
         if inertiadrive == 1:
           run()
         elif inertiadrive == 0:
            fuel = fuel - 200
            run()
     elif burnexe in ("N", "n"):
            print("Aborted.")
            run()    
   
   else:
      print("INVALID OPTION. RESETTING...")
      run()
run()
