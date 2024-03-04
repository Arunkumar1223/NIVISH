#Sction 1 Validations
def check_Child_Mobility(request):
    Child_Mobility = request.data.get('Child_Mobility')
    Child_Mobility_Can_not_Walk = request.data.get('Child_Mobility_Can_not_Walk')
    Child_Mobility_Can_not_Walk_other = request.data.get('Child_Mobility_Can_not_Walk_other')

    if Child_Mobility == 'Can not Walk':
        if Child_Mobility_Can_not_Walk == None:
            raise Exception("You have to select Anyone")
        
        elif Child_Mobility_Can_not_Walk == 'Other':
            if Child_Mobility_Can_not_Walk_other == None:
                raise Exception("You have to select Anyone")
        else:
            
            request.data['Child_Mobility_Can_not_Walk_other'] = None
                
    else:
        request.data['Child_Mobility_Can_not_Walk'] = None
        request.data['Child_Mobility_Can_not_Walk_other'] = None
        
def check_Student_Ambulant(request):
    Student_Ambulant = request.data.get('Student_Ambulant')
    Student_Ambulant_No = request.data.get('Student_Ambulant_No')

    if Student_Ambulant == 'No':
        if Student_Ambulant_No == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['Student_Ambulant_No'] = None

def check_Gait(request):
    Gait = request.data.get('Gait')
    Gait_Abnormal = request.data.get('Gait_Abnormal')
    Gait_Abnormal_Limp = request.data.get('Gait_Abnormal_Limp')
    Gait_Abnormal_Limp_other = request.data.get('Gait_Abnormal_Limp_other')

    if Gait == 'Abnormal':
        if Gait_Abnormal == None:
            raise Exception("You have to select Anyone")
        elif Gait_Abnormal == 'Limp':
           if Gait_Abnormal_Limp == None:
               raise Exception("You have to select Anyone")
           
           elif Gait_Abnormal_Limp == 'Other causes':
               if Gait_Abnormal_Limp_other == None:
                   raise Exception("You have to select Anyone")
           else:
               request.data['Gait_Abnormal_Limp_other'] = None
                
    else:
        request.data['Gait_Abnormal'] = None
        request.data['Gait_Abnormal_Limp'] = None
        request.data['Gait_Abnormal_Limp_other'] = None

def check_Wear_Brace_Support(request):
    Wear_Brace_Support = request.data.get('Wear_Brace_Support')
    Wear_Brace_Support_Yes = request.data.get('Wear_Brace_Support_Yes')

    if Wear_Brace_Support == 'Yes':
        if Wear_Brace_Support_Yes == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['Wear_Brace_Support_Yes'] = None

def check_Prosthesis(request):
    Prosthesis = request.data.get('Prosthesis')
    Prosthesis_Yes = request.data.get('Prosthesis_Yes')
    Prosthesis_Yes_other = request.data.get('Prosthesis_Yes_other')

    if Prosthesis == 'Yes':
        if Prosthesis_Yes == None:
            raise Exception("You have to select Anyone")
        elif Prosthesis_Yes == 'Other':
            if Prosthesis_Yes_other == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['Prosthesis_Yes_other'] = None
                
    else:
        request.data['Prosthesis_Yes'] = None
        request.data['Prosthesis_Yes_other'] = None

def check_Spine_Appearance(request):
    Spine_Appearance = request.data.get('Spine_Appearance')
    Spine_Appearance_Abnormal = request.data.get('Spine_Appearance_Abnormal')
    Spine_Appearance_Abnormal_Other = request.data.get('Spine_Appearance_Abnormal_Other')

    if Spine_Appearance == 'Abnormal':
        if Spine_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
        elif Spine_Appearance_Abnormal == 'Other':
            if Spine_Appearance_Abnormal_Other == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['Spine_Appearance_Abnormal_Other'] = None
                
    else:
        request.data['Spine_Appearance_Abnormal'] = None
        request.data['Spine_Appearance_Abnormal_Other'] = None

