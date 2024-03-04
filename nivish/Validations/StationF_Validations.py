def check_Skin_colour_Tone(request):
    Skin_colour_Tone = request.data.get('Skin_colour_Tone')
    Skin_colour_Tone_Abnormal = request.data.get('Skin_colour_Tone_Abnormal')

    if Skin_colour_Tone == 'Abnormal':
        if  Skin_colour_Tone_Abnormal == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Skin_colour_Tone_Abnormal']= None

def check_Skin_Texture_of_Skin(request):
    Skin_Texture_of_Skin = request.data.get('Skin_Texture_of_Skin')
    Skin_Texture_of_Skin_Abnormal =request.data.get('Skin_Texture_of_Skin_Abnormal')

    if Skin_Texture_of_Skin == 'Abnormal':
         if  Skin_Texture_of_Skin_Abnormal == None :
            raise Exception("you have select anyone")
    else:
        request.data['Skin_Texture_of_Skin_Abnormal']=None


def check_skin_Rash(request):
    skin_Rash =request.data.get('skin_Rash')
    skin_Rash_Present = request.data.get('skin_Rash_Present')
    skin_Rash_Present_Face = request.data.get('skin_Rash_Present_Face')
    skin_Rash_Present_Neck = request.data.get('skin_Rash_Present_Neck')
    skin_Rash_Present_Chest = request.data.get('skin_Rash_Present_Chest')
    skin_Rash_Present_Abdomen = request.data.get('skin_Rash_Present_Abdomen')
    skin_Rash_Present_Groin = request.data.get('skin_Rash_Present_Groin')
    skin_Rash_Present_Back = request.data.get('skin_Rash_Present_Back')
    skin_Rash_Present_Arms = request.data.get('skin_Rash_Present_Arms')
    skin_Rash_Present_Hands = request.data.get('skin_Rash_Present_Hands')
    skin_Rash_Present_Legs = request.data.get('skin_Rash_Present_Legs')
    skin_Rash_Present_Feet = request.data.get('skin_Rash_Present_Feet')
    

    if skin_Rash == 'Present':
        if skin_Rash_Present == None:
            raise Exception("you have select anyone")
        selected_values = request.data.get('skin_Rash_Present', '').split(',')

        # Initialize variables to store the values for each option
        Face_value = None
        Neck_value = None
        Chest_value = None
        Abdomen_value = None
        Groin_value = None
        Back_value = None
        Arms_value = None
        Hands_value = None
        Legs_value = None
        Feet_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Face":
                Face_value = skin_Rash_Present_Face
            elif i == "Neck":
                Neck_value = skin_Rash_Present_Neck
            elif i == "Chest":
                Chest_value = skin_Rash_Present_Chest
            elif i == "Abdomen":
                Abdomen_value = skin_Rash_Present_Abdomen
            elif i == "Groin":
                Groin_value = skin_Rash_Present_Groin
            elif i == "Back":
                Back_value = skin_Rash_Present_Back
            elif i == "Arms":
                Arms_value = skin_Rash_Present_Arms
            elif i == "Hands":
                Hands_value = skin_Rash_Present_Hands
            elif i == "Legs":
                Legs_value = skin_Rash_Present_Legs
            elif i == "Feet":
                Feet_value = skin_Rash_Present_Feet

        # Set the values for each option in the request data
        request.data['skin_Rash_Present_Face'] = Face_value
        request.data['skin_Rash_Present_Neck'] = Neck_value
        request.data['skin_Rash_Present_Chest'] = Chest_value
        request.data['skin_Rash_Present_Abdomen'] = Abdomen_value
        request.data['skin_Rash_Present_Groin'] = Groin_value
        request.data['skin_Rash_Present_Back'] = Back_value
        request.data['skin_Rash_Present_Arms'] = Arms_value
        request.data['skin_Rash_Present_Hands'] = Hands_value
        request.data['skin_Rash_Present_Legs'] = Legs_value
        request.data['skin_Rash_Present_Feet'] = Feet_value
        
    else:
        request.data['skin_Rash_Present']=None
        request.data['skin_Rash_Present_Face']=None
        request.data['skin_Rash_Present_Neck']=None
        request.data['skin_Rash_Present_Chest']=None
        request.data['skin_Rash_Present_Abdomen']=None
        request.data['skin_Rash_Present_Groin']=None
        request.data['skin_Rash_Present_Back']=None
        request.data['skin_Rash_Present_Arms']=None
        request.data['skin_Rash_Present_Hands']=None
        request.data['skin_Rash_Present_Legs']=None
        request.data['skin_Rash_Present_Feet']=None

