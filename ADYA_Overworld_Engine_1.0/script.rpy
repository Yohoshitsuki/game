##############################################################################
# Character Creation Screen - by Steamgirl
#
# A screen lets you distribute skill points.
# To use this screen initialise the various points
# Then use the following in your script:
# call screen character_creation
##############################################################################
# Example initialisation of points below. Move it where you want it.
init:
    #The number of maximum creation points
    $ init_creation_points = 9
    #The current number of creation points
    $ creation_points = init_creation_points
    
    $ skill1_points = 4
    $ skill2_points = 4
    
    
    #Skill 1 (in the example case, it's Charisma)
    $ Friendly_max = 4
    $ Friendly_points = 0

    #Skill 2 (in the example case, it's Strength)
    $ Agressive_max = 4
    $ Agressive_points = 0
    
    $ Devious_max = 4
    $ Devious_points = 0
    
    $ Reson_max = 4
    $ Reson_points = 0
     #-------Perk---------#
    $ Perk_max = 3
    $ Perk_points = 3
    $ init_Perk_points = 3
    
    $ Athletics_points = 0
    $ Charisma_points = 0
    
    $ Infiltration_points = 0
    $ Investigation_points = 0
    $ Lore_points = 0
    
    $ Perform_points = 0
    $ Wealth_points = 0
     
