# # # # # # # # # # # # # # # # # # # # # #
#    Homework Assignment #2: Functions    #
# # # # # # # # # # # # # # # # # # # # # #

"""
What's your favorite song?
Using the information from homework #1,
create 3 functions with the same name of 3
attributes you used on the previous homework.
Whenever you call that function, it should
return the corresponding value for that attribute.

For extra credit, you can create a function
that returns a boolean instead of a String or a
Number.
"""

### Functions definition
def song ():
    song = 'Runaway Baby'
    return(song)
    
def artist():
    artist = 'Bruno Mars'
    return(artist)

def album():
    album = 'Doo-Woops & Hooligans'
    return(album)

def composers():
    composer1, composer2, composer3, composer4 = 'Bruno Mars', 'Philip Lawrence', 'Ari Levine', 'Brody Brown'
    return('{0}, {1}, {2} & {3}'.format(composer1, composer2, composer3, composer4))

def release_date():
    day = 4
    month = 'October'
    year = 2010
    return('{0}/{1}/{2}'.format(month, day, year))

def is_a_hit():
    return(True)

def duration_in_minutes():
    duration_in_minutes = 2.45
    return(duration_in_minutes)

def last_more_than(minutes):
    return(duration_in_minutes() > minutes)

def duration_in_seconds():
    duration_in_seconds = 147
    return(duration_in_seconds)

def last_less_than(seconds):
    return(duration_in_seconds() < seconds)


### Functions Calling
print('Song', song())
print('Artist:', artist())
print('Album:', album())
print('Composers:', composers())
print('Release date:', release_date())
print(f'Is the song "{song()}" a hit?', is_a_hit())
print('Duration in minutes:', duration_in_minutes())
print('Does the song last more than 3 minutes?',last_more_than(3))       # 3 minutes
print('Does the song last more than 2 minutes?',last_more_than(2))       # 2 minutes
print('Duration in seconds:', duration_in_seconds())
print('Does the song last more than 120 seconds?',last_less_than(120))     # 120 seconds
print('Does the song last more than 150 seconds?',last_less_than(150))     # 150 seconds