def check_Other_Skin_lesions(request):
    Other_Skin_lesions =request.data.get('Other_Skin_lesions')
    Other_Skin_lesions_Yes = request.data.get('Other_Skin_lesions_Yes')
    Other_Skin_lesions_Yes_Other = request.data.get('Other_Skin_lesions_Yes_Other')
    Other_Skin_lesions_Yes_Birth_marks = request.data.get ('Other_Skin_lesions_Yes_Birth_marks')
    Other_Skin_lesions_Yes_Birth_marks_Other = request.data.get('Other_Skin_lesions_Yes_Birth_marks_Other')
    if Other_Skin_lesions == 'Yes':
        if Other_Skin_lesions_Yes == None:
            raise Exception("you have select anyone")
        selected_values = request.data.get('Other_Skin_lesions_Yes', '').split(',')
        Birth_marks_value = None
        Other_value = None
        Birth_Other_value = None
        for i in selected_values:
            if i == "Other":
                Other_value = Other_Skin_lesions_Yes_Other
        request.data['Other_Skin_lesions_Yes_Other'] = Other_value
        for i in selected_values:
            if i == "Birth marks":
                Birth_marks_value = Other_Skin_lesions_Yes_Birth_marks
                selected_values = request.data.get('Other_Skin_lesions_Yes_Birth_marks', '').split(',')
                Birth_Other_value = None
                for j in selected_values:
                    if j == "Other":
                        Birth_Other_value = Other_Skin_lesions_Yes_Birth_marks_Other
                request.data['Other_Skin_lesions_Yes_Birth_marks_Other'] = Birth_Other_value

        request.data['Other_Skin_lesions_Yes_Birth_marks'] = Birth_marks_value
        request.data['Other_Skin_lesions_Yes_Birth_marks_Other'] = Birth_Other_value
    else:
        request.data['Other_Skin_lesions_Yes']=None
        request.data['Other_Skin_lesions_Yes_Birth_marks']=None
        request.data['Other_Skin_lesions_Yes_Other']=None
        request.data['Other_Skin_lesions_Yes_Birth_marks_Other']=None
    
def check_skin_Acne(request):
    skin_Acne = request.data.get('skin_Acne')
    skin_Acne_Yes = request.data.get('skin_Acne_Yes')

    if skin_Acne == 'Yes':
        if  skin_Acne_Yes == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['skin_Acne_Yes']= None

def check_Nails_Shape(request):
    Nails_Shape = request.data.get('Nails_Shape')
    Nails_Shape_Abnormal = request.data.get('Nails_Shape_Abnormal')

    if Nails_Shape == 'Abnormal':
        if Nails_Shape_Abnormal == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Nails_Shape_Abnormal'] = None

def check_Nails_Deformity(request):
    Nails_Deformity = request.data.get('Nails_Deformity')
    Nails_Deformity_Yes = request.data.get('Nails_Deformity_Yes')

    if Nails_Deformity == 'Yes':
        if Nails_Deformity_Yes == None :
            raise Exception('you have select anyone')
        
    else:
        request.data['Nails_Deformity_Yes'] = None

