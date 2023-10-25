class Char:
    armor_class = 10
    hit_points = 5
    name = ""
    

    
    def __init__(self, name, align):
        self.name = name
        self.align = align
        
    def declare_attack(self, defender, roll):
        if roll >= defender.armor_class:
            defender.hit_points -= 1
        elif roll == 20:
            defender.hit_points -= 2
        
            
