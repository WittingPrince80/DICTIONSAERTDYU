from tkinter import*


root=Tk()
root.title("Dictionary")
root.geometry("600x600")


random = Label(root)

dictionary = {'Unbraking': 'It has a chance not to break a bit.',
              'Mending': 'Exp = fix it, infinite stuff, best enchant',
              'Sharpness': 'Swords be sharp',
              'Fire Aspect': 'Fire swords go brrrr',
              'Knockback': 'Swords Knockback victims',
              'Swepping Edge': 'Swords that sweep have sharp edge',
              'Power': 'Bows be strong',
              'Flame': 'Arrows on fire',
              'Punch': 'Arrow punch victim back... a lot',
              'Infinity': 'Arrow consurviture go brrrrr #minecraft logic',
              'Smite': 'More sharp swords but for dead monters',
              'Bane of arethrapods' : 'NO, NO, NO, WORST ENCHANT',
              'Protection' : 'Protection',
              'Fire Protection' : 'Hotness protection',
              'Projectile Protection' : 'Air attack protection',
              'Blast Protection': 'Boom protection',
              'Aqua Affinity' : 'Normal speed water break',
              'Resperation': 'Good at holding breath',
              'Deapth Strider': 'Olympic swimmerness',
              'Frost Walker': 'Couse the cold never bother me anyway, for water',
              'Feather Falling': ' Can jump of a skyscraper and live #minecraft logic'
              }
             
def enchant():
  
    random["text"] = dictionary['Infinity']
              
    
    button_enchant = Button(root,text = "Random Enchants Meaning",command = enchant)
    button_enchant.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    random.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
    root.mainloop()


