---
title: How To Play
layout: default
---
Navigation ~ [Home](https://captainhaywood.github.io/Spaceship-Sim) ~ [How to Play](https://captainhaywood.github.io/Spaceship-Sim/HOW) ~ [Credits](https://captainhaywood.github.io/Spaceship-Sim/CREDITS)

# How To Play
You start your game in orbit of Earth in the Sol system, with 1000 credits in your account. You have a small Frontier Corp Shuttle with 500 tons of cargospace and 5000 units of fuel, plus ten railgun slugs for defense. Your goal is to trade your way to the top among the seven stars that humanity has access to.
- IMPORTANT: Commands MUST be entered in ALL CAPS. Using caps lock is fine.
- NOTE: In menus, entering an invalid option will take you back to the top terminal prompt, and you must enter the command again.

For starters, the NAV command. Enter NAV into your terminal prompt and hit enter. You will see a menu like this:
```
---NAVIGATION MENU---
1 LOCAL SYSTEM
2 STARMAP
> 
```
Enter "1" and press enter. You will be presented with a list that looks like this:
```
---SOL SYSTEM---

1 SOL (CLASS G STAR)
|
2 MERCURY (BARREN ROCK WORLD)
|
3 VENUS (HOT HELL WORLD)
|
*skip*
|
12 SOL HYPERSPACE GATE
>
```
Seeing as Sol is a fairly bland system trading-wise, enter "12" for the hyperspace gate and press enter. If you want to explore Sol before doing so, however, feel free to select another destination that interests you. After selecting the gate, you will get a prompt like this:
```
The Sol Hyperspace Gate was mankind's first Faster-Than-Light device, and was an enourmous success, allowing one way travel to all nearby stars where more gates could be built.
1 Plot and execute course
2 Leave
> 
```
Enter "1" and press enter. The navigation software will check that you have enough fuel and that you are not already at the destination. If it checks out, it will display a final confirmation prompt:
```
Course plotted successfully. 200 units of fuel will be consumed to execute this course. Confirm? (Y/N)
> 
```
Enter "Y" or "y" and press enter to confirm. The travel sequence will play, which includes a sound effect.
```
Executing burn. Prepare for hypersleep.
Course complete. Now in orbit around SolGate.
```
- NOTE: During the travel sequence, the game will randomly check if a battle happens against the danger level of the system. In Sol, the danger level is zero, so you won't get an enemy encounter. In other systems, the danger level represents a probability from 1 to 100. With a danger level of, say, 20, you will get an encounter 20% of the time when travelling in that system. If you do get an encounter later, it will alert you like this:
```
Alert! Hostile vessel detected on intercept course - prepare for engagement!
```
- NOTE, CONTINUED: If you defeat the enemy, you will be placed back at the planet or other body you started from. Fuel will not have been consumed, and you may re-plot and execute the course.
After successfully arriving at the gate, you will have been brought back to the top-level command prompt. Enter "JUMP" and press enter. A menu will appear:
```
Querying hypergate for jump clearance...
Clearance granted.
1 Sol
2 Alpha Centauri
3 Barnard's Star
4 Sirius
5 Fomalhaut
6 Tau Ceti
7 TRAPPIST-1
> 
```
Seeing as Barnard's Star has the cheapest prices for the most valued commodity in the interstellar age - liquor - enter "3" and press enter. The jump sequence will play with a distinctive sound effect.
```
Jumping through hypergate to Barnard's Star...
Jump complete!
```
You will now be at the Barnard's Star hypergate. Before we proceed any further, you should try the STATUS command, which is invaluable for in-flight diagnosing of your current situation. Since you are once more at the top-level command prompt, enter "STATUS" and press enter. The status screen will print out. It should look like this if you have gone straight to Barnard's star and done nothing else:
```
---STATUS---
Hull: 100
Fuel: 4800
Cargo Usage: 0/500
Life Support Package Cargo: 0
Consumer Goods Cargo : 0
Industrial Goods Cargo: 0
Luxury Goods Cargo: 0
Liquor Cargo: 0
Current star system: Barnard's Star
Current celestial body: BarnardGate
Chance of hostile encounter in current system: 15/100
Nearby Station: none
Docked? no
Ship: Frontier Corp Shuttle
Railgun slugs: 10
---STATUS---
>
```
Once you have a good idea what the STATUS command does, you should try the SIM command before you go any further - unlike Sol, there is a risk of hostilities in Barnard's Star. The SIM command launches a simulated battle on your control terminal. Here is an example encounter:
```

```
