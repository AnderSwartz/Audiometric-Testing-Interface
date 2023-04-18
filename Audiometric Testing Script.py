from openexp.canvas import Canvas
import pygame.mixer as mixer
import random

mixer.init()
sound_file = 'C:\\Downloads\\audiometric_testing\\250Hz_44100Hz_16bit_05sec.mp3'
mixer.music.load(sound_file)
# print("a")

# # Create a canvas object
# my_canvas = Canvas(exp)

# my_canvas.text("testing")


# my_canvas.show()
# print("d")


# clock.sleep(1000)

# # Import the necessary modules


# # Initialize the mixer
# mixer.init()

# # Load the sound file
# sound_file = 'C:\\Downloads\\audiometric_testing\\250Hz_44100Hz_16bit_05sec.mp3'
# mixer.music.load(sound_file)

# # Play the sound
# mixer.music.play()
# # Import the necessary modules
# my_keyboard = Keyboard(keylist=['z', 'x'], timeout=1000)
# start_time = clock.time()
# key, end_time = my_keyboard.get_key()
# var.response = key
# var.response_time = end_time - start_time


# my_canvas = Canvas(exp)

# my_canvas.text(key)


# my_canvas.show()

# clock.sleep(1000)

#This script contains the relavant OpenSesame commands

#This script contains the relavant OpenSesame commands

freqs = list(range(1000, 2001, 1000))
# freqs.append(500)
# freqs.append(250)
scores = {}

my_canvas = Canvas(exp)

my_canvas.text("running prototype...")


my_canvas.show()
clock.sleep(1000)

for freq in freqs:
    
    hits = {}
    attempts = {}
    # print(hits)
    # print(attempts)
    hits[0] = 0 #probably dont need these anymore
    attempts[0] = 0
    amp = 0
    
    #This starts as False because we want to first trial to count
    new_ascending_presentation = False 
    #When it is True, that means we just went down 10 dbs, and we
    #dont want to count the next presentation as a hit or an attempt

    prev_hit = False
    attempts[-5] = 0
    while (prev_hit and attempts[amp+10] < 3) or (prev_hit and attempts[amp+10] >= 3 and hits[amp+10] / attempts[amp+10] < .5) or (not prev_hit and attempts[amp-5] < 3) or (not prev_hit and attempts[amp-5] >= 3 and hits[amp-5] / attempts[amp-5] < .5):
        prev_hit = False
        
        mixer.init()
        
        
        sound_path = 'C:\\Downloads\\audiometric_testing\\stimuli\\'+str(freq)+'hz'+str(amp)+'db.wav'
        # sound_file = 'C:\\Downloads\\audiometric_testing\\250Hz_44100Hz_16bit_05sec.mp3'
        sound = mixer.Sound(sound_path)
        # mixer.music.load(sound_file)
        # mixer.music.play()
        sound.play()
        
        my_canvas = Canvas(exp)
        
        my_canvas.text("Playing frequency "+str(freq)+  "hz at amplitude of " +str(amp) + "db")
        my_canvas.show()
        
        
        #wait for sound to finish playing (each should be 1 sec)
        clock.sleep(1000)
    
        
        #use key '1' instead?
        my_keyboard = Keyboard(keylist=['5'], timeout=3000)
        user_input, end_time = my_keyboard.get_key()
        
        my_canvas = Canvas(exp)
        my_canvas.text(user_input)
        my_canvas.show()
        
        if not new_ascending_presentation:
            if amp in attempts:
                attempts[amp] +=1
            else:
                attempts[amp] =1
        if user_input == "y":
            if not new_ascending_presentation:
                if amp in hits:
                    hits[amp] += 1
                else:
                    hits[amp] = 1
            prev_hit = True
            amp -= 10
            new_ascending_presentation = True
        else:
            if amp not in hits:
                hits[amp] = 0
            amp += 5
            new_ascending_presentation = False
        if amp not in attempts:
            attempts[amp] = 0
            
            
            
        #wait between presentations 2 seconds +- 1 second
       
        random_wait = random.randint(2000, 4000)
        clock.sleep(random_wait)
        
        # print(attempts)
        # print(hits)
        
        # print("prev_hit",prev_hit)
        # print("hits",hits)
        # print("attempts",attempts)
        # if(prev_hit):
        #     print(prev_hit and attempts[amp+10] < 3)
        #     print(prev_hit and attempts[amp+10] >= 3 and hits[amp+10] / attempts[amp+10] < .5)
        # else:
        #     print(not prev_hit and attempts[amp-5] < 3)
        #     print(not prev_hit and attempts[amp-5] >= 3 and hits[amp-5] / attempts[amp-5] < .5)
    if prev_hit:
        scores[str(freq)+"hz"] = str(amp+10)+"db"
    else:
        scores[str(freq)+"hz"] = str(amp-5)+"db"
    print(scores)
    
    
# print(scores)
log.write(scores)