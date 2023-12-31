# Requirements

- the hard requirements revolve around how many tests you can write and how many you can get to pass by then writing code for them. 

- the goal is to get through two (2) iteration this week but since this is open ended, so as much as you can

- complete the following: 
    1. Pseuducode should follow the examples and step through each individual task. 
    2. Code must be commented well
    3. Tests should be written first, then code written to pass the tests

### Stretch Goals

- Iteration 3

- Iteration 4

## Iteration 1 - Core

This iteration covers core functionality for leveling, combat, and character attributes

### Feature: Create a Character (done)

> As a character I want to have a name so that I can be distinguished from other characters

- can get and set a name
>> first test passed
>> now we need to define the name? 

### Feature: Alignment (done)

> As a character I want to have an alignment so that I have something to guide my actions

- can get and set alignment
>> first text passed
>> now we need to define the alignment? 
- alignments are Good, Evil, and Neutral

### Feature: Armor Class & Hit Points (done)

> As a combatant I want to have an armor class and hit points so that I can resists attacks from my enemies

- has an Armor Class that defaults to 10
>> test passed
- has 5 hit points by default
>> test passed

### Feature: Character Can Attack (done)

> As a combatant I want to be able to attack other combatants so that I can survive to fight another day

- roll a 20 sided die (don't code the die)
- roll must meet or beat opponents armor class to hit
- a natural roll of 20 always hits

>> so we need to write a function for the dice roll (not actually rolling the die) 
>> so this is when the character we've started to create will actually do something? 
>>> which is why we need a function not just defining the variable

### Feature: Character Can Be Damaged (done)

> As an attacker I want to be able to damage my enemies so that they will die and I will live

- if attack is successful, other character takes 1 point of damage when hit
- if a roll is a natural 20 then a critical hit is dealt and the damage is doubled
- when hit points are 0 or fewer, the character is dead

### Feature: Character has Abilities Score

> As a character I want to have several abilities so that I am not identical to other characters except in name

- abilities are strength, dexterity, constitution, wisdom, intelligence, charisma
- abilities range from 1 to 20 and default to 10
- abilities have modifiers according to the following table: (reference documentation to see table)

### Feature: Character Ability Modifiers Modify Attributes

> As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

- add strength modifier to:
    - attack roll and damage dealt
    - double strength modifier on critical hits
    - minimum damage is always 1 (even on a critical hit)
- add dexterity modifier to armor class
- add constitution modifier to hit points (always at least 1 hit point)

### Feature: A Character Can Gain Experience When Attacking (done)

> As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

- when a successful attack occurs, the character gains 10 experience points

### Feature: A Character Can Level (done)

> As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

- level defaults to 1
- after 1000 experience points, the character gains a level
    - 0xp -> 1st level
    - 1000 xp -> 2nd level
    - 2000 xp -> 3rd level
    - etc.
- for each level: 
    - hit points increase by 5 plus con modifier
    - 1 is added to attack roll for every even level achieved

## Iteration 2

- Characters that a character can have

### Feature: Characters have classes

> As a player I want a character to have a class that customize its capabilities so that I can play more interesting characters

##### Ideas

- changes in hit points
- changes in attack and damage
- increases critical range or damage
- bonuses/penalties versus other classes
- special abilities
- alignment limitations

##### Samples

> As a player I want to play a Fighter so that I can kick ass and take names

- attacks roll is increased by 1 for every level instead of every other level
- has 10 hit points per level instead of 5

> As a player I want to play a Rogue so that I can defeat my enemies with finesse

- does triple damage on critical hits
- ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
- adds Dexterity modifier to attacks instead of Strength
- cannot have Good alignment

> As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a medieval European setting

- has 6 hit point per level instead of 5 
- does 3 points of damage instead of 1 when successfully attacking
- adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
- attack roll is increased by 1 every 2nd and 3rd level

> As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

- has 8 hit points per level instead of 5
- +2 to attack and damage when attacking Evil characters
- does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
- attacks roll is increased by 1 for every level instead of every other level
- can only have good alignment





## Pseudocode

- start with test case for character name (this will fail)
- write class that will pass the test
- repeat
- move on to the next case

- need ability class
>> within ability class I want to create the abilities (we have assigned them to an enum that gives them a value)
- we need a function that will create the ability (the enum does not create the ability it just gives it a value?)
- we then need to go to the character (Char) class and call the function that creates the ability that we made in the ability scores file
- 