def check_Head_Skull_Fontanelle(request):
    Head_Skull_Fontanelle =request.data.get('Head_Skull_Fontanelle')
    Head_Skull_Fontanelle_Open = request.data.get('Head_Skull_Fontanelle_Open')
    Head_Skull_Fontanelle_Open_Fontanella = request.data.get('Head_Skull_Fontanelle_Open_Fontanella')
    Head_Skull_Fontanelle_Open_Occipital = request.data.get('Head_Skull_Fontanelle_Open_Occipital')


    if Head_Skull_Fontanelle == "Open":
        if Head_Skull_Fontanelle_Open == 'None':
            raise Exception('you have select anyone')
        selected_values = request.data.get('Head_Skull_Fontanelle_Open', '').split(',')

         # Initialize variables to store the values for each option
        FrontalFontanella_value = None
        OccipitalFontanell_value = None

        for i in selected_values:
            if i == "Frontal Fontanella":
                FrontalFontanella_value = Head_Skull_Fontanelle_Open_Fontanella
            elif i == "Occipital Fontanella":
                OccipitalFontanell_value = Head_Skull_Fontanelle_Open_Occipital

         # Set the values for each option in the request data
        request.data['Head_Skull_Fontanelle_Open_Fontanella'] = FrontalFontanella_value
        request.data['Head_Skull_Fontanelle_Open_Occipital'] = OccipitalFontanell_value

    else:
        request.data['Head_Skull_Fontanelle_Open'] = None
        request.data['Head_Skull_Fontanelle_Open_Fontanella'] = None
        request.data['Head_Skull_Fontanelle_Open_Occipital'] = None


def check_Head_Hair_Appearance(request):
    Head_Hair_Appearance = request.data.get('Head_Hair_Appearance')
    Head_Hair_Appearance_Abnormal = request.data.get('Head_Hair_Appearance_Abnormal')
    Head_Hair_Appearance_Abnormal_Other = request.data.get('Head_Hair_Appearance_Abnormal_Other')


    if Head_Hair_Appearance == 'Abnormal':
        if Head_Hair_Appearance_Abnormal == None:
            raise Exception("you have to select anyone")
        selected_values = request.data.get('Head_Hair_Appearance_Abnormal', '').split(',')
        Other_value = None
        for i in selected_values:
            if i == "Other":
                Other_value = Head_Hair_Appearance_Abnormal_Other
            request.data['Head_Hair_Appearance_Abnormal_Other'] = Other_value

           
    else:
        request.data['Head_Hair_Appearance_Abnormal'] = None
        request.data['Head_Hair_Appearance_Abnormal_Other'] = None

def check_Head_Scalp(request):
    Head_Scalp = request.data.get('Head_Scalp')
    Head_Scalp_Abnormal = request.data.get('Head_Scalp_Abnormal')

    if Head_Scalp == "Abnormal":
        if Head_Scalp_Abnormal == None:
            raise Exception("you have to select anyone")
    
    else:
        request.data['Head_Scalp_Abnormal'] = None

def check_Head_Parasites(request):

    Head_Parasites = request.data.get('Head_Parasites')
    Head_Parasites_Yes = request.data.get('Head_Parasites_Yes')
    Head_Parasites_Yes_Other = request.data.get('Head_Parasites_Yes_Other')

    
    if Head_Parasites == "Yes":
        if Head_Parasites_Yes == None:
            raise Exception("you have to select anyone")
        selected_values = request.data.get('Head_Parasites_Yes', '').split(',')

         # Initialize variables to store the values for each option
        Other_value = None
        for i in selected_values:
            if i == "Other":
                Other_value = Head_Parasites_Yes_Other
        request.data['Head_Parasites_Yes_Other'] = Other_value
    else:
        request.data['Head_Parasites_Yes'] = None
        request.data['Head_Parasites_Yes_Other'] = None


def check_Head_Hair_Loss(request):
    Head_Hair_Loss= request.data.get('Head_Hair_Loss')
    Head_Hair_Loss_Yes = request.data.get('Head_Hair_Loss_Yes')
    
    if Head_Hair_Loss == 'Yes':
        if  Head_Hair_Loss_Yes == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Head_Hair_Loss_Yes']= None

#section4

            
def check_Thyroid_Lymph_Thyroid_Gland(request):
    Thyroid_Lymph_Thyroid_Gland = request.data.get('Thyroid_Lymph_Thyroid_Gland')
    Thyroid_Lymph_Thyroid_Gland_Enlarged = request.data.get('Thyroid_Lymph_Thyroid_Gland_Enlarged')

    if Thyroid_Lymph_Thyroid_Gland == 'Enlarged':
        if  Thyroid_Lymph_Thyroid_Gland_Enlarged == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Thyroid_Gland_Enlarged']= None


