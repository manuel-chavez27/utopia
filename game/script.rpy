# The script of the game goes in this file.
# The game starts here.

##----------------
## Animations
##----------------
define transition_dissolve = Dissolve(1)
define scene_fade = Fade(1, 1, 1, color="000")

##----------------
## Music
##----------------
define audio.facing_uncomfort = "audio/music/Facing_Uncomfort.mp3"
define audio.gates_of_oase = "audio/music/Gates_Of_Oase.mp3"

##----------------
## SFX
##----------------

##----------------
## Utils
##----------------
define yellowTextbox = False
define redTextbox = False
define greenTextbox = False

define textbox = "Narration"
define textboxColor = 'Yellow'

define yellowTextBoxCharacter = False

define gui.name_xpos = 65
define gui.name_ypos = 10
define gui.name_text_size = 24

define gui.dialogue_xpos = 30

style textbox:
    spacing 100

#Make the character darken if not speaking
transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4e4e4eb2") * SaturationMatrix(1.0)

#Make the character brighter if speaking
transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

#Flip the character if it is on the left side
transform flip:
    xzoom -1.0

##----------------
## Characters
##----------------
#Man Silhouette
define hs = Character("Husband", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image hs base = "Characters/Silhouette/Unknown_Man_Silhouette.png"

#Woman Silhouette
define ws = Character("Wife", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image ws base = "Characters/Silhouette/Unknown_Woman_Silhouette.png"

#Common Soldiers
define cso = Character("Oase Soldier", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image cso base serious = "Characters/Common_Soldiers/Oase_Soldiers/OS_Base_Serious_Expression.png"
image cso talking serious = "Characters/Common_Soldiers/Oase_Soldiers/OS_Talking_Serious_Expression.png"
image cso scared = "Characters/Common_Soldiers/Oase_Soldiers/OS_Scared_Expression.png"
image cso shouting = "Characters/Common_Soldiers/Oase_Soldiers/OS_Shouting_Expression.png"

#Frederick Marcus
define fm = Character("Frederick Marcus", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "frederick", color="#FFF")
image fc base serious = "Characters/Frederick_Marcus/Casual/FC_Base_Serious_Expression.png"
image fc base happy = "Characters/Frederick_Marcus/Casual/FC_Base_Happy_Expression.png"
image fc talking serious = At("Characters/Frederick_Marcus/Casual/FC_Talking_Serious_Expression.png",sprite_highlight('frederick'))
image fc talking happy = At("Characters/Frederick_Marcus/Casual/FC_Talking_Happy_Expression.png",sprite_highlight('frederick'))
image fc ate hot food = "Characters/Frederick_Marcus/Casual/FC_Ate_Hot_Food_Expression.png"
image fc grunting pained = "Characters/Frederick_Marcus/Casual/FC_Grunting_Pained_Expression.png"
image fc shy = "Characters/Frederick_Marcus/Casual/FC_Shy_Embarrassed_Expression.png"
image fc frustrated = "Characters/Frederick_Marcus/Casual/FC_Frustrated_Expression.png"
image fc depressed = "Characters/Frederick_Marcus/Casual/FC_Depressed_Expression.png"
image fc angry = "Characters/Frederick_Marcus/Casual/FC_Angry_Expression.png"

#Constantine Appius
define ca = Character("Constantine Appius", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "constantine", color="#FFF")
image ca base serious = "Characters/Constantine_Appius/CA_Base_Serious_Expression.png"
image ca base happy = "Characters/Constantine_Appius/CA_Base_Happy_Expression.png"
image ca talking serious = "Characters/Constantine_Appius/CA_Talking_Serious_Expression.png"
image ca talking happy = "Characters/Constantine_Appius/CA_Talking_Happy_Expression.png"

define tm = Character("Tall Man", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "tall", color="#FFF")
image tm base happy = "Characters/Constantine_Appius/CA_Base_Happy_Expression.png"
image tm talking happy = "Characters/Constantine_Appius/CA_Talking_Happy_Expression.png"

#Blacksmith Jude
define bj = Character("Blacksmith Jude", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "blacksmith", color="#FFF")
image bj base serious = "Characters/Blacksmith_Jude/BJ_Base_Serious_Expression.png"
image bj talking serious = "Characters/Blacksmith_Jude/BJ_Talking_Serious_Expression.png"
image bj excited = "Characters/Blacksmith_Jude/BJ_Excited_Expression.png"
image bj sad = "Characters/Blacksmith_Jude/BJ_Sad_Expression.png"

#Emilia Annot
define ea = Character("Emilia Annot", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "emilia", color="#FFF")
image ed base serious = "Characters/Emilia_Annot/Dress/ED_Base_Serious_Expression.png"
image ed base happy = "Characters/Emilia_Annot/Dress/ED_Base_Happy_Expression.png"
image ed talking serious = "Characters/Emilia_Annot/Dress/ED_Talking_Expression_Serious.png"
image ed talking happy = "Characters/Emilia_Annot/Dress/ED_Talking_Expression_Happy.png"
image ed angry = "Characters/Emilia_Annot/Dress/ED_Angry_Expression.png"
image ed comforting = "Characters/Emilia_Annot/Dress/ED_Comforting_Expression.png"
image ed empathetic = "Characters/Emilia_Annot/Dress/ED_Empathetic_Expression.png"
image ed playful = "Characters/Emilia_Annot/Dress/ED_Playful_Expression.png"
image ed pouting = "Characters/Emilia_Annot/Dress/ED_Pouting_Expression.png"
image ed shy = "Characters/Emilia_Annot/Dress/ED_Shy_Embarrassed_Expression.png"

#Horace Annot
define ha = Character("Horace Annot", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "horace", color="#FFF")
image ha base serious = "Characters/Horace_Annot/HA_Base_Serious_Expression.png"
image ha base happy = "Characters/Horace_Annot/HA_Base_Happy_Expression.png"
image ha talking serious = "Characters/Horace_Annot/HA_Talking_Serious_Expression.png"
image ha talking happy = "Characters/Horace_Annot/HA_Talking_Happy_Expression.png"
image ha angry = "Characters/Horace_Annot/HA_Angry_expression.png"
image ha coughing = "Characters/Horace_Annot/HA_Coughing_Expression.png"
image ha grim_look = "Characters/Horace_Annot/HA_Grim_Look_On_Hand.png"
image ha laughing = "Characters/Horace_Annot/HA_Laughing_Expression.png"
image ha sad = "Characters/Horace_Annot/HA_Sad_Expression.png"
image ha thinking = "Characters/Horace_Annot/HA_Thinking_Expression.png"

#Ulrick Marcus
define um = Character("Ulrick Marcus", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "ulrick", color="#FFF")
image um base serious = "Characters/Ulrick_Marcus/UM_Base_Serious_Expression.png"
image um talking serious = "Characters/Ulrick_Marcus/UM_Talking_Serious_Expression.png"
image um angry = "Characters/Ulrick_Marcus/UM_Angry_Expression.png"
image um crying = "Characters/Ulrick_Marcus/UM_Crying_Expression.png"
image um frustrated = "Characters/Ulrick_Marcus/UM_Frustrated_Expression.png"
image um happy = "Characters/Ulrick_Marcus/UM_Happy_Expression.png"
image um questioning = "Characters/Ulrick_Marcus/UM_Questioning_Playful_Expression.png"

#Volker Marcus
define vm = Character("Volker Marcus", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "volker", color="#FFF")
image va base serious = "Characters/Volker_Marcus/armor/VA_Base_Serious_Expression.png"
image va talking serious = "Characters/Volker_Marcus/armor/VA_Talking_Serious_Expression.png"
image va dying = "Characters/Volker_Marcus/armor/VA_Dying_Expression.png"
image va happy = "Characters/Volker_Marcus/armor/VA_Happy_Expression.png"
image va scared = "Characters/Volker_Marcus/armor/VA_Scared_Expression.png"
image va shouting = "Characters/Volker_Marcus/armor/VA_Shouting_Expression.png"

#Anja Klein
define ak = Character("Anja Klein", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "anja", color="#FFF")
image ak angry assassin = "Characters/Anja_Klein/A_Angry_Assasin_Look_Expression.png"
image ak base happy = "Characters/Anja_Klein/A_Base_Happy_Expression.png"
image ak crying = "Characters/Anja_Klein/A_Crying_Expression.png"
image ak sad = "Characters/Anja_Klein/A_Sad_Expression.png"
image ak talking happy= "Characters/Anja_Klein/A_Talking_Happy_Expression.png"

#Ambrus Cadman
define ac = Character("Ambrus Cadman", windows_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), callback = name_callback, cb_name = "ambrus", color="#FFF")
image aa base serious = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Base_Serious_Expression.png"
image aa talking serious = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Talking_Serious_Expression.png"
image aa confident = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Confident_Expression.png"
image aa decapitated = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Decapitated_Expression.png"
image aa helmet = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Helmet_Expression.png"
image aa intimidating = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Intimidating_Expression.png"
image aa laughing = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Laughing_Expression.png"
image aa manical clean = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Manical_Smile_Clean_Expression.png"
image aa manical = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Maniacal_Smile_Expression.png"
image aa nohand = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_No_Hand_Expression.png"
image aa nohand blood = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_No_Hand_Expression_Blood.png"
image aa regenerated hand = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Regenarated_Hand_Expression.png"
image aa regenerating head = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Regenarating_Head_Expression.png"
image aa shouting = "Characters/Ambrus_Cadman/Ambrus_Armor/AA_Shouting_Expression.png"
#Ambrus Cadman Aura
image aaa base serious = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Base_Serious_Expression.png"
image aaa talking serious = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Talking_Serious_Expression.png"
image aaa confident = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Confident_Expression.png"
image aaa decapitated = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Decapitated_Expression.png"
image aaa helmet = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Helmet_Expression.png"
image aaa intimidating = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Intimidating_Expression.png"
image aaa laughing = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Laughing_Expression.png"
image aaa manical clean = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Manaical_Smile_Clean_Expression.png"
image aaa manical = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Maniacal_Smile_Expression.png"
image aaa nohand = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_No_Hand_Expression.png"
image aaa nohand blood = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_No_Hand_Expression_Blood.png"
image aaa regenerated hand = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Regenarated_Hand_Expression.png"
image aaa regenerating head = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Regenarating_Head.png"
image aaa shouting = "Characters/Ambrus_Cadman/Ambrus_Armor_Aura/AAA_Shouting_Expression.png"
#Ambrus Nude Aura
image ana base serious = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Base_Serious_Expression.png"
image ana talking serious = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Talking_Serious_Expression.png"
image ana confident = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Confident_Expression.png"
image ana decapitated = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Decapitated_Expression.png"
image ana intimidating = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Intimidating_Expression.png"
image ana laughing = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Laughing_Expression.png"
image ana maniacal clean = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Maniacal_Smile_Clean_Expression.png"
image ana maniacal = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Maniacal_Smile_Expression.png"
image ana nohand = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_No_Hand_Expression.png"
image ana nohand blood = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_No_Hand_Expression_Blood.png"
image ana regenerated hand = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Regenarated_Hand_Expression.png"
image ana regenerating head = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Regenarating_Head_Expression.png"
image ana shouting = "Characters/Ambrus_Cadman/Ambrus_Nude_Aura/ANA_Shouting_Expression.png"

label start:

    #Transition Background Chapter 0
    jump ch0

    # This ends the game.

    return
