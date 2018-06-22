init -10 python:
    
    import time
    
    # Order a list to have the items with a higher Priority nearer the beginning of the list.
    def Battle_Priority_Compare(a, b):
        if a.Priority > b.Priority:
            return -1
        elif b.Priority > a.Priority:
            return 1
        else: #equal
            return 0
       
    # Order a list to have the items with a Position nearer the bottom of the screen appear
    # later in the list (nearer left to break ties)
    def Battle_Draw_Compare(a, b):
        if (a.Position is None and b.Position is None):
            return 0
        elif (a.Position is None):
            return 1
        elif (b.Position is None):
            return -1
        elif (a.Position.Y < b.Position.Y):
            return -1
        elif (b.Position.Y < a.Position.Y):
            return 1
        elif (a.Position.X < b.Position.X):
            return -1
        elif (b.Position.X < a.Position.Y):
            return 1
        else:
            return 0
            
    ###
    # Prioritisers
    # Prioritisers are a way of increasing the unit's priority - depending on the turn basis used.
    # These are assigned to the Fighter instance, so it can have priorities addressed in a consistent manner.
    ###
    
    # The base class does nothing and always has a priority of 0.
    class Prioritiser(BattleAware):
        
        def __init__(self, fighter):
            self._priority = 0
            self._fighter = fighter
            
        def getPriority(self):
            return self._priority
        def setPriority(self, value):
            self._priority = value
            
        Priority = property(getPriority, setPriority)

    # The ActivePrioritiser emulates FF-style battles, where each fighter's initiative rises until they reach a certain level, at which point they get to take actions, and their priority is reduced to 0.
    class ActivePrioritiser(Prioritiser):
        
        def __init__(self, fighter):
            super(ActivePrioritiser, self).__init__(fighter)
            
            fighter.RegisterStat("Speed", 10)
            
            self._priority = renpy.random.randint(0, 100)
            
            
        def Tick(self):
            self._priority = self._priority + self._fighter.Stats.Speed

        def EndTurn(self):
            self._priority = 0
    
    # The TurnPrioritiser is used for simple turn-based battles; priority per se doesn't matter so much as who has or hasn't had their turn yet.
    # Of course, we still need to provide priority data in case anyone uses an Extra which makes use of it.
    class TurnPrioritiser (Prioritiser):
        
        def Tick(self):
            self._priority = 1
            
        def EndTurn(self):
            self._priority = 0
    
    ###
    # BattleSchema
    # BattleSchemata help the BattleContext set fighters up with the right set of classes - the right kind of Prioritiser, etc.
    ###
    
    # Base class does nothing
    class BattleSchema:
        
        def SetBattle(self, battle):
            self._battle = battle
        
        # Pass in the fighter instance rather than having separate methods to return each kind of thing a Fighter instance
        # needs - firstly for extensibility, secondly so we can check other properties on the instance and potentially make
        # decisions based on them.
        def SetUpFighter(self, fighter, **properties):
            None
        
        # Call to do any necessary initialisation on the battlefield itself.
        def SetUpBattlefield(self, battlefield):
            None
            
        # Return a dictionary mapping the battle-relevant layer keys to layer indices in the reserved-for-battles layers.
        # More than one key can be mapped to a single layer, but all keys must be returned.
        def GetLayers(self):
            return {"BG": 0, "Fighters": 0, "Stats": 1, "Effects": 2, "UI": 3, "Overlay":4}
                        
        # Return a BattleMechanic to run the current battle with
        def GetMechanic(self):
            return BattleMechanic(_battle)
        
        # Get an AttackResolver that the current battle will use to determine how attacks fare and what happens
        def GetAttackResolver(self):
            return AttackResolver()
            
        # Get a UIProvider with which the current battle will present choices and other interface to the user
        def GetUIProvider(self):
            return UIProvider(self._battle)
            
        # Get a BattlePanner with which to pan the screen if/when necessary
        def GetPanner(self, battle):
            return BattlePanner(battle)
            
        def GetLoSThreshold(self):
            return 0.25

        
    # ActiveSchema sets up for FF-style 'active' battles
    class ActiveSchema(BattleSchema):
        
        def SetUpFighter(self, fighter, **properties):
            fighter.SetPrioritiser(ActivePrioritiser(fighter))
            
        def GetMechanic(self):
            return ActiveBattleMechanic(self._battle)

        def GetAttackResolver(self):
            return ElementalAttackResolver()
            
        def GetPanner(self, battle):
            return SmoothPanner(battle)
    
    class SimpleTurnSchema(BattleSchema):
        
        def SetUpFighter(self, fighter, **properties):
            fighter.SetPrioritiser(TurnPrioritiser(fighter))
        
        def GetMechanic(self):
            return TurnBattleMechanic(self._battle)
        
        def GetAttackResolver(self):
            return DefaultAttackResolver()
        
        def GetPanner(self, battle):
            return SmoothPanner(battle)
    
    # CustomSchema allows people to use a particular Schema as a base, and then overlay their own replacement bits onto it.
    class CustomSchema (BattleSchema):
        
        def __init__(self, baseSchema, layers=None, mechanic=None, attackResolver=None, uiProvider=None, panner=None):
            self._schema = baseSchema()
            self._layers = layers
            self._mechanic = mechanic
            self._attackResolver = attackResolver
            self._uiProvider = uiProvider
            self._panner = panner
            
        def SetBattle(self, battle):
            self._battle = battle
            self._schema.SetBattle(battle)
        
        # Pass in the fighter instance rather than having separate methods to return each kind of thing a Fighter instance
        # needs - firstly for extensibility, secondly so we can check other properties on the instance and potentially make
        # decisions based on them.
        def SetUpFighter(self, fighter, **properties):
            self._schema.SetUpFighter(fighter, **properties)
        
        # Call to do any necessary initialisation on the battlefield itself.
        def SetUpBattlefield(self, battlefield):
            self._schema.SetUpBattlefield(battlefield)
            
        # Return a dictionary mapping the battle-relevant layer keys to layer indices in the reserved-for-battles layers.
        # More than one key can be mapped to a single layer, but all keys must be returned.
        def GetLayers(self):
            if (self._layers != None):
                return self._layers
            else:
                return self._schema.GetLayers()

        # Return a BattleMechanic to run the current battle with
        def GetMechanic(self):
            if (self._mechanic != None):
                return self._mechanic(self._battle)
            else:
                return self._schema.GetMechanic()
        
        # Get an AttackResolver that the current battle will use to determine how attacks fare and what happens
        def GetAttackResolver(self):
            if (self._attackResolver != None):
                return self._attackResolver()
            else:
                return self._schema.GetAttackResolver()
            
        # Get a UIProvider with which the current battle will present choices and other interface to the user
        def GetUIProvider(self):
            if (self._uiProvider != None):
                return self._uiProvider(self._battle)
            else:
                return self._schema.GetUIProvider()
            
        def GetPanner(self, battle):
            if (self._panner != None):
                return self._panner(battle)
            else:
                return self._schema.GetPanner(battle)
    
    ###
    # BattleMechanic
    # BattleMechanics determine the blow-by-blow flow of the battle, and are delegated with the duty of running the RunBattleRound method from Battle
    ###
    
    class BattleMechanic(object):
    
        def __init__(self, battle):
            self._battle = battle
            
        def SetUpFighter(self, fighter):
            None
        
        def RunBattleRound(self):
            return
        
        def RunFighterTurn(self, fighter):
            
            fighter._battle.PauseAsRequested()
            
            fighter._battle.PointOfInterest(position=fighter.Position, fighter=fighter)
            fighter.StartTurn()
            self._battle.FighterStartTurn(fighter)
            fighter.Act()
            # These should be taken care of by the various skills
            #fighter.EndTurn()
            #self._battle.FighterEndTurn(fighter)
            
            
    # In and Active Battle, everyone's priority goes up each tick, so between the ticks we need to start with the highest priority and check each Fighter;
    # Anyone with a priority over the threshold, we run their turn and then move on to the next Fighter.
    class ActiveBattleMechanic(BattleMechanic):
        
        def RunBattleRound(self):
            
            # Sort all fighters in descending order of priority
            fighters = self._battle.Fighters[:]
            fighters.sort(Battle_Priority_Compare)
            
            # For each fighter, if they're active and above the priority threshold (100), then perform their turn
            for fighter in fighters:
                if fighter.Active and fighter.Priority >= 100 and self._battle.On:
                    self.RunFighterTurn(fighter)
                    
    
    class TurnBattleMechanic(BattleMechanic):
        
        def RunBattleRound(self):
            
            # for each faction, perform a turn, one after another:
            for faction in self._battle.Factions:
                
                if self._battle.On == False:
                    return
                    
                self._battle.Show()
                
                self._battle.Announce("%(fac)s's Turn" % {"fac": faction})
                
                # get a list of fighters
                fighters = self._battle.FactionLists[faction][:]
                
                # loop while the fighter list isn't empty
                while len(fighters) > 0 and self._battle.On:
                    
                    # check that all fighters are still active:
                    for fighter in fighters[:]:
                        if fighter.Active == False:
                            fighters.remove(fighter)

                    
                    if len(fighters) == 0:
                        fighter = None
                    else:
                        if (faction in self._battle.PlayerFactions):
                            # First go through and check whether any of the fighters are non-player-controlled,
                            # and act with those ones automatically first.
                            nonPlayerFighters = [f for f in fighters if (f.PlayerControlled == False)]
                            
                            if len(nonPlayerFighters) > 0:
                                fighter = nonPlayerFighters[0]
                            else:
                                # If there aren't any non-Player-Controlled fighters left, let the player
                                # pick one to control.
                                fighter = self._battle.UI.PickFighter(fighters)
                        else:
                            fighter = renpy.random.choice(fighters)

                    if (fighter != None):
                        self.RunFighterTurn(fighter)
                        if fighter.TurnComplete:
                            fighters.remove(fighter)
                    else:
                        # If fighter == None, then either the list is empty or the user clicked the
                        # 'End Turn' button.
                        for f in fighters:
                            f.EndTurn()
                        fighters = []
    
    ###
    # AttackResolver
    # AttackResolvers work out how much damage a Fighter takes from a particular hit; parameters can be used to further influence the hit (e.g. passing type of hit, location, whatever.)
    ###
    
    class AttackResolver(object):
        
        def __init__(self):
            None
            
        def SetUpFighter(self, fighter):
            None
            
        def ResolveAttack(self, attacker, attack, multiplier, attributes, target, range=1, **parameters):
            None
    
    # DefaultAttackResolver is a very simple and deterministic resolver
    
    class DefaultAttackResolver(AttackResolver):
        
        def SetUpFighter(self, fighter):
            fighter.RegisterStat("Defence", 10)
            
        def ResolveAttack(self, attacker, attack, attributes, target, range=1):
            
            damage = 0
            
            #calculate damage - goes up more rapidly with zero or negative def
            if (target.Stats.Defence < 1):
                defence = 2 - target.Stats.Defence
                damage = attack * defence
            else:
                damage = (attack/target.Stats.Defence)+ 0.5

            damage = int(damage * 10)
                
            target.Damage(damage, attacker)
    class MyAttackResolver(AttackResolver):
        
        def SetUpFighter(self, fighter):
            fighter.RegisterStat("Might", 10)
            fighter.RegisterStat("Feel", 10)

            
            fighter.RegisterStat("Defence", 10)
            fighter.RegisterStat("Attack", 10)
            
            fighter.RegisterStat("Speech", 10)
            fighter.RegisterStat("Mind", 10)
            
            
            fighter.RegisterStat("MP", 10)
            
            fighter.RegisterStat("Health", 10)
            
            fighter.RegisterStat("Suport", 0)
            fighter.RegisterStat("Tactics", 0)
            fighter.RegisterStat("Hax", 1)
            
            fighter.RegisterStat("Move", 1)
            
            fighter.RegisterStat("Level", 1)
            fighter.RegisterStat("Chain", 0)
            
            fighter.RegisterStat("Infect",0)
            fighter.RegisterStat("Burn",0)
            
            #-----------Emotional----------------------------#
            
            fighter.RegisterStat("Powered", 0)
            fighter.RegisterStat("Used", 0)
            
            
        def ResolveAttack(self, attacker, attack, attributes, target, range=1):
            if attacker.Stats.Chain == 0 or attacker.Stats.Level == 1:
                pass
            damage = 0
            Critt = 0
            multiplier = 1
            Hitt = 1
            Hitt_bonus = 0
            Terrain = target.Position.Height
            #calculate damage - goes up more rapidly with zero or negative def
            r = (renpy.random.random()*20)
           
            #------Self Chain--------#
            attacker.Stats.Chain = 0
            
            #-------------Hitt Bonuses------------#
            if attacker.Stats.Move == attacker.BaseStats.Move:
                attacker._battle.Announce(attacker.Name + " Ambushes")
                Hitt_bonus = Hitt_bonus + attacker.Stats.Tactics
            if target.Stats.Move == 0:
                attacker._battle.Announce(target.Name + " is Exusted")
                Hitt_bonus = Hitt_bonus + attacker.Stats.Tactics
            
            if attacker.Facing == target.Facing:
                attacker._battle.Announce(target.Name + " BackStabs!")
                Hitt_bonus = Hitt_bonus + attacker.Stats.Tactics
            else:
                Hitt_bonus = Hitt_bonus
            if ('Emotion' in attributes):
                    if target.Stats.Used == 0:
                                multiplier = multiplier -0.75
                    if attacker.Stats.Powered == target.Stats.Used:
                                multiplier = multiplier + 1.5
                    if ('Heavy' in attributes):
                       
                            if attacker.Stats.Powered <= 3 and target.Stats.Used <= 3:
                                multiplier = multiplier
                                
                            else:
                                multiplier = multiplier -0.5
                    if ('Light' in attributes):
                            if attacker.Stats.Powered > 3 and target.Stats.Used > 3:
                                multiplier = multiplier 
                            else:    
                                multiplier = multiplier - 0.5
            else:
                #------Heavy------#
                if ('Anger' in attributes):
                    turns = 1
                if ('Sad' in attributes):
                    turns = 2
                if ('Terrify' in attributes):
                    turns = 3
                #-----------Light------#
                if ('Excite' in attributes):
                    turns = 4
                if ('Charm' in attributes):
                    turns = 5
                if ('Confuse' in attributes):
                    turns = 6
                if ('Curious' in attributes):
                    turns = 7
                else:
                    turns = 0

                attacker.AddEffect("UsedMarker", UsedMarkerEffect(attacker, turns))
                target.RemoveEffect("PowerMarker")
                target.AddEffect("PowerMarker", PowerMarkerEffect(target, turns))
            #-------------Hitting--------#
            if ('Attack' in attributes):
                if (r + attacker.Stats.Attack + target.Stats.Chain + Hitt_bonus) <= (target.Stats.Defence + Terrain):
                    Hitt = 0 #---------Miss-------
                else:
                    Hitt = 1
                    attacker._battle.Announce(" Attack Hitt!")
                    damage = damage
            if ('Speech' in attributes):
                if (r + attacker.Stats.Speech + target.Stats.Chain  + Hitt_bonus) <= (target.Stats.Mind + Terrain):
                    Hitt = 0 #---------Miss-------
                else:
                    Hitt = 1
                    damage = damage
            if ('Magic' in attributes):
                if (r + attacker.Stats.MP + target.Stats.Chain + Hitt_bonus) <= (target.Stats.MP + Terrain):
                    Hitt = 0 #---------Miss-------
                else:
                    Hitt = 1
                    attacker._battle.Announce(" The Spell Hitt!")
                    damage = damage
            if ('Emotion' in attributes):
                if attacker.Facing == target.Facing:
                    Terrain = Terrain + 12
                if attacker.Facing == "E" and target.Facing == "W":
                    Terrain = Terrain + 4
                if attacker.Facing == "W" and target.Facing == "E":
                    Terrain = Terrain + 4
                if attacker.Facing == "N" and target.Facing == "S":
                    Terrain = Terrain + 4
                if attacker.Facing == "S" and target.Facing == "N":
                    Terrain = Terrain + 4
                else:
                    Terrain = Terrain + 8
                    
                count = attacker.Stats.Hax
                
                while count > 10:
                    Hitt_bonus = Hitt_bonus +1
                    count = count -10
                count = target.Stats.Hax
                while count > 10:
                    Hitt_bonus = Hitt_bonus -1
                    count = count -10
                if r <= Terrain + Hitt_bonus:
                    Hitt = 0 #---------Miss-------
                else:
                    Hitt = 1
            #----------Critt/Hax------------#
            count = int(((renpy.random.random()*20) + attacker.Stats.Hax))
            while count > 19:
                
                Critt = Critt +1
                count = count -20
                
            attacker._battle.Announce(" Critt " +str(Critt)+" times!")   
            multiplier = multiplier + Critt
            #---------------Damage-------# 
            #damage = damage + self._multiplier 
            if Hitt == 1:
                
                #damage = int(damage)
                if ('Emotion' in attributes):
                    damage = (damage+ attacker.Stats.Feel)*multiplier
                else:
                    damage = (damage+ attacker.Stats.Might)*multiplier
                target.Damage(damage, attacker)
            else:
                damage = 0
                target.Damage(damage, attacker)
            #---------------Chain-------#   
            target.Stats.Chain = target.Stats.Chain + attacker.Stats.Suport
            
            
    class MyOtherAttackResolver(AttackResolver):
        
        def SetUpFighter(self, fighter):
            
            fighter.RegisterStat("Health", 10)
            
            fighter.RegisterStat("Suport", 1)
            fighter.RegisterStat("Hax", 1)
            
            fighter.RegisterStat("A_Air", 0)
            fighter.RegisterStat("Air", 0)
            
            fighter.RegisterStat("Lockpick", 0)
            fighter.RegisterStat("Break", 0)
            
            fighter.RegisterStat("Chain", 0)
            
            #-----------Emotional----------------------------#
            
            fighter.RegisterStat("Powered", 0)
            fighter.RegisterStat("Used", 0)
            
            
        def ResolveAttack(self, attacker, attack, attributes, target, range=1):
            damage = attack
            multiplier = 1
            attacker.Stats.Chain = 0
            Critt = 0
            if ('Emotion' in attributes):
                #---------emotional stadard modifier#
                multiplier = 0.5
                #----------Facing modifier#
                if attacker.Facing == target.Facing:
                    multiplier = multiplier - 0.25
                elif attacker.Facing == "E" and target.Facing == "W":
                    multiplier = multiplier + 0.5
                elif attacker.Facing == "W" and target.Facing == "E":
                    multiplier = multiplier + 0.5
                elif attacker.Facing == "N" and target.Facing == "S":
                    multiplier = multiplier + 0.5
                elif attacker.Facing == "S" and target.Facing == "N":
                    multiplier = multiplier + 0.5
                elif attacker.Facing == target.Facing:
                    multiplier = multiplier -0.25
                
            
                #----------respons modifier-------# 
                if target.Stats.Used == 0:
                    multiplier = multiplier -0.75
                    
                if attacker.Stats.Powered == target.Stats.Used:
                    
                    multiplier = multiplier + 0.5
                
                Powered = attacker.Stats.Powered
                Used = target.Stats.Used
                if ('Heavy' in attributes):
                                
                            #if attacker.Stats.Powered <= 3 and target.Stats.Used <= 3:
                                if ('Angry' in attributes):
                                    
                                    if Powered == 1:
                                        
                                        multiplier = multiplier +0.5
                                    if Used == 1:
                                        
                                        multiplier = multiplier + 0.5
                                    
                                if ('Sad' in attributes):
                                    if Powered == 2:
                                        multiplier = multiplier +0.5
                                    if Used == 2:
                                        multiplier = multiplier + 0.5
                                if ('Terrify' in attributes):
                                    if Powered == 3:
                                        multiplier = multiplier +0.5
                                    if Used == 3:
                                        multiplier = multiplier + 0.5
                                #----------attribute group check------------#        
                                if Used <= 3:
                                        multiplier = multiplier
                                if Powered <= 3:
                                        multiplier = multiplier
                                else:
                                        multiplier = multiplier -0.5
                                        
                                multiplier = multiplier
                                
                            
                if ('Light' in attributes):
                            #if attacker.Stats.Powered > 3 and target.Stats.Used > 3:
                                if ('Excite' in attributes):
                                    if Powered == 4:
                                        multiplier = multiplier +0.5
                                    if Used == 4:
                                        multiplier = multiplier + 0.5
                                if ('Charm' in attributes):
                                    if Powered == 5:
                                        multiplier = multiplier +0.5
                                    if Used == 5:
                                        multiplier = multiplier + 0.5
                                if ('Confuse' in attributes):
                                    if Powered == 6:
                                        multiplier = multiplier +0.5
                                    if target.Stats.Used == 6:
                                        multiplier = multiplier + 0.5
                                if ('Curious' in attributes):
                                    if Powered == 7:
                                        multiplier = multiplier +0.5
                                    if Used == 7:
                                        multiplier = multiplier + 0.5
                                #----------attribute group check------------#        
                                if Used > 3:
                                        multiplier = multiplier
                                if Powered > 3:
                                        multiplier = multiplier
                                #else:
                                 #       multiplier = multiplier -0.5
                                multiplier = multiplier
                #---------Suport Modifier of emotional modifier#                
                multiplier = multiplier* (1+(attacker.Stats.Suport /10))                
                #-----------Emotion marker-------------#
            else:
                #------Heavy------#
                if ('Angry' in attributes):
                    turns = 1
                if ('Sad' in attributes):
                    turns = 2
                if ('Terrify' in attributes):
                    turns = 3
                #-----------Light------#
                if ('Excite' in attributes):
                    turns = 4
                if ('Charm' in attributes):
                    turns = 5
                if ('Confuse' in attributes):
                    turns = 6
                if ('Curious' in attributes):
                    turns = 7
                

                attacker.AddEffect("UsedMarker", UsedMarkerEffect(attacker, turns))
                target.RemoveEffect("PowerMarker")
                target.AddEffect("PowerMarker", PowerMarkerEffect(target, turns))        
            #----------Critt-------------#
            if attacker.Facing == target.Facing:
                count = int(((renpy.random.random()*20) + (attacker.Stats.Hax*1.5)))+target.Stats.Chain
            else:
                count = int(((renpy.random.random()*20) + attacker.Stats.Hax))+target.Stats.Chain
            while count > 19:
                
                Critt = Critt +1
                count = count -20
             #-----Critt Mesage----#
            if Critt == 1:
                attacker._battle.Announce(" Hax! ")
            if Critt >1:
                attacker._battle.Announce(" Haxing " +str(Critt)+" times!")
            #------Hax Abilities--------#
            if ('Infect' in attributes):
                while Critt > 1:
                    Critt = Critt -1
                    target.Stats.Infect = target.Stats.Infect +1
                target.RemoveEffect("InfectEffect")
                target.AddEffect("InfectEffect", PowerMarkerEffect(target, 10))
            if ('Burn' in attributes):
                while Critt > 1:
                    Critt = Critt -1
                    target.Stats.Burn = target.Stats.Burn +1
                target.RemoveEffect("BurnEffect")
                target.AddEffect("BurnEffect", PowerMarkerEffect(target, 10))
            if ('Stun' in attributes):
                while Critt > 1:
                    Critt = Critt -1
                    
                    target.AddEffect("StunEffect", PowerMarkerEffect(target, 1))
            
            multiplier = multiplier +(Critt/2)
           
            #-------Anti Air----------#
            if ('Air' in target.Attributes) or target.Stats.Air > 0:
                if ('A_Air' in Attributes):
                    multiplier = multiplier +1
                multiplier = multiplier + attacker.Stats.A_Air
            #----loked and attacking objekt modefier------#
            if ('Objekt' in target.Attributes):
                damage = damage + attacker.stats.Break
            if ('Locked' in target.Attributes):
                damage = damage + attacker.stats.Lockpick
                multiplier = multiplier + attacker.stats.Lockpick
            #---------damge fixing-------#
            damage = damage * multiplier
            count = damage
            true_damage = 0
            while count > 0.9:
                count = count -1
                true_damage = true_damage +1
                
            if true_damage < 1:
                true_damage = 1
            target.Damage(true_damage, attacker)
            #target.Stats.Chain = target.Stats.Chain + attacker.Stats.Suport
            
    class ElementalAttackResolver(DefaultAttackResolver):
        
        def ResolveAttack(self, attacker, attack, attributes, target, range=1):
            
            multiplier = 1.0
            
            if ('fire' in attributes):
                if ('water' in target.Attributes):
                    multiplier = multiplier * 0.5
                if ('earth' in target.Attributes):
                    multiplier = multiplier * 4.0
                if ('fire' in target.Attributes):
                    multiplier = 0
            if ('water' in attributes):
                if ('earth' in target.Attributes):
                    multiplier = multiplier * 0.5
                if ('fire' in target.Attributes):
                    multiplier = multiplier * 4
                if ('water' in target.Attributes):
                    multiplier = 0
            if ('earth' in attributes):
                if ('fire' in target.Attributes):
                    multiplier = multiplier * 0.5
                if ('water' in target.Attributes):
                    multiplier = multiplier * 4
                if ('earth' in target.Attributes):
                    multiplier = 0

            damage = 0
            
            #calculate damage same as usual
            if (target.Stats.Defence < 1):
                defence = 2 - target.Stats.Defence
                damage = attack * defence
            else:
                damage = (attack/target.Stats.Defence)+ 0.5
                
            # Get a random number between 0.8 and 1.2
            random = (renpy.random.random() * 0.4) + 0.8

            damage = int(float(damage) * multiplier * 10 * random)
            
            target.Damage(damage, attacker)
            
    class SkillBasedAttackResolver(ElementalAttackResolver):
        
        def SetUpFighter(self, fighter):
            fighter.RegisterStat('Skill', 75)
            
        def ResolveAttack(self, attacker, attack, attributes, target, range=1, **parameters):
            
            #Check skill - which is a percentage chance of hitting
            if ((renpy.random.random()*100) <= attacker.Stats.Skill):
                # it's a hit, so we perform the attack as normal
                super(SkillBasedAttackResolver, self).ResolveAttack(attacker, attack, attributes, target, range=range, **parameters)
            else:
                # it's a miss, so we announce this to the user
                attacker._battle.Announce(attacker.Name + " missed!")
                
    ###
    # BattlePanner
    # A Panner is responsible for providing the implementation of the pan/offset function.
    ###
    
    class BattlePanner(object):
        def __init__(self, battle):
            self._battle = battle
            
        def Pan(self, transform, st, at):
            return 0
            
        def OnPan(self):
            None
            
        def Reset(self):
            None
            
    class DefaultPanner(BattlePanner):
            
        def Pan(self, transform, st, at):
            transform.xoffset =  0 - self._battle.CameraX
            transform.yoffset = 0 - self._battle.CameraY
            
            return 0.1
            
    class SmoothPanner(BattlePanner):
        
        def __init__(self, battle, period=0.25):
            super(SmoothPanner, self).__init__(battle)
            
            self._battle = battle
            
            self.Reset()
            
            self._period = period/2

        def OnPan(self):
            self._panned = True
            self._originX = self._currentX
            self._originY = self._currentY
            
            #renpy.force_full_redraw()
            #renpy.restart_interaction()
            
        def Pan(self, transform, st, at):
            if self._panned:
                self._timeOffset = time.clock()
                self._panned = False
                
            diff = (time.clock() - self._timeOffset) / (self._period)
            
            if diff >= 1:
                t = 1
            elif diff < 0: # Probably a loaded save, so reset so it doesn't randomly pan in the future
                t = 1
                self._timeOffset = time.clock() - 5
            else:
                t = diff
                
            x = ((self._battle.CameraX - self._originX) * t) + self._originX
            y = ((self._battle.CameraY - self._originY) * t) + self._originY
            
            self._currentX = x
            self._currentY = y
            transform.xoffset = 0-x
            transform.yoffset = 0-y
            
            if diff >= 1:
                return 0.1
            else:
                return 0
                
        def Reset(self):

            self._originX = self._battle.CameraX
            self._originY = self._battle.CameraY
            
            self._currentX = self._battle.CameraX
            self._currentY = self._battle.CameraY
            
            self._timeOffset = 0
            self._panned = False