def check_Thyroid_Lymph_Cervical_LN(request):
    Thyroid_Lymph_Cervical_LN = request.data.get('Thyroid_Lymph_Cervical_LN')
    Thyroid_Lymph_Cervical_LN_Palpable = request.data.get('Thyroid_Lymph_Cervical_LN_Palpable')

    if Thyroid_Lymph_Cervical_LN == 'Palpable':
        if  Thyroid_Lymph_Cervical_LN_Palpable == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Cervical_LN_Palpable']= None


def check_Thyroid_Lymph_Supraclavicular_LN(request):
    Thyroid_Lymph_Supraclavicular_LN = request.data.get('Thyroid_Lymph_Supraclavicular_LN')
    Thyroid_Lymph_Supraclavicular_LN_Palpable = request.data.get('Thyroid_Lymph_Supraclavicular_LN_Palpable')

    if Thyroid_Lymph_Supraclavicular_LN == 'Palpable':
        if  Thyroid_Lymph_Supraclavicular_LN_Palpable == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Supraclavicular_LN_Palpable']= None


def check_Thyroid_Lymph_Axillary_LN(request):
    Thyroid_Lymph_Axillary_LN = request.data.get('Thyroid_Lymph_Axillary_LN')
    Thyroid_Lymph_Axillary_LN_Palpable = request.data.get('Thyroid_Lymph_Axillary_LN_Palpable')

    if Thyroid_Lymph_Axillary_LN == 'Palpable':
        if  Thyroid_Lymph_Axillary_LN_Palpable == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Axillary_LN_Palpable']= None


def check_Thyroid_Lymph_Supratrochlear_LN(request):
    Thyroid_Lymph_Supratrochlear_LN = request.data.get('Thyroid_Lymph_Supratrochlear_LN')
    Thyroid_Lymph_Supratrochlear_LN_Palpable = request.data.get('Thyroid_Lymph_Supratrochlear_LN_Palpable')

    if Thyroid_Lymph_Supratrochlear_LN == 'Palpable':
        if  Thyroid_Lymph_Supratrochlear_LN_Palpable == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Supratrochlear_LN_Palpable']= None


def check_Thyroid_Lymph_Inguinal_LN(request):
    Thyroid_Lymph_Inguinal_LN = request.data.get('Thyroid_Lymph_Inguinal_LN')
    Thyroid_Lymph_Inguinal_LN_Palpable = request.data.get('Thyroid_Lymph_Inguinal_LN_Palpable')

    if Thyroid_Lymph_Inguinal_LN == 'Palpable':
        if  Thyroid_Lymph_Inguinal_LN_Palpable == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Thyroid_Lymph_Inguinal_LN_Palpable']= None

#section5
def check_Eyes_Discharge(request):
    Eyes_Discharge = request.data.get('Eyes_Discharge')
    Eyes_Discharge_Yes = request.data.get('Eyes_Discharge_Yes')
    Eyes_Discharge_Yes_Right_Eye =request.data.get('Eyes_Discharge_Yes_Right_Eye')
    Eyes_Discharge_Yes_Left_Eye =request.data.get('Eyes_Discharge_Yes_Left_Eye')


    if Eyes_Discharge == 'Yes':
        if  Eyes_Discharge_Yes == None :
            raise Exception("you have select anyone")
        selected_values = request.data.get('Eyes_Discharge_Yes', '').split(',')

         # Initialize variables to store the values for each option
        Right_Eye_value = None
        Left_Eye_value = None
        for i in selected_values:
            if i == "Right Eye":
                Right_Eye_value = Eyes_Discharge_Yes_Right_Eye 
            elif i == "Left Eye":
                Left_Eye_value = Eyes_Discharge_Yes_Left_Eye
        request.data['Eyes_Discharge_Yes_Right_Eye'] = Right_Eye_value
        request.data['Eyes_Discharge_Yes_Left_Eye'] = Left_Eye_value
        
    else:
        request.data['Eyes_Discharge_Yes']= None
        request.data['Eyes_Discharge_Yes_Right_Eye'] = None
        request.data['Eyes_Discharge_Yes_Left_Eye'] = None

