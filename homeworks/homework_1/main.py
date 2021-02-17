# # # # # # # # # # # # # # # # # # # # # #
#    Homework Assignment #1: Variables    #
# # # # # # # # # # # # # # # # # # # # # #

"""
What's your favorite song?
For this assignment I needed to describe all
the meta data of my favorite song.

Each attribute was define into a variable
and then printed into the console.
"""

### Attributes
song = 'Runaway Baby'
artist = 'Bruno Mars'
album = 'Doo-Woops & Hooligans'
composer1, composer2, composer3, composer4 = 'Bruno Mars', 'Philip Lawrence', 'Ari Levine', 'Brody Brown'
genre1, genre2, genre3 = 'Soul', 'Funk', 'Pop rock'
label = 'Atlantic, Elektra'
producer = 'The Smeezingtons'  
# Release date
day = 4
month = 'October'
year = 2010
# Other attributes
duration_in_seconds = 147
duration_in_minutes = 2.45
cost_in_USD = 1.38
billboard_UK, billboard_NZ, billboard_Hot100 = 19, 35, 50

### Printing all the attributes
print(song)
print(artist)
print(album)
print('Composers:')
print(composer1)
print(composer2)
print(composer3)
print(composer4)
print('Genres:')
print(genre1)
print(genre2)
print(genre3)
print('Label: ',label)
print('Producer:', producer)
print('Release date:',month, '/',day, '/', year)
print('Duration in seconds:', duration_in_seconds)
print('Duration in minutes:', duration_in_minutes)
print('Cost in Amazon $', cost_in_USD, 'USD')
print('Billboard UK:', billboard_UK)
print('Billboard NZ:', billboard_NZ)
print('Billboard Hot 100:', billboard_Hot100)