def check_Shoulder_Griddle_Appearance(request):
    Shoulder_Griddle_Appearance = request.data.get('Shoulder_Griddle_Appearance')
    Shoulder_Griddle_Appearance_Abnormal = request.data.get('Shoulder_Griddle_Appearance_Abnormal')
    Shoulder_Griddle_Appearance_Abnormal_Other = request.data.get('Shoulder_Griddle_Appearance_Abnormal_Other')

    if Shoulder_Griddle_Appearance == 'Abnormal':
        if Shoulder_Griddle_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
        elif Shoulder_Griddle_Appearance_Abnormal == 'Other':
            if Shoulder_Griddle_Appearance_Abnormal_Other == None:
                raise Exception("You have to select Anyone")
        else:
            request.data['Shoulder_Griddle_Appearance_Abnormal_Other'] = None
                
    else:
        request.data['Shoulder_Griddle_Appearance_Abnormal'] = None
        request.data['Shoulder_Griddle_Appearance_Abnormal_Other'] = None

def check_Spine_Mobility(request):
    Spine_Mobility = request.data.get('Spine_Mobility')
    Spine_Mobility_Restricted_movement = request.data.get('Spine_Mobility_Restricted_movement')

    if Spine_Mobility == 'Restricted movement':
        if Spine_Mobility_Restricted_movement == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['Spine_Mobility_Restricted_movement'] = None

def check_Neck_Mobility(request):
    Neck_Mobility = request.data.get('Neck_Mobility')
    Neck_Mobility_Restricted_movement = request.data.get('Neck_Mobility_Restricted_movement')

    if Neck_Mobility == 'Restricted movement':
        if Neck_Mobility_Restricted_movement == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['Neck_Mobility_Restricted_movement'] = None
        
#Section2 Validations
def check_UL_Right_Appearance(request):
    UL_Right_Appearance = request.data.get('UL_Right_Appearance')
    UL_Right_Appearance_Abnormal = request.data.get('UL_Right_Appearance_Abnormal')

    if UL_Right_Appearance == 'Abnormal':
        if UL_Right_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Right_Appearance_Abnormal'] = None

def check_UL_Right_Deep_Tendon_Reflexes_Biceps(request):
    UL_Right_Deep_Tendon_Reflexes_Biceps = request.data.get('UL_Right_Deep_Tendon_Reflexes_Biceps')
    UL_Right_DTR_Biceps_Abnormal = request.data.get('UL_Right_DTR_Biceps_Abnormal')

    if UL_Right_Deep_Tendon_Reflexes_Biceps == 'Abnormal':
        if UL_Right_DTR_Biceps_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Right_DTR_Biceps_Abnormal'] = None

def check_UL_Right_Deep_Tendon_Reflexes_Radial(request):
    UL_Right_Deep_Tendon_Reflexes_Radial = request.data.get('UL_Right_Deep_Tendon_Reflexes_Radial')
    UL_Right_DTR_Radial_Abnormal = request.data.get('UL_Right_DTR_Radial_Abnormal')

    if UL_Right_Deep_Tendon_Reflexes_Radial == 'Abnormal':
        if UL_Right_DTR_Radial_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Right_DTR_Radial_Abnormal'] = None

def check_UL_Right_Motor_Function_Range_of_Movement(request):
    UL_Right_Motor_Function_Range_of_Movement = request.data.get('UL_Right_Motor_Function_Range_of_Movement')
    UL_Right_MF_RM_Abnormal = request.data.get('UL_Right_MF_RM_Abnormal')
    UL_Right_MF_RM_Abnormal_Hyper_Flexible = request.data.get('UL_Right_MF_RM_Abnormal_Hyper_Flexible')
    UL_Right_MF_RM_Abnormal_Restricted = request.data.get('UL_Right_MF_RM_Abnormal_Restricted')

    if UL_Right_Motor_Function_Range_of_Movement == 'Abnormal':
        if UL_Right_MF_RM_Abnormal == None:
            raise Exception("You have to select Anyone")
        
        elif UL_Right_MF_RM_Abnormal == 'Hyper Flexible':
           request.data['UL_Right_MF_RM_Abnormal_Restricted'] = None
           if UL_Right_MF_RM_Abnormal_Hyper_Flexible == None:
            raise Exception("You have to select Anyone")
           
        elif UL_Right_MF_RM_Abnormal == 'Restricted':
           request.data['UL_Right_MF_RM_Abnormal_Hyper_Flexible'] = None
           if UL_Right_MF_RM_Abnormal_Restricted == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Right_MF_RM_Abnormal'] = None
        request.data['UL_Right_MF_RM_Abnormal_Hyper_Flexible'] = None
        request.data['UL_Right_MF_RM_Abnormal_Restricted'] = None