def Eyes_Eyelids(request):
    Eyes_Eyelids = request.data.get('Eyes_Eyelids')
    Eyes_Eyelids_Abnormal = request.data.get('Eyes_Eyelids_Abnormal')

    if Eyes_Eyelids == 'Abnormal':
        if  Eyes_Eyelids_Abnormal == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Eyes_Eyelids_Abnormal']= None


#section 6
#need to check
def Ears_Hearing(request):
    Ears_Hearing = request.data.get('Ears_Hearing')
    Ears_Hearing_Abnormal = request.data.get('Ears_Hearing_Abnormal')
    Ears_Hearing_Abnormal_Reduced = request.data.get('Ears_Hearing_Abnormal_Reduced')
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid = request.data.get("Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid")
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes = request.data.get("Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes")
    Ears_Hearing_Abnormal_Reduced_Other = request.data.get('Ears_Hearing_Abnormal_Reduced_Other')
    if Ears_Hearing == 'Abnormal':
        if Ears_Hearing_Abnormal is None:
            raise Exception("You have to select anyone")
        selected_values = request.data.get('Ears_Hearing_Abnormal', '').split(',')
        Reduced_value = None
        Other_value = None
        hearing_value = None
        hearing_yes=None
        for i in selected_values:
            if i == "Reduced":
                Reduced_value = Ears_Hearing_Abnormal_Reduced
                if Reduced_value == 'Wears Hearing Aid':
                    if Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid is None:
                        raise Exception("You have to select anyone")
                    elif Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid == 'Yes':
                        hearing_value = Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid
                        hearing_yes=Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes
                        if Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes is None:
                            raise Exception("You have to select Yes")
                        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid'] = hearing_value
                        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes'] = hearing_yes
                    else:
                        hearing_value = Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid
                        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes'] = None
                        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid'] = hearing_value
            else:
                request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid'] = None
                request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes'] = None
        request.data['Ears_Hearing_Abnormal_Reduced'] = Reduced_value
        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid'] = hearing_value
        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes'] = hearing_yes
        for i in selected_values:
            if i == "Other":
                print("other")
                Other_value = Ears_Hearing_Abnormal_Reduced_Other
        request.data['Ears_Hearing_Abnormal_Reduced_Other'] = Other_value
    else:
        request.data['Ears_Hearing_Abnormal'] = None
        request.data['Ears_Hearing_Abnormal_Reduced'] = None
        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid'] = None
        request.data['Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes'] = None
        request.data['Ears_Hearing_Abnormal_Reduced_Other'] = None

def check_Ears_Discharge(request):
    Ears_Discharge = request.data.get('Ears_Discharge')
    Ears_Discharge_Yes = request.data.get('Ears_Discharge_Yes')
    Ears_Discharge_Yes_Right_Ear =request.data.get('Ears_Discharge_Yes_Right_Ear')
    Ears_Discharge_Yes_Left_Ear =request.data.get('Ears_Discharge_Yes_Left_Ear')


    if Ears_Discharge == 'Yes':
        if  Ears_Discharge_Yes == None :
            raise Exception("you have select anyone")
        selected_values = request.data.get('Ears_Discharge_Yes', '').split(',')

        Right_Ear_value = None
        Left_Ear_value = None
        for i in selected_values:
            if i == "Right Ear":
                Right_Ear_value = Ears_Discharge_Yes_Right_Ear 
            elif i == "Left Ear":
                Left_Ear_value = Ears_Discharge_Yes_Left_Ear
        request.data['Ears_Discharge_Yes_Right_Ear'] = Right_Ear_value
        request.data['Ears_Discharge_Yes_Left_Ear'] = Left_Ear_value
        
    else:
        request.data['Ears_Discharge_Yes']= None
        request.data['Ears_Discharge_Yes_Right_Ear'] = None
        request.data['Ears_Discharge_Yes_Left_Ear'] = None


def check_Ear_Wax(request):
    Ear_Wax = request.data.get('Ear_Wax')
    Ear_Wax_Present = request.data.get('Ear_Wax_Present')

    if Ear_Wax == 'Present':
        if  Ear_Wax_Present == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Ear_Wax_Present']= None


