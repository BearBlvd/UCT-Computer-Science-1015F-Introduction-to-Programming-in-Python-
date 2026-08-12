#Oyama Nongcula 
#NNGOYA001
#CSC1015F Assignment 3B

print("""Welcome to the Biology Expert
------------------------------------------------------------------
Answer the following questions by selecting from among the options.""")

Back_bone=input("Does the organism have a backbone? (yes/no):\n")
animal=""

if Back_bone.lower()=="yes":

    is_warm_blooded=input("Is it warm-blooded? (yes/no):\n")

    if is_warm_blooded.lower()=="yes":

        has_feathers=input("Does it have feathers? (yes/no):\n")
    
        if has_feathers.lower()=="yes":
            animal="It is a Bird."
        else:

            has_fur=input("Does it have fur? (yes/no):\n")

            if has_fur.lower()=="yes":
                animal="It is a Mammal."
            else:
                animal="Other vertebrate."

    else:
        has_scales=input("Does it have scales? (yes/no):\n")

        if has_scales.lower()=="yes":

            lives_underwater=input("Does it live in water? (yes/no):\n")

            if lives_underwater.lower()=="yes":
                animal="It is a fish."
            else:
                animal="It is a Reptile."
        else:
            animal="It is an Amphibian." 
else:
    has_skeleton=input("Does it have an exoskeleton? (yes/no):\n") 

    if has_skeleton.lower()=="yes":
        has_six_legs=input("Does it have six legs? (yes/no):\n")

        if has_six_legs.lower()=="yes":
            animal="It is an Insect."
        else:
            has_eight_legs=input("Does it have eight legs? (yes/no):\n")

            if has_eight_legs.lower()=="yes":
                animal="It is an Arachnid."
            else:
                animal="It is a Crustacean"
    else:
        has_segmented_body=input("Does it have a segmented body? (yes/no):\n")

        if has_segmented_body.lower()=="yes":
            animal="It is an Annelid (e.g., Earthworm)."
        else:
            animal="It is a Mollusc."

            has_shell=input("Does it have a shell? (yes/no):\n")
            if has_shell.lower()=="yes":
                animal="It is a Snail or Clam."
            else:
                animal="It is an Octopus or Squid."
print(f"{animal}")
