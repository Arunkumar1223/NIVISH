#Sction 1 Validations
def check_CNS_Speech(request):
    CNS_Speech = request.data.get('CNS_Speech')
    CNS_Speech_Abnormal = request.data.get('CNS_Speech_Abnormal')
    CNS_Speech_Abnormal_Other = request.data.get('CNS_Speech_Abnormal_Other')

    if CNS_Speech == 'Abnormal':
        if CNS_Speech_Abnormal == None:
            raise Exception("You have to select Anyone")
        elif CNS_Speech_Abnormal == 'Other':
           if CNS_Speech_Abnormal_Other == None:
            raise Exception("You have to select Anyone")
        else:
            request.data['CNS_Speech_Abnormal_Other'] = None
                
    else:
        request.data['CNS_Speech_Abnormal'] = None
        request.data['CNS_Speech_Abnormal_Other'] = None

def check_CNS_History_of_Headache(request):
    CNS_History_of_Headache = request.data.get('CNS_History_of_Headache')
    CNS_History_of_Headache_yes_Frequency = request.data.get('CNS_History_of_Headache_yes_Frequency')
    CNS_History_of_Headache_yes_Frequency_Continuous = request.data.get('CNS_History_of_Headache_yes_Frequency_Continuous')
    CNS_History_of_Headache_yes_Associated_With = request.data.get('CNS_History_of_Headache_yes_Associated_With')
    CNS_History_of_Headache_yes_Associated_With_Occurrence = request.data.get('CNS_History_of_Headache_yes_Associated_With_Occurrence')
    CNS_History_of_Headache_yes_Associated_With_Other = request.data.get('CNS_History_of_Headache_yes_Associated_With_Other')
    CNS_History_of_Headache_yes_From = request.data.get('CNS_History_of_Headache_yes_From')
    CNS_History_of_Headache_yes_Duration = request.data.get('CNS_History_of_Headache_yes_Duration')

    if CNS_History_of_Headache == 'Yes':
        if CNS_History_of_Headache_yes_Frequency == None and CNS_History_of_Headache_yes_Associated_With == None and CNS_History_of_Headache_yes_From == None and CNS_History_of_Headache_yes_Duration == None:
            raise Exception("You have to select Anyone")
        
        elif CNS_History_of_Headache_yes_Frequency == 'Continuous':
           if CNS_History_of_Headache_yes_Frequency_Continuous == None:
            raise Exception("You have to select Anyone")
        else:
            request.data['CNS_History_of_Headache_yes_Frequency_Continuous'] = None

        selected_values = request.data.get('CNS_History_of_Headache_yes_Associated_With', '').split(',')
        # Initialize variables to store the values for each option
        Occurrence = None
        Other_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Occurrence":
                Occurrence = CNS_History_of_Headache_yes_Associated_With_Occurrence
            elif i == "Other":
                Other_value = CNS_History_of_Headache_yes_Associated_With_Other

        # Set the values for each option in the request data
        request.data['CNS_History_of_Headache_yes_Associated_With_Occurrence'] = Occurrence
        request.data['CNS_History_of_Headache_yes_Associated_With_Other'] = Other_value
                
    else:
        request.data['CNS_History_of_Headache_yes_Frequency'] = None
        request.data['CNS_History_of_Headache_yes_Frequency_Continuous'] = None
        request.data['CNS_History_of_Headache_yes_Associated_With'] = None
        request.data['CNS_History_of_Headache_yes_Associated_With_Occurrence'] = None
        request.data['CNS_History_of_Headache_yes_Associated_With_Other'] = None
        request.data['CNS_History_of_Headache_yes_From'] = None
        request.data['CNS_History_of_Headache_yes_Duration'] = None

def check_CNS_History_of_Dizziness(request):
    CNS_History_of_Dizziness = request.data.get('CNS_History_of_Dizziness')
    CNS_History_of_Dizziness_yes_Frequency = request.data.get('CNS_History_of_Dizziness_yes_Frequency')
    CNS_History_of_Dizziness_yes_Frequency_Continuous = request.data.get('CNS_History_of_Dizziness_yes_Frequency_Continuous')
    CNS_History_of_Dizziness_yes_Associated_With = request.data.get('CNS_History_of_Headache_yes_Associated_With')
    CNS_History_of_Dizziness_yes_Associated_With_Occurrence = request.data.get('CNS_History_of_Dizziness_yes_Associated_With_Occurrence')
    CNS_History_of_Dizziness_yes_Associated_With_Other = request.data.get('CNS_History_of_Dizziness_yes_Associated_With_Other')

    if CNS_History_of_Dizziness == 'Yes':
        if CNS_History_of_Dizziness_yes_Frequency == None and CNS_History_of_Dizziness_yes_Associated_With == None:
            raise Exception("You have to select Anyone")
        
        elif CNS_History_of_Dizziness_yes_Frequency == 'Continuous':
           if CNS_History_of_Dizziness_yes_Frequency_Continuous == None:
            raise Exception("You have to select Anyone")
        else:
            request.data['CNS_History_of_Dizziness_yes_Frequency_Continuous'] = None

        selected_values = request.data.get('CNS_History_of_Dizziness_yes_Associated_With', '').split(',')
        # Initialize variables to store the values for each option
        Occurrence = None
        Other_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Occurrence":
                Occurrence = CNS_History_of_Dizziness_yes_Associated_With_Occurrence
            elif i == "Other":
                Other_value = CNS_History_of_Dizziness_yes_Associated_With_Other

        # Set the values for each option in the request data
        request.data['CNS_History_of_Dizziness_yes_Associated_With_Occurrence'] = Occurrence
        request.data['CNS_History_of_Dizziness_yes_Associated_With_Other'] = Other_value
                
    else:
        request.data['CNS_History_of_Dizziness_yes_Frequency'] = None
        request.data['CNS_History_of_Dizziness_yes_Frequency_Continuous'] = None
        request.data['CNS_History_of_Dizziness_yes_Associated_With'] = None
        request.data['CNS_History_of_Dizziness_yes_Associated_With_Occurrence'] = None
        request.data['CNS_History_of_Dizziness_yes_Associated_With_Other'] = None

#Sction 2 Validations
def check_RS_Shape_of_Chest(request):
    RS_Shape_of_Chest = request.data.get('RS_Shape_of_Chest')
    RS_Shape_of_Chest_Abnormal = request.data.get('RS_Shape_of_Chest_Abnormal')
    RS_Shape_of_Chest_Abnormal_Other = request.data.get('RS_Shape_of_Chest_Abnormal_Other')

    if RS_Shape_of_Chest == 'Abnormal':
        if RS_Shape_of_Chest_Abnormal == None:
            raise Exception("You have to select Anyone")
        elif RS_Shape_of_Chest_Abnormal == 'Other':
           if RS_Shape_of_Chest_Abnormal_Other == None:
            raise Exception("You have to select Anyone")
        else:
            request.data['RS_Shape_of_Chest_Abnormal_Other'] = None
                
    else:
        request.data['RS_Shape_of_Chest_Abnormal'] = None
        request.data['RS_Shape_of_Chest_Abnormal_Other'] = None

def check_RS_Type_of_Respiration_Label(request):
    RS_Type_of_Respiration_Label = request.data.get('RS_Type_of_Respiration_Label')
    RS_Type_of_Respiration_Label_Other = request.data.get('RS_Type_of_Respiration_Label_Other')

    if RS_Type_of_Respiration_Label == 'Other':
        if RS_Type_of_Respiration_Label_Other == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['RS_Type_of_Respiration_Label_Other'] = None