def check_Ear_Eardrum(request):
    Ear_Eardrum = request.data.get('Ear_Eardrum')
    Ear_Eardrum_Abnormal = request.data.get('Ear_Eardrum_Abnormal')
    Ear_Eardrum_Abnormal_Right_Ear =request.data.get('Ear_Eardrum_Abnormal_Right_Ear')
    Ear_Eardrum_Abnormal_Left_Ear =request.data.get('Ear_Eardrum_Abnormal_Left_Ear')


    if Ear_Eardrum == 'Abnormal':
        if  Ear_Eardrum_Abnormal == None :
            raise Exception("you have select anyone")
        selected_values = request.data.get('Ear_Eardrum_Abnormal', '').split(',')

         # Initialize variables to store the values for each option
        Right_Ear_value = None
        Left_Ear_value = None
        for i in selected_values:
            if i == "Right Ear":
                Right_Ear_value = Ear_Eardrum_Abnormal_Right_Ear 
            elif i == "Left Ear":
                Left_Ear_value = Ear_Eardrum_Abnormal_Left_Ear
        request.data['Ear_Eardrum_Abnormal_Right_Ear'] = Right_Ear_value
        request.data['Ear_Eardrum_Abnormal_Left_Ear'] = Left_Ear_value
        
    else:
        request.data['Ear_Eardrum_Abnormal']= None
        request.data['Ear_Eardrum_Abnormal_Right_Ear'] = None
        request.data['Ear_Eardrum_Abnormal_Left_Ear'] = None

#section7

def check_Nose_Discharge(request):
    Nose_Discharge = request.data.get('Nose_Discharge')
    Nose_Discharge_Yes = request.data.get('Nose_Discharge_Yes')
    Nose_Discharge_Yes_Right_Nostril =request.data.get('Nose_Discharge_Yes_Right_Nostril')
    Nose_Discharge_Yes_Left_Nostril =request.data.get('Nose_Discharge_Yes_Left_Nostril')


    if Nose_Discharge == 'Yes':
        if  Nose_Discharge_Yes == None :
            raise Exception("you have select anyone")
        selected_values = request.data.get('Nose_Discharge_Yes', '').split(',')

         # Initialize variables to store the values for each option
        Right_Nostril_value = None
        Left_Nostril_value = None

        for i in selected_values:
            if i == "Right Nostril":
                Right_Nostril_value = Nose_Discharge_Yes_Right_Nostril 
            elif i == "Left Nostril":
                Left_Nostril_value = Nose_Discharge_Yes_Left_Nostril
        request.data['Nose_Discharge_Yes_Right_Nostril'] = Right_Nostril_value
        request.data['Nose_Discharge_Yes_Left_Nostril'] = Left_Nostril_value
        
    else:
        request.data['Nose_Discharge_Yes']= None
        request.data['Nose_Discharge_Yes_Right_Nostril'] = None
        request.data['Nose_Discharge_Yes_Left_Nostril'] = None

def check_Nose_Dryness(request):
    Nose_Dryness = request.data.get('Nose_Dryness')
    Nose_Dryness_Yes = request.data.get('Nose_Dryness_Yes')

    if Nose_Dryness == 'Yes':
        if  Nose_Dryness_Yes == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Nose_Dryness_Yes']= None


def check_Nose_Crusting(request):
    Nose_Crusting = request.data.get('Nose_Crusting')
    Nose_Crusting_Yes = request.data.get('Nose_Crusting_Yes')

    if Nose_Crusting == 'Yes':
        if  Nose_Crusting_Yes == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Nose_Crusting_Yes']= None


def check_Nose_Polyps(request):
    Nose_Polyps = request.data.get('Nose_Polyps')
    Nose_Polyps_Yes = request.data.get('Nose_Polyps_Yes')

    if Nose_Polyps == 'Yes':
        if  Nose_Polyps_Yes == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Nose_Polyps_Yes']= None

#SECTION8

