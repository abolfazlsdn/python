def meditate(mana, max_mana, energy, energy_drinks):
    while mana <= max_mana or energy_drinks ==0:
          if energy > 0 :
               mana+=1
               energy-=1
          elif energy_drinks>0:
               energy_drinks-=1
               energy+=50
    return mana,energy,energy_drinks

print(meditate(5,10,0,1))
          