screen character_creation:
    default tt = Tooltip("  ")
    #$ tooltip = GetTooltip()

        
    frame:
        
        xfill True
        has vbox
        
        xanchor 0
        hbox:
            text "Points available: [creation_points]"
        hbox:
            if creation_points == 0 or Friendly_points == Friendly_max:
                textbutton ("Friendly") xminimum 200 action None
            else:
                textbutton ("Friendly") xminimum 200 action [SetVariable("Friendly_points", Friendly_points + 1), SetVariable("creation_points", creation_points - 1)]hovered tt.Action("Rank [Friendly_points], effects your suport stat \n ")
                
            bar range Friendly_max * 1.2 value Friendly_points xmaximum 100
        hbox:
            if creation_points == 0 or Agressive_points == Agressive_max:
                textbutton ("Agressive") xminimum 200 action None
            else:
                textbutton ("Agressive") xminimum 200 action [SetVariable("Agressive_points", Agressive_points + 1), SetVariable("creation_points", creation_points - 1)]hovered tt.Action("Rank [Agressive_points], effects your physical \n and speech damage")
            bar range Agressive_max * 1.2 value Agressive_points xmaximum 100
            
        hbox:
            if creation_points == 0 or Devious_points == Devious_max:
                textbutton ("Devious") xminimum 200 action None
            else:
                textbutton ("Devious") xminimum 200 action [SetVariable("Devious_points", Devious_points + 1), SetVariable("creation_points", creation_points - 1)]hovered tt.Action("Rank [Devious_points], effects your dadge and hax chans \n ")
            bar range Devious_max * 1.2 value Devious_points xmaximum 100
        hbox:
            if creation_points == 0 or Reson_points == Reson_max:
                textbutton ("Reson") xminimum 200 action None
            else:
                textbutton ("Reson") xminimum 200 action [SetVariable("Reson_points", Reson_points + 1), SetVariable("creation_points", creation_points - 1)]hovered tt.Action("Rank [Reson_points], effects your hitt chans \n and your magic points")
            bar range Reson_max * 1.2 value Reson_points xmaximum 100
            
        hbox:
            textbutton ("Start Over") action [SetVariable("Friendly_points", 0), SetVariable("Agressive_points", 0), SetVariable("Devious_points", 0), SetVariable("Reson_points", 0), SetVariable("creation_points", init_creation_points)]
            
        #--------Perks--------#
        hbox:
            text "Perk Points available: [Perk_points]"
        hbox:
            if Perk_points == 0 or Athletics_points == Perk_max:
                textbutton ("Athletics") xminimum 200 action None
            else:
                textbutton ("Athletics") xminimum 200 action [SetVariable("Athletics_points", Athletics_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Athletics_points xmaximum 100
        
        hbox:
            if Perk_points == 0 or Charisma_points == Perk_max:
                textbutton ("Charisma") xminimum 200 action None
            else:
                textbutton ("Charisma") xminimum 200 action [SetVariable("Charisma_points", Charisma_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Charisma_points xmaximum 100
        
        hbox:
            if Perk_points == 0 or Infiltration_points == Perk_max:
                textbutton ("Infiltration") xminimum 200 action None
            else:
                textbutton ("Infiltration") xminimum 200 action [SetVariable("Infiltration_points", Infiltration_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Infiltration_points xmaximum 100
        
        hbox:
            if Perk_points == 0 or Investigation_points == Perk_max:
                textbutton ("Investigation") xminimum 200 action None
            else:
                textbutton ("Investigation") xminimum 200 action [SetVariable("Investigation_points", Investigation_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Investigation_points xmaximum 100
        
        hbox:
            if Perk_points == 0 or Lore_points == Perk_max:
                textbutton ("Lore") xminimum 200 action None
            else:
                textbutton ("Lore") xminimum 200 action [SetVariable("Lore_points", Lore_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Lore_points xmaximum 100
        
        hbox:
            if Perk_points == 0 or Perform_points == Perk_max:
                textbutton ("Perform") xminimum 200 action None
            else:
                textbutton ("Perform") xminimum 200 action [SetVariable("Perform_points", Perform_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Perform_points xmaximum 100
            
        hbox:
            if Perk_points == 0 or Wealth_points == Perk_max:
                textbutton ("Wealth") xminimum 200 action None
            else:
                textbutton ("Wealth") xminimum 200 action [SetVariable("Wealth_points", Wealth_points + 1), SetVariable("Perk_points", Perk_points - 1)]
            bar range Perk_max * 1.2 value Wealth_points xmaximum 100
        hbox:
            
            textbutton ("Start Over") action [SetVariable("Athletics_points", 0), SetVariable("Charisma_points", 0), SetVariable("Infiltration_points", 0), SetVariable("Investigation_points", 0), SetVariable("Lore_points", 0), SetVariable("Perform_points", 0), SetVariable("Wealth_points", 0), SetVariable("Perk_points", init_Perk_points)]
            if creation_points == 0 and Perk_points == 0:
                textbutton ("Finished") action [SetVariable("Proceed", 1), Return()]
            else:
                textbutton ("Finished") action None    
        hbox:
            xfill True
            text tt.value xanchor-300 yanchor -50
screen tooltip_test:

    default tt = Tooltip("No button selected.")

    frame:
        xfill True
        xalign 0.0
        yalign 0.0

        has vbox
        

        textbutton "One.":
            action Return(1)
            hovered tt.Action("The loneliest number.")

        textbutton "Two.":
            action Return(2)
            hovered tt.Action("Is what it takes.")

        textbutton "Three.":
            action Return(3)
            hovered tt.Action("A crowd.")
    default tt = Tooltip("No button selected.")
    frame:
        
        has vbox
        xalign 0.7
        yalign 0.7
        text tt.value        
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
image white = Solid((255,255,255, 255))
image black = Solid((0,0,0, 255))
image field = "jadebrook_field.jpg"
image inn = "inn.jpg"
image girl = "girl.png"

# The game starts here.
label start:
    #jump party_screen_demo
    #jump isometric_grid_demo
    #jump equip_demo
    $playerX = None
    $playerY = None
    menu:
        "Warrior":
            python:
                player = warrior_sprites
                Sprite=GetHumanWarriorFemaleSprite()
        "Salesman":
            python:
                player = salesman_sprites
                Sprite=GetHumanSalesmanFemaleSprite()
        "Mage":
            python:
                player = mage_sprites
                Sprite=GetHumanMageFemaleSprite()
        "Bard":
            python:
                player = bard_sprites
                Sprite=GetHumanBardFemaleSprite()
        "Pathfinder":
            python:
                player = pathfinder_sprites
                Sprite=GetHumanPathFinderFemaleSprite()
        "Courtier":
            python:
                player = skammerska_sprites
                Sprite=GetHumanSkammerskaFemaleSprite()
        "Elf":
            python:
                player = elf_mage_sprites
                Sprite=GetElfMageFemaleSprite()
    
    #show screen character_creation
    $ Proceed = 0
    show screen character_creation
    while creation_points > 0 or Perk_points > 0 or Proceed == 0:
        pause
    hide screen character_creation
    $ renpy.block_rollback()
    ""
    $ player_name = renpy.input("What is your name, Adventurer?")

    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Generica"
    python:
       steve = PlayerFighter(player_name, Speed=9, Move=10, Attack=50, Speech=5, Defence=2, Bonus_Move=0, Might=5, Health=30, Used=0, Powered=0, sprite=Sprite)
   
label map:
    $map_on = True
    window hide None
    scene black
    #play music "happy.ogg" fadein .5
    python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = moordell_layout, tileList = moordell_tiles,
            portals = moordell_portals, portal_tiles = moordell_portal_tiles,
            enemy_layout = moordell_enemies_layout, enemySprites = moordell_enemies,
            
            NPCSprites = moordell_villagers, #villagers, uses the same layout as enemies
            groundLayout = moordell_ground,
            playerSprites = player, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
    with dissolve
    return
    
label talky_label:
    #show girl at left onlayer npcPortraits with dissolve
    e "I'm an NPC!"
    e "You can talk to me if you need help."
    
    e "I might have something useful to say."
    e "Or not."
    e "Until then I'll just go about my day."
    #hide girl with dissolve
    jump elevation_demo
    return
label talky2:
    show girl at left onlayer npcPortraits with dissolve
    e "I'm also an NPC!"
    e "But I'm static. I'm content to just sit around."
    e "I'm more likely to be important, so the programmer made me easier to find!"
    e "By the way, I wonder what's beyond that gate. Maybe you should go see."
    hide girl with dissolve
    return
label ari_caught:
    scene field with dissolve
    "Oh no! You got caught."
    $ari_battle.won = True
    jump map
    
label leave_city:
    #scene field with dissolve
    "Looks like it's time to go."
    jump elevation_demo
    return
    
label inn:
    scene inn with dissolve
    "This is where an inn would go!"
    "Truly amazing."
    jump map
label building_locked:
    "It's locked."
    return
label tree:
    "It's a tree."
    return
label inn_desc:
    "It's an inn. A faint light is cast through the window, and figures can be seen moving inside."
    "A pleasant din is heard through the door."
    return
    
