init python:
    
    class Dummy: #a dummy class used in place of a battle. Normally this should be integrated with Jake's battle engine, instead of using a dummy class.
        def __init__(self,won):
            self.won = won
            
        
    ari_battle = Dummy(False)
    #sprite arrays should always be in north, south, east, west order.
    map_on = False #Is a map being displayed? This governs whether the "yesno" screen is modal.
    
    #SPRITES
    ari_sprites = [["ari-n2.png", "ari-n3.png", "ari-n1.png", "ari-n1.png"],  #enemy sprites
        ["ADYA_Overworld_Engine_1.0/ari-s2.png", "ADYA_Overworld_Engine_1.0/ari-s3.png", "ADYA_Overworld_Engine_1.0/ari-s1.png", "ADYA_Overworld_Engine_1.0/ari-s1.png"], 
        ["ari-e2.png", "ari-e3.png", "ari-e4.png", "ari-e1.png"], 
        ["ari-w2.png", "ari-w3.png", "ari-w4.png", "ari-w1.png"],
        (64,64)]
        
    salesman_sprites =[ #player sprites         #       ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-1.png
    ["ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Salesman sprites/salesmanbase-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    
    warrior_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-2.png","ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-3.png","ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-2.png","ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Warrior sprites/warrior-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    bard_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Bard sprites/bard-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    mage_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    elf_mage_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-n-elf-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-s-elf-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-e-elf-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/Mage sprites/mage-walk-w-elf-female-small-6.png"],
    (32,64)
    ]
    pathfinder_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/PathFinder sprites/pathfinder-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    
    skammerska_sprites =[ #player sprites         
    ["ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-n-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-s-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-e-human-female-small-6.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-1.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-2.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-3.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-4.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-5.png", "ADYA_Overworld_Engine_1.0/Sprites/skammerska sprites/skammerska-walk-w-human-female-small-6.png"],
    (32,64)
    ]
    
    #Prototype_sprites =[ #player sprites         
    #["ADYA_Overworld_Engine_1.0/Sprites/x sprites/x.png", ],
    #["ADYA_Overworld_Engine_1.0/Sprites/x sprites/x.png", ],
    #["ADYA_Overworld_Engine_1.0/Sprites/x sprites/x.png", ],
    #["ADYA_Overworld_Engine_1.0/Sprites/x sprites/x.png", ],
    #["ADYA_Overworld_Engine_1.0/Sprites/x sprites/x.png", ],
    #(32,64)
    #]
    villager_sprites = [ #villager
    ["ADYA_Overworld_Engine_1.0/villager-n1.png", "ADYA_Overworld_Engine_1.0/villager-n2.png", "ADYA_Overworld_Engine_1.0/villager-n3.png"],
    ["ADYA_Overworld_Engine_1.0/villager-s1.png", "ADYA_Overworld_Engine_1.0/villager-s2.png", "ADYA_Overworld_Engine_1.0/villager-s3.png"],
    ["villager-e1.png", "villager-e2.png", "villager-e3.png"],
    ["villager-w1.png", "villager-w2.png", "villager-w3.png"],
    (96,96)
    ]
    
    #TILESETS   game/ADYA_Overworld_Engine_1.0/Sprites/tiles/
    fontain_sprites = [ #villager
    ["ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png"],
    ["ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_1.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_2.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png", "ADYA_Overworld_Engine_1.0/Sprites/tiles/fontain_3.png"],
    
    (128,128)
    ]
     
   
    #signifier, base name, building size, roof size, has roof, goToLabel, actionLabel (used for descriptions)   ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/
    moordell_tiles = [
    ["1","ADYA_Overworld_Engine_1.0/cute_buildings/1", (256,216), (256,256),True,None,"building_locked"],
    ["2","ADYA_Overworld_Engine_1.0/cute_buildings/2", (256,216), (256, 256),True,None,"building_locked"],
    ["3","ADYA_Overworld_Engine_1.0/cute_buildings/3", (256,216), (256,256),True,None,"building_locked"],
    ["*","ADYA_Overworld_Engine_1.0/cute_buildings/inn", (342,216),(342,256),True, "inn","inn_desc"],
    ["4", "ADYA_Overworld_Engine_1.0/Sprites/tiles/Wood_floor", (64,64),None,False,None,None],
    ["5", "ADYA_Overworld_Engine_1.0/Sprites/tiles/stone_wall", (64,64),None,False,None,None],
    ["6", "ADYA_Overworld_Engine_1.0/Sprites/tiles/wall-painted", (64,64),None,False,None,None],
    ["7", "ADYA_Overworld_Engine_1.0/Sprites/tiles/sea-painted", (64,64),None, False,None,None],
    ["8", "ADYA_Overworld_Engine_1.0/Sprites/tiles/dirt-painted", (64,64),None, False, None,None],
    
    ["g", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/_1", (64,64),None, False, None,None],
    ["G", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/_2", (64,64),None, False, None,None],
    ["S", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/S", (64,64),None, False, None,None],
    ["N", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/N", (64,64),None, False, None,None],
    ["E", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/E", (64,64),None, False, None,None],
    ["W", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/W", (64,64),None, False, None,None],
    
    ["n", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/NW", (64,64),None, False, None,None],
    ["e", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/NE", (64,64),None, False, None,None],
    ["s", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/SE", (64,64),None, False, None,None],
    ["w", "ADYA_Overworld_Engine_1.0/Sprites/tiles/field grass/SW", (64,64),None, False, None,None],
    #-----------------1=NW      0=center        9=W#
    
    
    #---buildings-------#
    ["t","ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tree", (64,44), (191,194),True,None,"tree"],
    ["h","ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/Smal house painted2", (128,64), (150,170),True,None,"leave_city"],
     
    
    #-----city top floor-------------#
    ["å", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_1", (64,64),None, False, None, None],
    ["Å", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_7", (64,64),None, False, None, None],
    ["ä", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_13", (64,64),None, False, None, None],
    ["Ä", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_14", (64,64),None, False, None, None],
    ["ö", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_15", (64,64),None, False, None, None],
    ["Ö", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_9", (64,64),None, False, None, None],
    ["p", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_3", (64,64),None, False, None, None],
    ["P", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_2", (64,64),None, False, None, None],
    ["C", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_8", (64,64),None, False, None, None],
    #-------city wall-------#
    ["a", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_4", (64,64),None, False, None, None],
    ["b", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_10", (64,64),None, False, None, None],
    ["c", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_16", (64,64),None, False, None, None],
    ["d", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_17", (64,64),None, False, None, None],
    ["j", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_18", (64,64),None, False, None, None],
    ["f", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_12", (64,64),None, False, None, None],
    ["g", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_6", (64,64),None, False, None, None],
    ["h", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_5", (64,64),None, False, None, None],
    ["i", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/city/CityWall_11", (64,64),None, False, None, None],
    #---------tower top--------#
    ["l", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tower/spire_1", (64,64),None, False, None, None],
    ["m", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tower/spire_2", (64,64),None, False, None, None],
    ["r", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tower/spire_3", (64,64),None, False, None, None],
    
    ["Z", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tower/Tower", (192,160),None, False, None, None],
   
    ["Q", "ADYA_Overworld_Engine_1.0/Sprites/buildings and stuff/tower/towertop", (192,258),(192,258), True, None, None],
    ]
    #signifier, range, roaming,  sprite set, facing, associated battle label, associated battle
    moordell_enemies = [
    ["a", (512,512), True, ari_sprites, "down", "ari_caught", ari_battle],
    ]
    
    #signifier, range, roaming,  sprite set, facing, conversation label
    moordell_villagers = [
    ["v", (256,256), True, bard_sprites, "down", "talky_label"], #example of roaming NPC
    ["b",None, False, villager_sprites,  "down", "talky2"], #example of static NPC
    ["f", (0,0), True, fontain_sprites, "down", "talky_label"],
    ]
    
    #[signifier, goToLabel]
    moordell_portal_tiles = [['p', 'leave_city']]
    
    
    #MAP LAYOUTS
    #these maps should align for ease of use. 
    #If they don't look square, switch to a monospace font like consolas!   
    
    moordell_layout =[
    "ooooooooooooooo",
    "woooooooooooooe",
    "woooooo+ooooooe",
    "woooooooooooooe",
    "woooooooooooooe",
    "woooooooo0ooooe",
    "woooooooooooooe",
    "woqoooooooooooe",
    "woooooooQoooooe",
    "woooooooooooooe",
    "wooohoooooooooe",
    "woooooooooooooe",
    "wooooooolmroooe",
    "woooooooooooooe",
    "wooo1oooooooooe",
    "woooooooooooooe",
    "ooooooooooooooo",
    ]
  
    moordell_portals =[
    "ooooooopooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
    
    
    moordell_ground =[
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGnNeGGGGGGGGG",
    "GGGWgEGGGGGGGGG",
    "GGGwSsGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGG",
    ]
    
  
    moordell_enemies_layout =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "oooooooooofoooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooovooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]

