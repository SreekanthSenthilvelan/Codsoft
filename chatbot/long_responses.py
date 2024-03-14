import random

R_LIFE = "Well,The purpose of our Life is to stay happy with lovable bond around us."
R_FITNESS = "Variety is the spice of life,Cardio and weight training ia a very effective way to keep healthy."
R_LOVE = "iam so glad to hear this from you,but as a AI program i can't able to do anything,anyway thank you."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response