def check_Mouth_Throat_Mucosa(request):
    Mouth_Throat_Mucosa = request.data.get('Mouth_Throat_Mucosa')
    Mouth_Throat_Mucosa_Abnormal = request.data.get('Mouth_Throat_Mucosa_Abnormal')
    Mouth_Throat_Mucosa_Abnormal_Other =request.data.get('Mouth_Throat_Mucosa_Abnormal_Other')

    if Mouth_Throat_Mucosa == 'Abnormal':
        if  Mouth_Throat_Mucosa_Abnormal == None :
            raise Exception("you have select anyone")
        
        selected_values = request.data.get('Mouth_Throat_Mucosa_Abnormal', '').split(',')
        Other_value = None
        for i in selected_values:
          if i == "Other":
                
                Other_value = Mouth_Throat_Mucosa_Abnormal_Other
        request.data['Mouth_Throat_Mucosa_Abnormal_Other'] = Other_value

    else:
        request.data['Mouth_Throat_Mucosa_Abnormal']= None
        request.data['Mouth_Throat_Mucosa_Abnormal_Other']= None

def check_Mouth_Throat_Tongue(request):
    Mouth_Throat_Tongue = request.data.get('Mouth_Throat_Tongue')
    Mouth_Throat_Tongue_Abnormal = request.data.get('Mouth_Throat_Tongue_Abnormal')
    Mouth_Throat_Tongue_Abnormal_Other =request.data.get('Mouth_Throat_Tongue_Abnormal_Other')

    if Mouth_Throat_Tongue == 'Abnormal':
        if  Mouth_Throat_Tongue_Abnormal == None :
            raise Exception("you have select anyone")
        
        selected_values = request.data.get('Mouth_Throat_Tongue_Abnormal', '').split(',')
        Other_value = None
        for i in selected_values:
          if i == "Other":
                
                Other_value = Mouth_Throat_Tongue_Abnormal_Other
        request.data['Mouth_Throat_Tongue_Abnormal_Other'] = Other_value

    else:
        request.data['Mouth_Throat_Tongue_Abnormal']= None
        request.data['Mouth_Throat_Tongue_Abnormal_Other']= None
   

def check_Mouth_Tonsils(request):
    Mouth_Tonsils = request.data.get('Mouth_Tonsils')
    Mouth_Tonsils_Abnormal = request.data.get('Mouth_Tonsils_Abnormal')

    if Mouth_Tonsils == 'Abnormal':
        if  Mouth_Tonsils_Abnormal == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Mouth_Tonsils_Abnormal']= None

def check_Mouth_Uvula(request):
    Mouth_Uvula = request.data.get('Mouth_Uvula')
    Mouth_Uvula_Abnormal = request.data.get('Mouth_Uvula_Abnormal')

    if Mouth_Uvula == 'Abnormal':
        if  Mouth_Uvula_Abnormal == None :
            raise Exception("you have select anyone")
        
    else:
        request.data['Mouth_Uvula_Abnormal']= None


def check_Mouth_Palate(request):
    Mouth_Palate = request.data.get('Mouth_Palate')
    Mouth_Palate_Cleft_Palate = request.data.get('Mouth_Palate_Cleft_Palate')
    Mouth_Palate_CleftLip_Palate = request.data.get('Mouth_Palate_CleftLip_Palate')
    Mouth_Palate_Other = request.data.get('Mouth_Palate_Other')

    if Mouth_Palate == 'Cleft Palate':
        if  Mouth_Palate_Cleft_Palate == None :
            raise Exception("you have select anyone")
        request.data['Mouth_Palate_CleftLip_Palate'] = None
        request.data['Mouth_Palate_Other'] = None


    elif Mouth_Palate == 'Cleft Lip & Palate':
        if  Mouth_Palate_CleftLip_Palate == None :
            raise Exception("you have select anyone")
        request.data['Mouth_Palate_Cleft_Palate']= None
        request.data['Mouth_Palate_Other']= None
        
        
    elif Mouth_Palate == 'Other':
        if  Mouth_Palate_Other == None :
            raise Exception("you have select anyone")
        request.data['Mouth_Palate_Cleft_Palate']= None
        request.data['Mouth_Palate_CleftLip_Palate']= None

        
    else:
        request.data['Mouth_Palate_Cleft_Palate']= None
        request.data['Mouth_Palate_CleftLip_Palate']= None
        request.data['Mouth_Palate_Other']= None