#Sction 3 Validations
def check_RL_Breath_Sounds(request):
    RL_Breath_Sounds = request.data.get('RL_Breath_Sounds')
    RL_Breath_Sounds_Abnormal = request.data.get('RL_Breath_Sounds_Abnormal')
    RL_Breath_Sounds_Abnormal_Apical = request.data.get('RL_Breath_Sounds_Abnormal_Apical')
    RL_Breath_Sounds_Abnormal_Mid_Zone = request.data.get('RL_Breath_Sounds_Abnormal_Mid_Zone')
    RL_Breath_Sounds_Abnormal_Basal = request.data.get('RL_Breath_Sounds_Abnormal_Basal')
    RL_Breath_Sounds_Abnormal_Sub_Scapular = request.data.get('RL_Breath_Sounds_Abnormal_Sub_Scapular')
    RL_Breath_Sounds_Abnormal_Diffuse = request.data.get('RL_Breath_Sounds_Abnormal_Diffuse')

    if RL_Breath_Sounds == 'Abnormal':
        if RL_Breath_Sounds_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('RL_Breath_Sounds_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Apical_value = None
        Mid_Zone_value = None
        Basal_value = None
        Sub_Scapular_value = None
        Diffuse_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Apical":
                Apical_value = RL_Breath_Sounds_Abnormal_Apical
            elif i == "Mid Zone":
                Mid_Zone_value = RL_Breath_Sounds_Abnormal_Mid_Zone
            elif i == "Basal":
                Basal_value = RL_Breath_Sounds_Abnormal_Basal
            elif i == "Sub Scapular":
                Sub_Scapular_value = RL_Breath_Sounds_Abnormal_Sub_Scapular
            elif i == "Diffuse":
                Diffuse_value = RL_Breath_Sounds_Abnormal_Diffuse

        # Set the values for each option in the request data
        request.data['RL_Breath_Sounds_Abnormal_Apical'] = Apical_value
        request.data['RL_Breath_Sounds_Abnormal_Mid_Zone'] = Mid_Zone_value
        request.data['RL_Breath_Sounds_Abnormal_Basal'] = Basal_value
        request.data['RL_Breath_Sounds_Abnormal_Sub_Scapular'] = Sub_Scapular_value
        request.data['RL_Breath_Sounds_Abnormal_Diffuse'] = Diffuse_value

    else:
        request.data['RL_Breath_Sounds_Abnormal'] = None
        request.data['RL_Breath_Sounds_Abnormal_Apical'] = None
        request.data['RL_Breath_Sounds_Abnormal_Mid_Zone'] = None
        request.data['RL_Breath_Sounds_Abnormal_Basal'] = None
        request.data['RL_Breath_Sounds_Abnormal_Sub_Scapular'] = None
        request.data['RL_Breath_Sounds_Abnormal_Diffuse'] = None


# more validations should be done for this function
def check_RL_Rales_Crepts(request):
    course_list=[]
    RL_Rales_Crepts = request.data.get('RL_Rales_Crepts')
    RL_Rales_Crepts_Present = request.data.get('RL_Rales_Crepts_Present')
    RL_Rales_Crepts_Present_Apical = request.data.get('RL_Rales_Crepts_Present_Apical')
    RL_Rales_Crepts_Present_Mid_Zone = request.data.get('RL_Rales_Crepts_Present_Mid_Zone')
    RL_Rales_Crepts_Present_Basal = request.data.get('RL_Rales_Crepts_Present_Basal')
    RL_Rales_Crepts_Present_Sub_Scapular = request.data.get('RL_Rales_Crepts_Present_Sub_Scapular')
    RL_Rales_Crepts_Present_Diffuse = request.data.get('RL_Rales_Crepts_Present_Diffuse')
    RL_Rales_Crepts_Present_Apical_Fine = request.data.get('RL_Rales_Crepts_Present_Apical_Fine')
    RL_Rales_Crepts_Present_Apical_Coarse=request.data.get('RL_Rales_Crepts_Present_Apical_Coarse')
    RL_Rales_Crepts_Present_Mid_Zone_Fine=request.data.get('RL_Rales_Crepts_Present_Mid_Zone_Fine')
    RL_Rales_Crepts_Present_Mid_Zone_Coarse=request.data.get('RL_Rales_Crepts_Present_Mid_Zone_Coarse')
    RL_Rales_Crepts_Present_Basal_Fine=request.data.get('RL_Rales_Crepts_Present_Basal_Fine')
    RL_Rales_Crepts_Present_Basal_Coarse=request.data.get('RL_Rales_Crepts_Present_Basal_Coarse')
    RL_Rales_Crepts_Present_Sub_Scapular_Fine=request.data.get('RL_Rales_Crepts_Present_Sub_Scapular_Fine')
    RL_Rales_Crepts_Present_Sub_Scapular_Coarse=request.data.get('RL_Rales_Crepts_Present_Sub_Scapular_Coarse')
    RL_Rales_Crepts_Present_Diffuse_Fine=request.data.get('RL_Rales_Crepts_Present_Diffuse_Fine')
    RL_Rales_Crepts_Present_Diffuse_Coarse=request.data.get('RL_Rales_Crepts_Present_Diffuse_Coarse')
   


    if RL_Rales_Crepts == 'Present':
        if RL_Rales_Crepts_Present == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('RL_Rales_Crepts_Present', '').split(',')
        # Initialize variables to store the values for each option
        Apical_value = None
        Mid_Zone_value = None
        Basal_value = None
        Sub_Scapular_value = None
        Diffuse_value = None
        Apical_Fine_value = None
        Apical_Coarse_value = None
        Mid_Zone_Fine_value = None
        Mid_Zone_Coarse_value = None
        Basal_Fine_value = None
        Basal_Coarse_value = None
        Sub_Scapular_Fine_value = None
        Sub_Scapular_Coarse_value = None
        Diffuse_Fine_value = None
        Diffuse_Coarse_value = None


        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Apical":
                Apical_value = RL_Rales_Crepts_Present_Apical
                if RL_Rales_Crepts_Present_Apical is None:
                    raise Exception("You have to select Anyone")
                elif RL_Rales_Crepts_Present_Apical == "Fine":
                    Apical_Fine_value = RL_Rales_Crepts_Present_Apical_Fine
                    request.data['RL_Rales_Crepts_Present_Apical_Coarse'] = Apical_Coarse_value
                elif RL_Rales_Crepts_Present_Apical == "Coarse":
                    Apical_Coarse_value = RL_Rales_Crepts_Present_Apical_Coarse
                    request.data['RL_Rales_Crepts_Present_Apical_Fine'] = Apical_Fine_value
                        
        request.data['RL_Rales_Crepts_Present_Apical'] = Apical_value    
        request.data['RL_Rales_Crepts_Present_Apical_Fine'] = Apical_Fine_value
        request.data['RL_Rales_Crepts_Present_Apical_Coarse'] = Apical_Coarse_value

        for i in selected_values:
            if i == "Mid Zone":
                Mid_Zone_value = RL_Rales_Crepts_Present_Mid_Zone
                if RL_Rales_Crepts_Present_Mid_Zone is None:
                    raise Exception("You have to select Anyone")
                elif RL_Rales_Crepts_Present_Mid_Zone == "Fine":
                    Mid_Zone_Fine_value = RL_Rales_Crepts_Present_Mid_Zone_Fine
                    request.data['RL_Rales_Crepts_Present_Mid_Zone_Coarse'] = Mid_Zone_Coarse_value
                elif RL_Rales_Crepts_Present_Mid_Zone == "Coarse":
                    Mid_Zone_Coarse_value = RL_Rales_Crepts_Present_Mid_Zone_Coarse
                    request.data['RL_Rales_Crepts_Present_Mid_Zone_Fine'] = Mid_Zone_Fine_value
                        
        request.data['RL_Rales_Crepts_Present_Mid_Zone'] = Mid_Zone_value    
        request.data['RL_Rales_Crepts_Present_Mid_Zone_Fine'] = Mid_Zone_Fine_value
        request.data['RL_Rales_Crepts_Present_Mid_Zone_Coarse'] = Mid_Zone_Coarse_value

        for i in selected_values:
            if i == "Basal":
                Basal_value = RL_Rales_Crepts_Present_Basal
                if RL_Rales_Crepts_Present_Basal is None:
                    raise Exception("You have to select Anyone")
                elif RL_Rales_Crepts_Present_Basal == "Fine":
                    Basal_Fine_value = RL_Rales_Crepts_Present_Basal_Fine
                    request.data['RL_Rales_Crepts_Present_Basal_Coarse'] = Basal_Coarse_value
                elif RL_Rales_Crepts_Present_Basal == "Coarse":
                    Basal_Coarse_value = RL_Rales_Crepts_Present_Basal_Coarse
                    request.data['RL_Rales_Crepts_Present_Basal_Fine'] = Basal_Fine_value
                        
        request.data['RL_Rales_Crepts_Present_Basal'] = Basal_value    
        request.data['RL_Rales_Crepts_Present_Basal_Fine'] = Basal_Fine_value
        request.data['RL_Rales_Crepts_Present_Basal_Coarse'] = Basal_Coarse_value

        for i in selected_values:
            if i == "Sub Scapular":
                Sub_Scapular_value = RL_Rales_Crepts_Present_Sub_Scapular
                if RL_Rales_Crepts_Present_Sub_Scapular is None:
                    raise Exception("You have to select Anyone")
                elif RL_Rales_Crepts_Present_Sub_Scapular == "Fine":
                    Sub_Scapular_Fine_value = RL_Rales_Crepts_Present_Sub_Scapular_Fine
                    request.data['RL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = Sub_Scapular_Coarse_value
                elif RL_Rales_Crepts_Present_Sub_Scapular == "Coarse":
                    Sub_Scapular_Coarse_value = RL_Rales_Crepts_Present_Sub_Scapular_Coarse
                    request.data['RL_Rales_Crepts_Present_Sub_Scapular_Fine'] = Sub_Scapular_Fine_value
                        
        request.data['RL_Rales_Crepts_Present_Sub_Scapular'] = Sub_Scapular_value    
        request.data['RL_Rales_Crepts_Present_Sub_Scapular_Fine'] = Sub_Scapular_Fine_value
        request.data['RL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = Sub_Scapular_Coarse_value

        for i in selected_values:
            if i == "Diffuse":
                Diffuse_value = RL_Rales_Crepts_Present_Diffuse
                if RL_Rales_Crepts_Present_Diffuse is None:
                    raise Exception("You have to select Anyone")
                elif RL_Rales_Crepts_Present_Diffuse == "Fine":
                    Diffuse_Fine_value = RL_Rales_Crepts_Present_Diffuse_Fine
                    request.data['RL_Rales_Crepts_Present_Diffuse_Coarse'] = Diffuse_Coarse_value
                elif RL_Rales_Crepts_Present_Diffuse == "Coarse":
                    Diffuse_Coarse_value = RL_Rales_Crepts_Present_Diffuse_Coarse
                    request.data['RL_Rales_Crepts_Present_Diffuse_Fine'] = Diffuse_Fine_value
                        
        request.data['RL_Rales_Crepts_Present_Diffuse'] = Diffuse_value    
        request.data['RL_Rales_Crepts_Present_Diffuse_Fine'] = Diffuse_Fine_value
        request.data['RL_Rales_Crepts_Present_Diffuse_Coarse'] = Diffuse_Coarse_value
           

    else:
        request.data['RL_Rales_Crepts_Present'] = None
        request.data['RL_Rales_Crepts_Present_Apical'] = None
        request.data['RL_Rales_Crepts_Present_Mid_Zone'] = None
        request.data['RL_Rales_Crepts_Present_Basal'] = None
        request.data['RL_Rales_Crepts_Present_Sub_Scapular'] = None
        request.data['RL_Rales_Crepts_Present_Diffuse'] = None

        request.data['RL_Rales_Crepts_Present_Apical_Fine'] = None
        request.data['RL_Rales_Crepts_Present_Apical_Coarse'] = None
        request.data['RL_Rales_Crepts_Present_Mid_Zone_Fine'] = None
        request.data['RL_Rales_Crepts_Present_Mid_Zone_Coarse'] = None
        request.data['RL_Rales_Crepts_Present_Basal_Fine'] = None
        request.data['RL_Rales_Crepts_Present_Basal_Coarse'] = None
        request.data['RL_Rales_Crepts_Present_Sub_Scapular_Fine'] = None
        request.data['RL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = None
        request.data['RL_Rales_Crepts_Present_Diffuse_Fine'] = None
        request.data['RL_Rales_Crepts_Present_Diffuse_Coarse'] = None


def check_RL_Rhonchi_Wheezing(request):
    RL_Rhonchi_Wheezing = request.data.get('RL_Rhonchi_Wheezing')
    RL_Rhonchi_Wheezing_Present = request.data.get('RL_Rhonchi_Wheezing_Present')
    
    if RL_Rhonchi_Wheezing == 'Present':
        if RL_Rhonchi_Wheezing_Present == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['RL_Rhonchi_Wheezing_Present'] = None

def check_RL_Added_Sounds(request):
    RL_Added_Sounds = request.data.get('RL_Added_Sounds')
    RL_Added_Sounds_Present = request.data.get('RL_Added_Sounds_Present')
    
    if RL_Added_Sounds == 'Present':
        if RL_Added_Sounds_Present == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['RL_Added_Sounds_Present'] = None

def check_RL_Added_Zone_of_Concern(request):
    RL_Added_Zone_of_Concern = request.data.get('RL_Added_Zone_of_Concern')
    RL_Added_Zone_of_Concern_Abnormal = request.data.get('RL_Added_Zone_of_Concern_Abnormal')
    
    if RL_Added_Zone_of_Concern == 'Present':
        if RL_Added_Zone_of_Concern_Abnormal == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['RL_Added_Zone_of_Concern_Abnormal'] = None

def check_LL_Breath_Sounds(request):
    LL_Breath_Sounds = request.data.get('LL_Breath_Sounds')
    LL_Breath_Sounds_Abnormal = request.data.get('LL_Breath_Sounds_Abnormal')
    LL_Breath_Sounds_Abnormal_Apical = request.data.get('LL_Breath_Sounds_Abnormal_Apical')
    LL_Breath_Sounds_Abnormal_Mid_Zone = request.data.get('LL_Breath_Sounds_Abnormal_Mid_Zone')
    LL_Breath_Sounds_Abnormal_Basal = request.data.get('LL_Breath_Sounds_Abnormal_Basal')
    LL_Breath_Sounds_Abnormal_Sub_Scapular = request.data.get('LL_Breath_Sounds_Abnormal_Sub_Scapular')
    LL_Breath_Sounds_Abnormal_Diffuse = request.data.get('LL_Breath_Sounds_Abnormal_Diffuse')

    if LL_Breath_Sounds == 'Abnormal':
        if LL_Breath_Sounds_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('LL_Breath_Sounds_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Apical_value = None
        Mid_Zone_value = None
        Basal_value = None
        Sub_Scapular_value = None
        Diffuse_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Apical":
                Apical_value = LL_Breath_Sounds_Abnormal_Apical
            elif i == "Mid Zone":
                Mid_Zone_value = LL_Breath_Sounds_Abnormal_Mid_Zone
            elif i == "Basal":
                Basal_value = LL_Breath_Sounds_Abnormal_Basal
            elif i == "Sub Scapular":
                Sub_Scapular_value = LL_Breath_Sounds_Abnormal_Sub_Scapular
            elif i == "Diffuse":
                Diffuse_value = LL_Breath_Sounds_Abnormal_Diffuse

        # Set the values for each option in the request data
        request.data['LL_Breath_Sounds_Abnormal_Apical'] = Apical_value
        request.data['LL_Breath_Sounds_Abnormal_Mid_Zone'] = Mid_Zone_value
        request.data['LL_Breath_Sounds_Abnormal_Basal'] = Basal_value
        request.data['LL_Breath_Sounds_Abnormal_Sub_Scapular'] = Sub_Scapular_value
        request.data['LL_Breath_Sounds_Abnormal_Diffuse'] = Diffuse_value

    else:
        request.data['LL_Breath_Sounds_Abnormal'] = None
        request.data['LL_Breath_Sounds_Abnormal_Apical'] = None
        request.data['LL_Breath_Sounds_Abnormal_Mid_Zone'] = None
        request.data['LL_Breath_Sounds_Abnormal_Basal'] = None
        request.data['LL_Breath_Sounds_Abnormal_Sub_Scapular'] = None
        request.data['LL_Breath_Sounds_Abnormal_Diffuse'] = None


# more validations should be done for this function
def check_LL_Rales_Crepts(request):
    LL_Rales_Crepts = request.data.get('LL_Rales_Crepts')
    LL_Rales_Crepts_Present = request.data.get('LL_Rales_Crepts_Present')
    LL_Rales_Crepts_Present_Apical = request.data.get('LL_Rales_Crepts_Present_Apical')
    LL_Rales_Crepts_Present_Mid_Zone = request.data.get('LL_Rales_Crepts_Present_Mid_Zone')
    LL_Rales_Crepts_Present_Basal = request.data.get('LL_Rales_Crepts_Present_Basal')
    LL_Rales_Crepts_Present_Sub_Scapular = request.data.get('LL_Rales_Crepts_Present_Sub_Scapular')
    LL_Rales_Crepts_Present_Diffuse = request.data.get('LL_Rales_Crepts_Present_Diffuse')
    LL_Rales_Crepts_Present_Apical_Fine = request.data.get('LL_Rales_Crepts_Present_Apical_Fine')
    LL_Rales_Crepts_Present_Apical_Coarse = request.data.get('LL_Rales_Crepts_Present_Apical_Coarse')
    LL_Rales_Crepts_Present_Mid_Zone_Fine = request.data.get('LL_Rales_Crepts_Present_Mid_Zone_Fine')
    LL_Rales_Crepts_Present_Mid_Zone_Coarse = request.data.get('LL_Rales_Crepts_Present_Mid_Zone_Coarse')
    LL_Rales_Crepts_Present_Basal_Fine = request.data.get('LL_Rales_Crepts_Present_Basal_Fine')
    LL_Rales_Crepts_Present_Basal_Coarse = request.data.get('LL_Rales_Crepts_Present_Basal_Coarse')
    LL_Rales_Crepts_Present_Sub_Scapular_Fine = request.data.get('LL_Rales_Crepts_Present_Sub_Scapular_Fine')
    LL_Rales_Crepts_Present_Sub_Scapular_Coarse = request.data.get('LL_Rales_Crepts_Present_Sub_Scapular_Coarse')
    LL_Rales_Crepts_Present_Diffuse_Fine = request.data.get('LL_Rales_Crepts_Present_Diffuse_Fine')
    LL_Rales_Crepts_Present_Diffuse_Coarse = request.data.get('LL_Rales_Crepts_Present_Diffuse_Coarse')

    if LL_Rales_Crepts == 'Present':
        if LL_Rales_Crepts_Present == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('LL_Rales_Crepts_Present', '').split(',')
        # Initialize variables to store the values for each option
        Apical_value = None
        Mid_Zone_value = None
        Basal_value = None
        Sub_Scapular_value = None
        Diffuse_value = None
        Apical_Fine_value = None
        Apical_Coarse_value = None
        Mid_Zone_Fine_value = None
        Mid_Zone_Coarse_value = None
        Basal_Fine_value = None
        Basal_Coarse_value = None
        Sub_Scapular_Fine_value = None
        Sub_Scapular_Coarse_value = None
        Diffuse_Fine_value = None
        Diffuse_Coarse_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Apical":
                Apical_value = LL_Rales_Crepts_Present_Apical
                if LL_Rales_Crepts_Present_Apical is None:
                    raise Exception("You have to select Anyone")
                elif LL_Rales_Crepts_Present_Apical == "Fine":
                    Apical_Fine_value = LL_Rales_Crepts_Present_Apical_Fine
                    request.data['LL_Rales_Crepts_Present_Apical_Coarse'] = Apical_Coarse_value
                elif LL_Rales_Crepts_Present_Apical == "Coarse":
                    Apical_Coarse_value = LL_Rales_Crepts_Present_Apical_Coarse
                    request.data['LL_Rales_Crepts_Present_Apical_Fine'] = Apical_Fine_value
                        
        request.data['LL_Rales_Crepts_Present_Apical'] = Apical_value    
        request.data['LL_Rales_Crepts_Present_Apical_Fine'] = Apical_Fine_value
        request.data['LL_Rales_Crepts_Present_Apical_Coarse'] = Apical_Coarse_value

        for i in selected_values:
            if i == "Mid Zone":
                Mid_Zone_value = LL_Rales_Crepts_Present_Mid_Zone
                if LL_Rales_Crepts_Present_Mid_Zone is None:
                    raise Exception("You have to select Anyone")
                elif LL_Rales_Crepts_Present_Mid_Zone == "Fine":
                    Mid_Zone_Fine_value = LL_Rales_Crepts_Present_Mid_Zone_Fine
                    request.data['LL_Rales_Crepts_Present_Mid_Zone_Coarse'] = Mid_Zone_Coarse_value
                elif LL_Rales_Crepts_Present_Mid_Zone == "Coarse":
                    Mid_Zone_Coarse_value = LL_Rales_Crepts_Present_Mid_Zone_Coarse
                    request.data['LL_Rales_Crepts_Present_Mid_Zone_Fine'] = Mid_Zone_Fine_value
                        
        request.data['LL_Rales_Crepts_Present_Mid_Zone'] = Mid_Zone_value    
        request.data['LL_Rales_Crepts_Present_Mid_Zone_Fine'] = Mid_Zone_Fine_value
        request.data['LL_Rales_Crepts_Present_Mid_Zone_Coarse'] = Mid_Zone_Coarse_value

        for i in selected_values:
            if i == "Basal":
                Basal_value = LL_Rales_Crepts_Present_Basal
                if LL_Rales_Crepts_Present_Basal is None:
                    raise Exception("You have to select Anyone")
                elif LL_Rales_Crepts_Present_Basal == "Fine":
                    Basal_Fine_value = LL_Rales_Crepts_Present_Basal_Fine
                    request.data['LL_Rales_Crepts_Present_Basal_Coarse'] = Basal_Coarse_value
                elif LL_Rales_Crepts_Present_Basal == "Coarse":
                    Basal_Coarse_value = LL_Rales_Crepts_Present_Basal_Coarse
                    request.data['LL_Rales_Crepts_Present_Basal_Fine'] = Basal_Fine_value
                        
        request.data['LL_Rales_Crepts_Present_Basal'] = Basal_value    
        request.data['LL_Rales_Crepts_Present_Basal_Fine'] = Basal_Fine_value
        request.data['LL_Rales_Crepts_Present_Basal_Coarse'] = Basal_Coarse_value

        for i in selected_values:
            if i == "Sub Scapular":
                Sub_Scapular_value = LL_Rales_Crepts_Present_Sub_Scapular
                if LL_Rales_Crepts_Present_Sub_Scapular is None:
                    raise Exception("You have to select Anyone")
                elif LL_Rales_Crepts_Present_Sub_Scapular == "Fine":
                    Sub_Scapular_Fine_value = LL_Rales_Crepts_Present_Sub_Scapular_Fine
                    request.data['LL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = Sub_Scapular_Coarse_value
                elif LL_Rales_Crepts_Present_Sub_Scapular == "Coarse":
                    Sub_Scapular_Coarse_value = LL_Rales_Crepts_Present_Sub_Scapular_Coarse
                    request.data['LL_Rales_Crepts_Present_Sub_Scapular_Fine'] = Sub_Scapular_Fine_value
                        
        request.data['LL_Rales_Crepts_Present_Sub_Scapular'] = Sub_Scapular_value    
        request.data['LL_Rales_Crepts_Present_Sub_Scapular_Fine'] = Sub_Scapular_Fine_value
        request.data['LL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = Sub_Scapular_Coarse_value

        for i in selected_values:
            if i == "Diffuse":
                Diffuse_value = LL_Rales_Crepts_Present_Diffuse
                if LL_Rales_Crepts_Present_Diffuse is None:
                    raise Exception("You have to select Anyone")
                elif LL_Rales_Crepts_Present_Diffuse == "Fine":
                    Diffuse_Fine_value = LL_Rales_Crepts_Present_Diffuse_Fine
                    request.data['LL_Rales_Crepts_Present_Diffuse_Coarse'] = Diffuse_Coarse_value
                elif LL_Rales_Crepts_Present_Diffuse == "Coarse":
                    Diffuse_Coarse_value = LL_Rales_Crepts_Present_Diffuse_Coarse
                    request.data['LL_Rales_Crepts_Present_Diffuse_Fine'] = Diffuse_Fine_value
                        
        request.data['LL_Rales_Crepts_Present_Diffuse'] = Diffuse_value    
        request.data['LL_Rales_Crepts_Present_Diffuse_Fine'] = Diffuse_Fine_value
        request.data['LL_Rales_Crepts_Present_Diffuse_Coarse'] = Diffuse_Coarse_value



    else:
        request.data['LL_Rales_Crepts_Present'] = None
        request.data['LL_Rales_Crepts_Present_Apical'] = None
        request.data['LL_Rales_Crepts_Present_Mid_Zone'] = None
        request.data['LL_Rales_Crepts_Present_Basal'] = None
        request.data['LL_Rales_Crepts_Present_Sub_Scapular'] = None
        request.data['LL_Rales_Crepts_Present_Diffuse'] = None

        request.data['LL_Rales_Crepts_Present_Apical_Fine'] = None
        request.data['LL_Rales_Crepts_Present_Apical_Coarse'] = None
        request.data['LL_Rales_Crepts_Present_Mid_Zone_Fine'] = None
        request.data['LL_Rales_Crepts_Present_Mid_Zone_Coarse'] = None
        request.data['LL_Rales_Crepts_Present_Basal_Fine'] = None
        request.data['LL_Rales_Crepts_Present_Basal_Coarse'] = None
        request.data['LL_Rales_Crepts_Present_Sub_Scapular_Fine'] = None
        request.data['LL_Rales_Crepts_Present_Sub_Scapular_Coarse'] = None
        request.data['LL_Rales_Crepts_Present_Diffuse_Fine'] = None
        request.data['LL_Rales_Crepts_Present_Diffuse_Coarse'] = None


def check_LL_Rhonchi_Wheezing(request):
    LL_Rhonchi_Wheezing = request.data.get('LL_Rhonchi_Wheezing')
    LL_Rhonchi_Wheezing_Present = request.data.get('LL_Rhonchi_Wheezing_Present')
    
    if LL_Rhonchi_Wheezing == 'Present':
        if LL_Rhonchi_Wheezing_Present == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['LL_Rhonchi_Wheezing_Present'] = None

def check_LL_Added_Sounds(request):
    LL_Added_Sounds = request.data.get('LL_Added_Sounds')
    LL_Added_Sounds_Present = request.data.get('LL_Added_Sounds_Present')
    
    if LL_Added_Sounds == 'Present':
        if LL_Added_Sounds_Present == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['LL_Added_Sounds_Present'] = None

def check_LL_Added_Zone_of_Concern(request):
    LL_Added_Zone_of_Concern = request.data.get('LL_Added_Zone_of_Concern')
    LL_Added_Zone_of_Concern_Abnormal = request.data.get('LL_Added_Zone_of_Concern_Abnormal')
    
    if LL_Added_Zone_of_Concern == 'Abnormal':
        if LL_Added_Zone_of_Concern_Abnormal == None:
            raise Exception("You have to select Anyone")
        
    else:
        request.data['LL_Added_Zone_of_Concern_Abnormal'] = None

#Sction 4 Validations
def check_CVS_Jugular_Pulsations(request):
    CVS_Jugular_Pulsations = request.data.get('CVS_Jugular_Pulsations')
    CVS_Jugular_Pulsations_Visible = request.data.get('CVS_Jugular_Pulsations_Visible')
    CVS_Jugular_Pulsations_Visible_Abnormal = request.data.get('CVS_Jugular_Pulsations_Visible_Abnormal')

    if CVS_Jugular_Pulsations == 'Visible':
        if CVS_Jugular_Pulsations_Visible == None:
            raise Exception("You have to select Anyone")
        elif CVS_Jugular_Pulsations_Visible == 'Abnormal':
            if CVS_Jugular_Pulsations_Visible_Abnormal == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['CVS_Jugular_Pulsations_Visible_Abnormal'] = None
        

    else:
        request.data['CVS_Jugular_Pulsations_Visible'] = None
        request.data['CVS_Jugular_Pulsations_Visible_Abnormal'] = None

def check_CVS_Suprasternal_Pulsations(request):
    CVS_Suprasternal_Pulsations = request.data.get('CVS_Suprasternal_Pulsations')
    CVS_Suprasternal_Pulsations_Present = request.data.get('CVS_Suprasternal_Pulsations_Present')

    if CVS_Suprasternal_Pulsations == 'Visible':
        if CVS_Suprasternal_Pulsations_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['CVS_Suprasternal_Pulsations_Present'] = None

def check_CVS_Peripheral_Pulsations_Radial(request):
    CVS_Peripheral_Pulsations_Radial = request.data.get('CVS_Peripheral_Pulsations_Radial')
    CVS_Peripheral_Pulsations_Radial_Present = request.data.get('CVS_Peripheral_Pulsations_Radial_Present')
    CVS_Peripheral_Pulsations_Radial_Present_Abnormal = request.data.get('CVS_Peripheral_Pulsations_Radial_Present_Abnormal')

    if CVS_Peripheral_Pulsations_Radial == 'Present':
        if CVS_Peripheral_Pulsations_Radial_Present == None:
            raise Exception("You have to select Anyone")
        elif CVS_Peripheral_Pulsations_Radial_Present == 'Abnormal':
            if CVS_Peripheral_Pulsations_Radial_Present_Abnormal == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['CVS_Peripheral_Pulsations_Radial_Present_Abnormal'] = None
        

    else:
        request.data['CVS_Peripheral_Pulsations_Radial_Present'] = None
        request.data['CVS_Peripheral_Pulsations_Radial_Present_Abnormal'] = None

def check_CVS_Peripheral_Pulsations_Dorsalis_Pedis(request):
    CVS_Peripheral_Pulsations_Dorsalis_Pedis = request.data.get('CVS_Peripheral_Pulsations_Dorsalis_Pedis')
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present = request.data.get('CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present')
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal = request.data.get('CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal')

    if CVS_Peripheral_Pulsations_Dorsalis_Pedis == 'Present':
        if CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present == None:
            raise Exception("You have to select Anyone")
        elif CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present == 'Abnormal':
            if CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal'] = None
        

    else:
        request.data['CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present'] = None
        request.data['CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal'] = None
      
def check_CVS_Murmur(request):
    CVS_Murmur = request.data.get('CVS_Murmur')
    CVS_Murmur_Present = request.data.get('CVS_Murmur_Present')
    CVS_Murmur_Present_Other = request.data.get('CVS_Murmur_Present_Other')

    if CVS_Murmur == 'Present':
        if CVS_Murmur_Present == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('CVS_Murmur_Present', '').split(',')
        # Initialize variables to store the values for each option
        Other_value = None
        for i in selected_values:
            if i == "Other":
                Other_value = CVS_Murmur_Present_Other
        request.data['CVS_Murmur_Present_Other'] = Other_value

    else:
        request.data['CVS_Murmur_Present'] = None
        request.data['CVS_Murmur_Present_Other'] = None

def check_CVS_Click(request):
    CVS_Click = request.data.get('CVS_Click')
    CVS_Click_Present_Position = request.data.get('CVS_Click_Present_Position')

    if CVS_Click == 'Present':
        if CVS_Click_Present_Position == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['CVS_Click_Present_Position'] = None

def check_CVS_Apex_Beat(request):
    CVS_Apex_Beat = request.data.get('CVS_Apex_Beat')
    CVS_Apex_Beat_Present_Displaced = request.data.get('CVS_Apex_Beat_Present_Displaced')

    if CVS_Apex_Beat == 'Displaced':
        if CVS_Apex_Beat_Present_Displaced == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['CVS_Apex_Beat_Present_Displaced'] = None

#Section 5 Validations
def check_AUS_Cleft_Lip(request):
    AUS_Cleft_Lip = request.data.get('AUS_Cleft_Lip')
    AUS_Cleft_Lip_Present = request.data.get('AUS_Cleft_Lip_Present')

    if AUS_Cleft_Lip == 'Present':
        if AUS_Cleft_Lip_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_Cleft_Lip_Present'] = None

def check_AUS_Cleft_Palate(request):
    AUS_Cleft_Palate = request.data.get('AUS_Cleft_Palate')
    AUS_Cleft_Palate_Present = request.data.get('AUS_Cleft_Palate_Present')

    if AUS_Cleft_Palate == 'Present':
        if AUS_Cleft_Palate_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_Cleft_Palate_Present'] = None

def check_AUS_Right_Hypochondrium_Pain(request):
    AUS_Right_Hypochondrium_Pain = request.data.get('AUS_Right_Hypochondrium_Pain')
    AUS_RH_Pain_Yes_Pain_Score = request.data.get('AUS_RH_Pain_Yes_Pain_Score')

    if AUS_Right_Hypochondrium_Pain == 'Yes':
        if AUS_RH_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RH_Pain_Yes_Pain_Score'] = None

def check_AUS_RH_Tenderness(request):
    AUS_RH_Tenderness = request.data.get('AUS_RH_Tenderness')
    AUS_RH_Tenderness_Present = request.data.get('AUS_RH_Tenderness_Present')

    if AUS_RH_Tenderness == 'Present':
        if AUS_RH_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RH_Tenderness_Present'] = None

def check_AUS_RH_Swelling_Lumps(request):
    AUS_RH_Swelling_Lumps = request.data.get('AUS_RH_Swelling_Lumps')
    AUS_RH_Swelling_Lumps_Present_Description = request.data.get('AUS_RH_Swelling_Lumps_Present_Description')
    AUS_RH_Swelling_Lumps_Present_Size = request.data.get('AUS_RH_Swelling_Lumps_Present_Size')
    AUS_RH_Swelling_Lumps_Present_Texture = request.data.get('AUS_RH_Swelling_Lumps_Present_Texture')

    if AUS_RH_Swelling_Lumps == 'Present':
        if AUS_RH_Swelling_Lumps_Present_Description == None and AUS_RH_Swelling_Lumps_Present_Size == None and AUS_RH_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RH_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_RH_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_RH_Swelling_Lumps_Present_Texture'] = None

def check_AUS_RH_Liver(request):
    AUS_RH_Liver = request.data.get('AUS_RH_Liver')
    AUS_RH_Liver_Palpable = request.data.get('AUS_RH_Liver_Palpable')

    if AUS_RH_Liver == 'Palpable':
        if AUS_RH_Liver_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RH_Liver_Palpable'] = None

def check_AUS_RH_Gall_Bladder(request):
    AUS_RH_Gall_Bladder = request.data.get('AUS_RH_Gall_Bladder')
    AUS_RH_Gall_Bladder_Tender = request.data.get('AUS_RH_Gall_Bladder_Tender')

    if AUS_RH_Gall_Bladder == 'Tender':
        if AUS_RH_Gall_Bladder_Tender == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RH_Gall_Bladder_Tender'] = None


def check_AUS_Right_Lumbar_Pain(request):
    AUS_Right_Lumbar_Pain = request.data.get('AUS_Right_Lumbar_Pain')
    AUS_RL_Pain_Yes_Pain_Score = request.data.get('AUS_RL_Pain_Yes_Pain_Score')

    if AUS_Right_Lumbar_Pain == 'Yes':
        if AUS_RL_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RL_Pain_Yes_Pain_Score'] = None

def check_AUS_RL_Tenderness(request):
    AUS_RL_Tenderness = request.data.get('AUS_RL_Tenderness')
    AUS_RL_Tenderness_Present = request.data.get('AUS_RL_Tenderness_Present')

    if AUS_RL_Tenderness == 'Present':
        if AUS_RL_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RL_Tenderness_Present'] = None

def check_AUS_RL_Swelling_Lumps(request):
    AUS_RL_Swelling_Lumps = request.data.get('AUS_RL_Swelling_Lumps')
    AUS_RL_Swelling_Lumps_Present_Description = request.data.get('AUS_RL_Swelling_Lumps_Present_Description')
    AUS_RL_Swelling_Lumps_Present_Size = request.data.get('AUS_RL_Swelling_Lumps_Present_Size')
    AUS_RL_Swelling_Lumps_Present_Texture = request.data.get('AUS_RL_Swelling_Lumps_Present_Texture')

    if AUS_RL_Swelling_Lumps == 'Present':
        if AUS_RL_Swelling_Lumps_Present_Description == None and AUS_RL_Swelling_Lumps_Present_Size == None and AUS_RL_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RL_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_RL_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_RL_Swelling_Lumps_Present_Texture'] = None

def check_AUS_RL_Right_Kidney(request):
    AUS_RL_Right_Kidney = request.data.get('AUS_RL_Right_Kidney')
    AUS_RL_Right_Kidney_Palpable = request.data.get('AUS_RL_Right_Kidney_Palpable')

    if AUS_RL_Right_Kidney == 'Palpable':
        if AUS_RL_Right_Kidney_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RL_Right_Kidney_Palpable'] = None

def check_AUS_Right_Iliac_Pain(request):
    AUS_Right_Iliac_Pain = request.data.get('AUS_Right_Iliac_Pain')
    AUS_RI_Pain_Yes_Pain_Score = request.data.get('AUS_RI_Pain_Yes_Pain_Score')

    if AUS_Right_Iliac_Pain == 'Yes':
        if AUS_RI_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RI_Pain_Yes_Pain_Score'] = None

def check_AUS_RI_MBP(request):
    AUS_RI_MBP = request.data.get('AUS_RI_MBP')
    AUS_RI_MBP_Pain_Score = request.data.get('AUS_RI_MBP_Pain_Score')

    if AUS_RI_MBP == 'Tender':
        if AUS_RI_MBP_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RI_MBP_Pain_Score'] = None

def check_AUS_RI_Tenderness(request):
    AUS_RI_Tenderness = request.data.get('AUS_RI_Tenderness')
    AUS_RI_Tenderness_Present = request.data.get('AUS_RI_Tenderness_Present')

    if AUS_RI_Tenderness == 'Present':
        if AUS_RI_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RI_Tenderness_Present'] = None

def check_AUS_RI_Swelling_Lumps(request):
    AUS_RI_Swelling_Lumps = request.data.get('AUS_RI_Swelling_Lumps')
    AUS_RI_Swelling_Lumps_Present_Description = request.data.get('AUS_RI_Swelling_Lumps_Present_Description')
    AUS_RI_Swelling_Lumps_Present_Size = request.data.get('AUS_RI_Swelling_Lumps_Present_Size')
    AUS_RI_Swelling_Lumps_Present_Texture = request.data.get('AUS_RI_Swelling_Lumps_Present_Texture')

    if AUS_RI_Swelling_Lumps == 'Present':
        if AUS_RI_Swelling_Lumps_Present_Description == None and AUS_RI_Swelling_Lumps_Present_Size == None and AUS_RI_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_RI_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_RI_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_RI_Swelling_Lumps_Present_Texture'] = None


def check_AUS_Epigastric_Pain(request):
    AUS_Epigastric_Pain = request.data.get('AUS_Epigastric_Pain')
    AUS_E_Pain_Yes_Pain_Score = request.data.get('AUS_E_Pain_Yes_Pain_Score')

    if AUS_Epigastric_Pain == 'Yes':
        if AUS_E_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_E_Pain_Yes_Pain_Score'] = None

# need to check
def check_AUS_E_Tenderness(request):
    AUS_E_Tenderness = request.data.get('AUS_E_Tenderness')
    AUS_E_Tenderness_Present = request.data.get('AUS_E_Tenderness_Present')
    AUS_E_Tenderness_Present_Rebound = request.data.get('AUS_E_Tenderness_Present_Rebound')

    if AUS_E_Tenderness == 'Present':
        if AUS_E_Tenderness_Present == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_E_Tenderness_Present_Rebound'] = None
    
    elif AUS_E_Tenderness == 'Present Rebound':
        if AUS_E_Tenderness_Present_Rebound == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_E_Tenderness_Present'] = None

    else:
        request.data['AUS_E_Tenderness_Present'] = None
        request.data['AUS_E_Tenderness_Present_Rebound'] = None

def check_AUS_E_Swelling_Lumps(request):
    AUS_E_Swelling_Lumps = request.data.get('AUS_E_Swelling_Lumps')
    AUS_E_Swelling_Lumps_Present_Description = request.data.get('AUS_E_Swelling_Lumps_Present_Description')
    AUS_E_Swelling_Lumps_Present_Size = request.data.get('AUS_E_Swelling_Lumps_Present_Size')
    AUS_E_Swelling_Lumps_Present_Texture = request.data.get('AUS_E_Swelling_Lumps_Present_Texture')

    if AUS_E_Swelling_Lumps == 'Present':
        if AUS_E_Swelling_Lumps_Present_Description == None and AUS_E_Swelling_Lumps_Present_Size == None and AUS_E_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_E_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_E_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_E_Swelling_Lumps_Present_Texture'] = None

def check_AUS_Umbilical_Pain(request):
    AUS_Umbilical_Pain = request.data.get('AUS_Umbilical_Pain')
    AUS_U_Pain_Yes_Pain_Score = request.data.get('AUS_U_Pain_Yes_Pain_Score')

    if AUS_Umbilical_Pain == 'Yes':
        if AUS_U_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_U_Pain_Yes_Pain_Score'] = None

# need to check
def check_AUS_U_Tenderness(request):
    AUS_U_Tenderness = request.data.get('AUS_U_Tenderness')
    AUS_U_Tenderness_Present = request.data.get('AUS_U_Tenderness_Present')
    AUS_U_Tenderness_Present_Rebound = request.data.get('AUS_U_Tenderness_Present_Rebound')

    if AUS_U_Tenderness == 'Present':
        if AUS_U_Tenderness_Present == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_U_Tenderness_Present_Rebound'] = None
    
    elif AUS_U_Tenderness == 'Present Rebound':
        if AUS_U_Tenderness_Present_Rebound == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_U_Tenderness_Present'] = None

    else:
        request.data['AUS_U_Tenderness_Present'] = None
        request.data['AUS_U_Tenderness_Present_Rebound'] = None

def check_AUS_U_Swelling_Lumps(request):
    AUS_U_Swelling_Lumps = request.data.get('AUS_U_Swelling_Lumps')
    AUS_U_Swelling_Lumps_Present_Description = request.data.get('AUS_U_Swelling_Lumps_Present_Description')
    AUS_U_Swelling_Lumps_Present_Size = request.data.get('AUS_U_Swelling_Lumps_Present_Size')
    AUS_U_Swelling_Lumps_Present_Texture = request.data.get('AUS_U_Swelling_Lumps_Present_Texture')

    if AUS_U_Swelling_Lumps == 'Present':
        if AUS_U_Swelling_Lumps_Present_Description == None and AUS_U_Swelling_Lumps_Present_Size == None and AUS_U_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_U_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_U_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_U_Swelling_Lumps_Present_Texture'] = None

def check_AUS_Suprapubic_Pain(request):
    AUS_Suprapubic_Pain = request.data.get('AUS_Suprapubic_Pain')
    AUS_S_Pain_Yes_Pain_Score = request.data.get('AUS_S_Pain_Yes_Pain_Score')

    if AUS_Suprapubic_Pain == 'Yes':
        if AUS_S_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_S_Pain_Yes_Pain_Score'] = None

# need to check
def check_AUS_S_Tenderness(request):
    AUS_S_Tenderness = request.data.get('AUS_S_Tenderness')
    AUS_S_Tenderness_Present = request.data.get('AUS_S_Tenderness_Present')
    AUS_S_Tenderness_Present_Rebound = request.data.get('AUS_S_Tenderness_Present_Rebound')

    if AUS_S_Tenderness == 'Present':
        if AUS_S_Tenderness_Present == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_S_Tenderness_Present_Rebound'] = None
    
    elif AUS_S_Tenderness == 'Present Rebound':
        if AUS_S_Tenderness_Present_Rebound == None:
            raise Exception("You have to select Anyone")
        request.data['AUS_S_Tenderness_Present'] = None

    else:
        request.data['AUS_S_Tenderness_Present'] = None
        request.data['AUS_S_Tenderness_Present_Rebound'] = None

def check_AUS_S_Swelling_Lumps(request):
    AUS_S_Swelling_Lumps = request.data.get('AUS_S_Swelling_Lumps')
    AUS_S_Swelling_Lumps_Present_Description = request.data.get('AUS_S_Swelling_Lumps_Present_Description')
    AUS_S_Swelling_Lumps_Present_Size = request.data.get('AUS_S_Swelling_Lumps_Present_Size')
    AUS_S_Swelling_Lumps_Present_Texture = request.data.get('AUS_S_Swelling_Lumps_Present_Texture')

    if AUS_S_Swelling_Lumps == 'Present':
        if AUS_S_Swelling_Lumps_Present_Description == None and AUS_S_Swelling_Lumps_Present_Size == None and AUS_S_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_S_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_S_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_S_Swelling_Lumps_Present_Texture'] = None

def check_AUS_S_Uterus(request):
    AUS_S_Uterus = request.data.get('AUS_S_Uterus')
    AUS_S_Uterus_Palpable = request.data.get('AUS_S_Uterus_Palpable')

    if AUS_S_Uterus == 'Palpable':
        if AUS_S_Uterus_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_S_Uterus_Palpable'] = None

def check_AUS_Left_Hypochondrium_Pain(request):
    AUS_Left_Hypochondrium_Pain = request.data.get('AUS_Left_Hypochondrium_Pain')
    AUS_LH_Pain_Yes_Pain_Score = request.data.get('AUS_LH_Pain_Yes_Pain_Score')

    if AUS_Left_Hypochondrium_Pain == 'Yes':
        if AUS_LH_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LH_Pain_Yes_Pain_Score'] = None

def check_AUS_LH_Tenderness(request):
    AUS_LH_Tenderness = request.data.get('AUS_LH_Tenderness')
    AUS_LH_Tenderness_Present = request.data.get('AUS_LH_Tenderness_Present')

    if AUS_LH_Tenderness == 'Present':
        if AUS_LH_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LH_Tenderness_Present'] = None

def check_AUS_LH_Swelling_Lumps(request):
    AUS_LH_Swelling_Lumps = request.data.get('AUS_LH_Swelling_Lumps')
    AUS_LH_Swelling_Lumps_Present_Description = request.data.get('AUS_LH_Swelling_Lumps_Present_Description')
    AUS_LH_Swelling_Lumps_Present_Size = request.data.get('AUS_LH_Swelling_Lumps_Present_Size')
    AUS_LH_Swelling_Lumps_Present_Texture = request.data.get('AUS_LH_Swelling_Lumps_Present_Texture')

    if AUS_LH_Swelling_Lumps == 'Present':
        if AUS_LH_Swelling_Lumps_Present_Description == None and AUS_LH_Swelling_Lumps_Present_Size == None and AUS_LH_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LH_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_LH_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_LH_Swelling_Lumps_Present_Texture'] = None

def check_AUS_LH_Spleen(request):
    AUS_LH_Spleen = request.data.get('AUS_LH_Spleen')
    AUS_LH_Spleen_Palpable = request.data.get('AUS_LH_Spleen_Palpable')

    if AUS_LH_Spleen == 'Palpable':
        if AUS_LH_Spleen_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LH_Spleen_Palpable'] = None

def check_AUS_Left_Lumbar_Pain(request):
    AUS_Left_Lumbar_Pain = request.data.get('AUS_Left_Lumbar_Pain')
    AUS_LL_Pain_Yes_Pain_Score = request.data.get('AUS_LL_Pain_Yes_Pain_Score')

    if AUS_Left_Lumbar_Pain == 'Yes':
        if AUS_LL_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LL_Pain_Yes_Pain_Score'] = None

def check_AUS_LL_Tenderness(request):
    AUS_LL_Tenderness = request.data.get('AUS_LL_Tenderness')
    AUS_LL_Tenderness_Present = request.data.get('AUS_LL_Tenderness_Present')

    if AUS_LL_Tenderness == 'Present':
        if AUS_LL_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LL_Tenderness_Present'] = None

def check_AUS_LL_Swelling_Lumps(request):
    AUS_LL_Swelling_Lumps = request.data.get('AUS_LL_Swelling_Lumps')
    AUS_LL_Swelling_Lumps_Present_Description = request.data.get('AUS_LL_Swelling_Lumps_Present_Description')
    AUS_LL_Swelling_Lumps_Present_Size = request.data.get('AUS_LL_Swelling_Lumps_Present_Size')
    AUS_LL_Swelling_Lumps_Present_Texture = request.data.get('AUS_LL_Swelling_Lumps_Present_Texture')

    if AUS_LL_Swelling_Lumps == 'Present':
        if AUS_LL_Swelling_Lumps_Present_Description == None and AUS_LL_Swelling_Lumps_Present_Size == None and AUS_LL_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LL_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_LL_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_LL_Swelling_Lumps_Present_Texture'] = None

def check_AUS_LL_Left_Kidney(request):
    AUS_LL_Left_Kidney = request.data.get('AUS_LL_Left_Kidney')
    AUS_LL_Left_Kidney_Palpable = request.data.get('AUS_LL_Left_Kidney_Palpable')

    if AUS_LL_Left_Kidney == 'Palpable':
        if AUS_LL_Left_Kidney_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LL_Left_Kidney_Palpable'] = None

def check_AUS_Left_Iliac_Pain(request):
    AUS_Left_Iliac_Pain = request.data.get('AUS_Left_Iliac_Pain')
    AUS_LI_Pain_Yes_Pain_Score = request.data.get('AUS_LI_Pain_Yes_Pain_Score')

    if AUS_Left_Iliac_Pain == 'Yes':
        if AUS_LI_Pain_Yes_Pain_Score == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LI_Pain_Yes_Pain_Score'] = None

def check_AUS_LI_Tenderness(request):
    AUS_LI_Tenderness = request.data.get('AUS_LI_Tenderness')
    AUS_LI_Tenderness_Present = request.data.get('AUS_LI_Tenderness_Present')

    if AUS_LI_Tenderness == 'Present':
        if AUS_LI_Tenderness_Present == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LI_Tenderness_Present'] = None

def check_AUS_LI_Swelling_Lumps(request):
    AUS_LI_Swelling_Lumps = request.data.get('AUS_LI_Swelling_Lumps')
    AUS_LI_Swelling_Lumps_Present_Description = request.data.get('AUS_LI_Swelling_Lumps_Present_Description')
    AUS_LI_Swelling_Lumps_Present_Size = request.data.get('AUS_LI_Swelling_Lumps_Present_Size')
    AUS_LI_Swelling_Lumps_Present_Texture = request.data.get('AUS_LI_Swelling_Lumps_Present_Texture')

    if AUS_LI_Swelling_Lumps == 'Present':
        if AUS_LI_Swelling_Lumps_Present_Description == None and AUS_LI_Swelling_Lumps_Present_Size == None and AUS_LI_Swelling_Lumps_Present_Texture == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_LI_Swelling_Lumps_Present_Description'] = None
        request.data['AUS_LI_Swelling_Lumps_Present_Size'] = None
        request.data['AUS_LI_Swelling_Lumps_Present_Texture'] = None

def check_AUS_Hernia(request):
    AUS_Hernia = request.data.get('AUS_Hernia')
    AUS_Hernia_Present = request.data.get('AUS_Hernia_Present')

    if AUS_Hernia == 'Present':
        if AUS_Hernia_Present == None:
            raise Exception("You have to select Anyone")
    
    else:
        request.data['AUS_Hernia_Present'] = None

def check_AUS_Urinary_Bladder(request):
    AUS_Urinary_Bladder = request.data.get('AUS_Urinary_Bladder')
    AUS_Urinary_Bladder_Palpable = request.data.get('AUS_Urinary_Bladder_Palpable')

    if AUS_Urinary_Bladder == 'Palpable':
        if AUS_Urinary_Bladder_Palpable == None:
            raise Exception("You have to select Anyone")

    else:
        request.data['AUS_Urinary_Bladder_Palpable'] = None

# Section 6A Validations
def check_Pubertal_Girls(request):
    Pubertal_Assessment_Girls = request.data.get('Pubertal_Assessment_Girls')
    PAG_Tanner_Score = request.data.get('PAG_Tanner_Score')

    if Pubertal_Assessment_Girls == 'Indicated':
        if PAG_Tanner_Score is None:
            raise Exception("You have to select Anyone")
    else:
        request.data["PAG_Tanner_Score"] = None

def check_Years_Menarche_Attained(request):
    
    PAG_Menarche_Attained = request.data.get("PAG_Menarche_Attained")
    PAG_MA_Yes_Age_of_Menarche = request.data.get("PAG_MA_Yes_Age_of_Menarche")

    if PAG_Menarche_Attained == 'Yes':
        if PAG_MA_Yes_Age_of_Menarche is None:
            raise Exception("You have to select Anyone")
    else:
        request.data['PAG_MA_Yes_Age_of_Menarche'] = None
        request.data['PAG_MA_Yes_Character_Regularity'] = None
        request.data['PAG_MA_Yes_LMP_Date'] = None
        request.data['PAG_MA_Yes_Character_Frequency_in_Days'] = None
        request.data['PAG_MA_Yes_Duration_in_days'] = None
        request.data['PAG_MA_Yes_Flow'] = None
        request.data['PAG_MA_Yes_Comfort'] = None
        request.data['PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses'] = None
        request.data['PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes'] = None
        request.data['PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other'] = None
        request.data['PAG_Yes_Cracking_of_Voice_or_chnage_in_voice'] = None

def check_PAG_during_menses(request):
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses = request.data.get('PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses')
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes = request.data.get('PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes')
    PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other = request.data.get('PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes')
    
    if PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses == 'Yes':
        if PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes is None:
            raise Exception("You have to select Anyone")
        
        selected_values = request.data.get('PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes', '').split(',')
        Other_value = None
        
        for i in selected_values:
            if i == "Other":
                Other_value = PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other
        request.data['PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other'] = Other_value


        

    else:
        request.data['PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes'] = None
        request.data['PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other'] = None
 
def check_Pubertal_Girls_Behaviour(request):
    PAG_HaveYouExperienced_A_change_in_behaviour_recently = request.data.get("PAG_HaveYouExperienced_A_change_in_behaviour_recently")
    PAG_Change_behaviour_Yes = request.data.get("PAG_Change_behaviour_Yes")
    PAG_Change_behaviour_Yes_Quiet_Withdrawn = request.data.get("PAG_Change_behaviour_Yes_Quiet_Withdrawn")
    PAG_Change_behaviour_Outgoing = request.data.get("PAG_Change_behaviour_Outgoing")
    PAG_Change_behaviour_Aggressive = request.data.get("PAG_Change_behaviour_Aggressive")
    PAG_Change_behaviour_Bold_and_Daring = request.data.get("PAG_Change_behaviour_Bold_and_Daring")
    PAG_Change_behaviour_Careless = request.data.get("PAG_Change_behaviour_Careless")

    if PAG_HaveYouExperienced_A_change_in_behaviour_recently == 'Yes':
        if PAG_Change_behaviour_Yes == None:
            raise Exception("You have to select yes")
        selected_values = request.data.get('PAG_Change_behaviour_Yes', '').split(',')
        Quiet_Withdrawn_value = None
        Outgoing_value = None
        Aggressive_value = None
        Bold_and_Daring_value = None
        Caring_value = None

        for i in selected_values:
            if i == 'Quiet and Withdrawn':
                Quiet_Withdrawn_value = PAG_Change_behaviour_Yes_Quiet_Withdrawn
            elif i == 'Outgoing':
                Outgoing_value = PAG_Change_behaviour_Outgoing
            elif i == 'Aggressive':
                Aggressive_value = PAG_Change_behaviour_Aggressive
            elif i == 'Bold and Daring':
                Bold_and_Daring_value = PAG_Change_behaviour_Bold_and_Daring
            elif i == 'Careless':
                Caring_value = PAG_Change_behaviour_Careless

        request.data['PAG_Change_behaviour_Yes_Quiet_Withdrawn'] = Quiet_Withdrawn_value
        request.data['PAG_Change_behaviour_Outgoing'] = Outgoing_value
        request.data['PAG_Change_behaviour_Aggressive'] = Aggressive_value
        request.data['PAG_Change_behaviour_Bold_and_Daring'] = Bold_and_Daring_value
        request.data['PAB_Change_behaviour_Careless'] = Caring_value       
    else:
        request.data['PAG_Change_behaviour_Yes'] = None
        request.data['PAG_Change_behaviour_Yes_Quiet_Withdrawn'] = None
        request.data['PAG_Change_behaviour_Outgoing'] = None
        request.data['PAG_Change_behaviour_Aggressive'] = None
        request.data['PAG_Change_behaviour_Bold_and_Daring'] = None
        request.data['PAB_Change_behaviour_Careless'] = None

def check_PAG_Abnormal_finding(request):
    PAG_Any_other_abnormal_finding = request.data.get("PAG_Any_other_abnormal_finding")
    PAG_Any_other_abnormal_finding_Yes = request.data.get("PAG_Any_other_abnormal_finding_Yes")

    if PAG_Any_other_abnormal_finding == 'Yes':
        if PAG_Any_other_abnormal_finding_Yes is None:
            raise Exception("You have to select anyone")
    else:
        request.data['PAG_Any_other_abnormal_finding_Yes'] = None

# Section 6B Validations
def check_Pubertal_Boys(request):

    Pubertal_Assessment_Boys = request.data.get("Pubertal_Assessment_Boys")
    PAB_Tanner_Score = request.data.get("PAB_Tanner_Score")

    if Pubertal_Assessment_Boys == 'Indicated':
        if PAB_Tanner_Score is None:
            raise Exception("You have to select Anyone")
    else:
        request.data['PAB_Tanner_Score'] = None

def check_Pubertal_Behaviour(request):
    PAB_HaveYouExperienced_A_change_in_behaviour_recently = request.data.get("PAB_HaveYouExperienced_A_change_in_behaviour_recently")
    PAB_Change_behaviour_Yes = request.data.get("PAB_Change_behaviour_Yes")
    PAB_Change_behaviour_Yes_Quiet_Withdrawn = request.data.get("PAB_Change_behaviour_Yes_Quiet_Withdrawn")
    PAB_Change_behaviour_Outgoing = request.data.get("PAB_Change_behaviour_Outgoing")
    PAB_Change_behaviour_Aggressive = request.data.get("PAB_Change_behaviour_Aggressive")
    PAB_Change_behaviour_Bold_and_Daring = request.data.get("PAB_Change_behaviour_Bold_and_Daring")
    PAB_Change_behaviour_Careless = request.data.get("PAB_Change_behaviour_Careless")

    if PAB_HaveYouExperienced_A_change_in_behaviour_recently == 'Yes':
        if PAB_Change_behaviour_Yes == None:
            raise Exception("You have to select yes")
        selected_values = request.data.get('PAB_Change_behaviour_Yes', '').split(',')
        Quiet_Withdrawn_value = None
        Outgoing_value = None
        Aggressive_value = None
        Bold_and_Daring_value = None
        Caring_value = None

        for i in selected_values:
            if i == 'Quiet and Withdrawn':
                Quiet_Withdrawn_value = PAB_Change_behaviour_Yes_Quiet_Withdrawn
            elif i == 'Outgoing':
                Outgoing_value = PAB_Change_behaviour_Outgoing
            elif i == 'Aggressive':
                Aggressive_value = PAB_Change_behaviour_Aggressive
            elif i == 'Bold and Daring':
                Bold_and_Daring_value = PAB_Change_behaviour_Bold_and_Daring
            elif i == 'Careless':
                Caring_value = PAB_Change_behaviour_Careless
            request.data['PAB_Change_behaviour_Yes_Quiet_Withdrawn'] = Quiet_Withdrawn_value
            request.data['PAB_Change_behaviour_Outgoing'] = Outgoing_value
            request.data['PAB_Change_behaviour_Aggressive'] = Aggressive_value
            request.data['PAB_Change_behaviour_Bold_and_Daring'] = Bold_and_Daring_value
            request.data['PAB_Change_behaviour_Careless'] = Caring_value       
    else:
        request.data['PAB_Change_behaviour_Yes'] = None
        request.data['PAB_Change_behaviour_Yes_Quiet_Withdrawn'] = None
        request.data['PAB_Change_behaviour_Outgoing'] = None
        request.data['PAB_Change_behaviour_Aggressive'] = None
        request.data['PAB_Change_behaviour_Bold_and_Daring'] = None
        request.data['PAB_Change_behaviour_Careless'] = None
    
def check_Abnormal_finding(request):
    PAB_Any_other_abnormal_finding = request.data.get("PAB_Any_other_abnormal_finding")
    PAB_Any_other_abnormal_finding_Yes = request.data.get("PAB_Any_other_abnormal_finding_Yes")

    if PAB_Any_other_abnormal_finding == 'Yes':
        if PAB_Any_other_abnormal_finding_Yes is None:
            raise Exception("You have to select anyone")
    else:
        request.data['PAB_Any_other_abnormal_finding_Yes'] = None

# Section 7 Validations
def check_History_medication(request):
    History_of_Medication = request.data.get("History_of_Medication")
    History_of_Medication_Yes = request.data.get("History_of_Medication_Yes")

    if History_of_Medication == 'Yes':
        if History_of_Medication_Yes is None:
            raise Exception("You have to select anyone")     
    else:
        request.data['History_of_Medication_Yes'] = None
        request.data['Name_of_Medication'] = None
        
    