def check_UL_Right_Deep_Tendon_Reflexes_Sensory_Function(request):
    UL_Right_Deep_Tendon_Reflexes_Sensory_Function = request.data.get('UL_Right_Deep_Tendon_Reflexes_Sensory_Function')
    UL_Right_DTR_SF_Abnormal = request.data.get('UL_Right_DTR_SF_Abnormal')
    UL_Right_DTR_SF_Abnormal_Touch = request.data.get('UL_Right_DTR_SF_Abnormal_Touch')
    UL_Right_DTR_SF_Abnormal_Pain_Present = request.data.get('UL_Right_DTR_SF_Abnormal_Pain_Present')
    UL_Right_DTR_SF_Abnormal_Pressure_Abnormal = request.data.get('UL_Right_DTR_SF_Abnormal_Pressure_Abnormal')
    UL_Right_DTR_SF_Abnormal_Tenderness_Present = request.data.get('UL_Right_DTR_SF_Abnormal_Tenderness_Present')

    if UL_Right_Deep_Tendon_Reflexes_Sensory_Function == 'Abnormal':
        if UL_Right_DTR_SF_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('UL_Right_DTR_SF_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Touch_Abnormal_value = None
        Pain_Present_value = None
        Pressure_Abnormal_value = None
        Tenderness_Present_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Touch Abnormal":
                Touch_Abnormal_value = UL_Right_DTR_SF_Abnormal_Touch
            elif i == "Pain Present":
                Pain_Present_value = UL_Right_DTR_SF_Abnormal_Pain_Present
            elif i == "Pressure Abnormal":
                Pressure_Abnormal_value = UL_Right_DTR_SF_Abnormal_Pressure_Abnormal
            elif i == "Tenderness Present":
                Tenderness_Present_value = UL_Right_DTR_SF_Abnormal_Tenderness_Present

        # Set the values for each option in the request data
        request.data['UL_Right_DTR_SF_Abnormal_Touch'] = Touch_Abnormal_value
        request.data['UL_Right_DTR_SF_Abnormal_Pain_Present'] = Pain_Present_value
        request.data['UL_Right_DTR_SF_Abnormal_Pressure_Abnormal'] = Pressure_Abnormal_value
        request.data['UL_Right_DTR_SF_Abnormal_Tenderness_Present'] = Tenderness_Present_value

    else:
        request.data['UL_Right_DTR_SF_Abnormal'] = None
        request.data['UL_Right_DTR_SF_Abnormal_Touch'] = None
        request.data['UL_Right_DTR_SF_Abnormal_Pain_Present'] = None
        request.data['UL_Right_DTR_SF_Abnormal_Pressure_Abnormal'] = None
        request.data['UL_Right_DTR_SF_Abnormal_Tenderness_Present'] = None

def check_UL_Left_Appearance(request):
    UL_Left_Appearance = request.data.get('UL_Left_Appearance')
    UL_Left_Appearance_Abnormal = request.data.get('UL_Left_Appearance_Abnormal')

    if UL_Left_Appearance == 'Abnormal':
        if UL_Left_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Left_Appearance_Abnormal'] = None

def check_UL_Left_Deep_Tendon_Reflexes_Biceps(request):
    UL_Left_Deep_Tendon_Reflexes_Biceps = request.data.get('UL_Left_Deep_Tendon_Reflexes_Biceps')
    UL_Left_DTR_Biceps_Abnormal = request.data.get('UL_Left_DTR_Biceps_Abnormal')

    if UL_Left_Deep_Tendon_Reflexes_Biceps == 'Abnormal':
        if UL_Left_DTR_Biceps_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Left_DTR_Biceps_Abnormal'] = None

def check_UL_Left_Deep_Tendon_Reflexes_Radial(request):
    UL_Left_Deep_Tendon_Reflexes_Radial = request.data.get('UL_Left_Deep_Tendon_Reflexes_Radial')
    UL_Left_DTR_Radial_Abnormal = request.data.get('UL_Left_DTR_Radial_Abnormal')

    if UL_Left_Deep_Tendon_Reflexes_Radial == 'Abnormal':
        if UL_Left_DTR_Radial_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_Left_DTR_Radial_Abnormal'] = None

def check_UL_Left_Motor_Function_Range_of_Movement(request):
    UL_Left_Motor_Function_Range_of_Movement = request.data.get('UL_Left_Motor_Function_Range_of_Movement')
    UL_left_MF_RM_Abnormal = request.data.get('UL_left_MF_RM_Abnormal')
    UL_Left_MF_RM_Abnormal_Hyper_Flexible = request.data.get('UL_Left_MF_RM_Abnormal_Hyper_Flexible')
    UL_Left_MF_RM_Abnormal_Restricted = request.data.get('UL_Left_MF_RM_Abnormal_Restricted')

    if UL_Left_Motor_Function_Range_of_Movement == 'Abnormal':
        if UL_left_MF_RM_Abnormal == None:
            raise Exception("You have to select Anyone")
        
        elif UL_left_MF_RM_Abnormal == 'Hyper Flexible':
           request.data['UL_Left_MF_RM_Abnormal_Restricted'] = None
           if UL_Left_MF_RM_Abnormal_Hyper_Flexible == None:
            raise Exception("You have to select Anyone")
           
        elif UL_left_MF_RM_Abnormal == 'Restricted':
           request.data['UL_Left_MF_RM_Abnormal_Hyper_Flexible'] = None
           if UL_Left_MF_RM_Abnormal_Restricted == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['UL_left_MF_RM_Abnormal'] = None
        request.data['UL_Left_MF_RM_Abnormal_Hyper_Flexible'] = None
        request.data['UL_Left_MF_RM_Abnormal_Restricted'] = None

def check_UL_Left_Deep_Tendon_Reflexes_Sensory_Function(request):
    UL_Left_Deep_Tendon_Reflexes_Sensory_Function = request.data.get('UL_Left_Deep_Tendon_Reflexes_Sensory_Function')
    UL_Left_DTR_SF_Abnormal = request.data.get('UL_Left_DTR_SF_Abnormal')
    UL_Left_DTR_SF_Abnormal_Touch = request.data.get('UL_Left_DTR_SF_Abnormal_Touch')
    UL_Left_DTR_SF_Abnormal_Pain_Present = request.data.get('UL_Left_DTR_SF_Abnormal_Pain_Present')
    UL_Left_DTR_SF_Abnormal_Pressure_Abnormal = request.data.get('UL_Left_DTR_SF_Abnormal_Pressure_Abnormal')
    UL_Left_DTR_SF_Abnormal_Tenderness_Present = request.data.get('UL_Left_DTR_SF_Abnormal_Tenderness_Present')

    if UL_Left_Deep_Tendon_Reflexes_Sensory_Function == 'Abnormal':
        if UL_Left_DTR_SF_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('UL_Left_DTR_SF_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Touch_Abnormal_value = None
        Pain_Present_value = None
        Pressure_Abnormal_value = None
        Tenderness_Present_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Touch Abnormal":
                Touch_Abnormal_value = UL_Left_DTR_SF_Abnormal_Touch
            elif i == "Pain Present":
                Pain_Present_value = UL_Left_DTR_SF_Abnormal_Pain_Present
            elif i == "Pressure Abnormal":
                Pressure_Abnormal_value = UL_Left_DTR_SF_Abnormal_Pressure_Abnormal
            elif i == "Tenderness Present":
                Tenderness_Present_value = UL_Left_DTR_SF_Abnormal_Tenderness_Present

        # Set the values for each option in the request data
        request.data['UL_Left_DTR_SF_Abnormal_Touch'] = Touch_Abnormal_value
        request.data['UL_Left_DTR_SF_Abnormal_Pain_Present'] = Pain_Present_value
        request.data['UL_Left_DTR_SF_Abnormal_Pressure_Abnormal'] = Pressure_Abnormal_value
        request.data['UL_Left_DTR_SF_Abnormal_Tenderness_Present'] = Tenderness_Present_value

    else:
        request.data['UL_Left_DTR_SF_Abnormal'] = None
        request.data['UL_Left_DTR_SF_Abnormal_Touch'] = None
        request.data['UL_Left_DTR_SF_Abnormal_Pain_Present'] = None
        request.data['UL_Left_DTR_SF_Abnormal_Pressure_Abnormal'] = None
        request.data['UL_Left_DTR_SF_Abnormal_Tenderness_Present'] = None

#Section3 Validations
def check_LL_Right_Appearance(request):
    LL_Right_Appearance = request.data.get('LL_Right_Appearance')
    LL_Right_Appearance_Abnormal = request.data.get('LL_Right_Appearance_Abnormal')

    if LL_Right_Appearance == 'Abnormal':
        if LL_Right_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['LL_Right_Appearance_Abnormal'] = None

def check_LL_Right_Motor_Function_Knee(request):
    LL_Right_Motor_Function_Knee = request.data.get('LL_Right_Motor_Function_Knee')
    LL_Right_Motor_Function_Knee_Abnormal = request.data.get('LL_Right_Motor_Function_Knee_Abnormal')

    if LL_Right_Motor_Function_Knee == 'Abnormal':
        if LL_Right_Motor_Function_Knee_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['LL_Right_Motor_Function_Knee_Abnormal'] = None

def check_LL_Right_Deep_Tendon_Reflexes_Sensory_Function(request):
    LL_Right_Deep_Tendon_Reflexes_Sensory_Function = request.data.get('LL_Right_Deep_Tendon_Reflexes_Sensory_Function')
    LL_Right_DTR_SF_Abnormal = request.data.get('LL_Right_DTR_SF_Abnormal')
    LL_Right_DTR_SF_Abnormal_Touch = request.data.get('LL_Right_DTR_SF_Abnormal_Touch')
    LL_Right_DTR_SF_Abnormal_Pain_Present = request.data.get('LL_Right_DTR_SF_Abnormal_Pain_Present')
    LL_Right_DTR_SF_Abnormal_Pressure_Abnormal = request.data.get('UL_Left_DTR_SF_Abnormal_Pressure_Abnormal')
    LL_Right_DTR_SF_Abnormal_Tenderness_Present = request.data.get('UL_Left_DTR_SF_Abnormal_Tenderness_Present')

    if LL_Right_Deep_Tendon_Reflexes_Sensory_Function == 'Abnormal':
        if LL_Right_DTR_SF_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('LL_Right_DTR_SF_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Touch_Abnormal_value = None
        Pain_Present_value = None
        Pressure_Abnormal_value = None
        Tenderness_Present_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Touch Abnormal":
                Touch_Abnormal_value = LL_Right_DTR_SF_Abnormal_Touch
            elif i == "Pain Present":
                Pain_Present_value = LL_Right_DTR_SF_Abnormal_Pain_Present
            elif i == "Pressure Abnormal":
                Pressure_Abnormal_value = LL_Right_DTR_SF_Abnormal_Pressure_Abnormal
            elif i == "Tenderness Present":
                Tenderness_Present_value = LL_Right_DTR_SF_Abnormal_Tenderness_Present

        # Set the values for each option in the request data
        request.data['LL_Right_DTR_SF_Abnormal_Touch'] = Touch_Abnormal_value
        request.data['LL_Right_DTR_SF_Abnormal_Pain_Present'] = Pain_Present_value
        request.data['LL_Right_DTR_SF_Abnormal_Pressure_Abnormal'] = Pressure_Abnormal_value
        request.data['LL_Right_DTR_SF_Abnormal_Tenderness_Present'] = Tenderness_Present_value

    else:
        request.data['LL_Right_DTR_SF_Abnormal'] = None
        request.data['LL_Right_DTR_SF_Abnormal_Touch'] = None
        request.data['LL_Right_DTR_SF_Abnormal_Pain_Present'] = None
        request.data['LL_Right_DTR_SF_Abnormal_Pressure_Abnormal'] = None
        request.data['LL_Right_DTR_SF_Abnormal_Tenderness_Present'] = None

def check_LL_Left_Appearance(request):
    LL_Left_Appearance = request.data.get('LL_Left_Appearance')
    LL_Left_Appearance_Abnormal = request.data.get('LL_Left_Appearance_Abnormal')

    if LL_Left_Appearance == 'Abnormal':
        if LL_Left_Appearance_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['LL_Left_Appearance_Abnormal'] = None

def check_LL_Left_Motor_Function_Knee(request):
    LL_Left_Motor_Function_Knee = request.data.get('LL_Left_Motor_Function_Knee')
    LL_Left_Motor_Function_Knee_Abnormal = request.data.get('LL_Left_Motor_Function_Knee_Abnormal')

    if LL_Left_Motor_Function_Knee == 'Abnormal':
        if LL_Left_Motor_Function_Knee_Abnormal == None:
            raise Exception("You have to select Anyone")
                
    else:
        request.data['LL_Left_Motor_Function_Knee_Abnormal'] = None

def check_LL_Left_Deep_Tendon_Reflexes_Sensory_Function(request):
    LL_Left_Deep_Tendon_Reflexes_Sensory_Function = request.data.get('LL_Left_Deep_Tendon_Reflexes_Sensory_Function')
    LL_Left_DTR_SF_Abnormal = request.data.get('LL_Left_DTR_SF_Abnormal')
    LL_Left_DTR_SF_Abnormal_Touch = request.data.get('LL_Left_DTR_SF_Abnormal_Touch')
    LL_Left_DTR_SF_Abnormal_Pain_Present = request.data.get('LL_Left_DTR_SF_Abnormal_Pain_Present')
    LL_Left_DTR_SF_Abnormal_Pressure_Abnormal = request.data.get('LL_Left_DTR_SF_Abnormal_Pressure_Abnormal')
    LL_Left_DTR_SF_Abnormal_Tenderness_Present = request.data.get('LL_Left_DTR_SF_Abnormal_Tenderness_Present')

    if LL_Left_Deep_Tendon_Reflexes_Sensory_Function == 'Abnormal':
        if LL_Left_DTR_SF_Abnormal == None:
            raise Exception("You have to select Anyone")
        selected_values = request.data.get('LL_Left_DTR_SF_Abnormal', '').split(',')
        # Initialize variables to store the values for each option
        Touch_Abnormal_value = None
        Pain_Present_value = None
        Pressure_Abnormal_value = None
        Tenderness_Present_value = None

        # Loop through the selected values and set the corresponding variables
        for i in selected_values:
            if i == "Touch Abnormal":
                Touch_Abnormal_value = LL_Left_DTR_SF_Abnormal_Touch
            elif i == "Pain Present":
                Pain_Present_value = LL_Left_DTR_SF_Abnormal_Pain_Present
            elif i == "Pressure Abnormal":
                Pressure_Abnormal_value = LL_Left_DTR_SF_Abnormal_Pressure_Abnormal
            elif i == "Tenderness Present":
                Tenderness_Present_value = LL_Left_DTR_SF_Abnormal_Tenderness_Present

        # Set the values for each option in the request data
        request.data['LL_Left_DTR_SF_Abnormal_Touch'] = Touch_Abnormal_value
        request.data['LL_Left_DTR_SF_Abnormal_Pain_Present'] = Pain_Present_value
        request.data['LL_Left_DTR_SF_Abnormal_Pressure_Abnormal'] = Pressure_Abnormal_value
        request.data['LL_Left_DTR_SF_Abnormal_Tenderness_Present'] = Tenderness_Present_value

    else:
        request.data['LL_Left_DTR_SF_Abnormal'] = None
        request.data['LL_Left_DTR_SF_Abnormal_Touch'] = None
        request.data['LL_Left_DTR_SF_Abnormal_Pain_Present'] = None
        request.data['LL_Left_DTR_SF_Abnormal_Pressure_Abnormal'] = None
        request.data['LL_Left_DTR_SF_Abnormal_Tenderness_Present'] = None