#Section 1
def check_Do_you_have_problem_inhearing_your_Teachers_Friends_Parents(request):
    Do_you_have_problem_inhearing_your_Teachers_Friends_Parents = request.data.get('Do_you_have_problem_inhearing_your_Teachers_Friends_Parents')
    Do_you_have_problem_inhearing_your_Teachers_Yes = request.data.get('Do_you_have_problem_inhearing_your_Teachers_Yes')
    if Do_you_have_problem_inhearing_your_Teachers_Friends_Parents == 'Yes':
        if Do_you_have_problem_inhearing_your_Teachers_Yes == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Do_you_have_problem_inhearing_your_Teachers_Yes'] = None

def check_Does_any_fluid_come_out_of_your_ears(request):
    Does_any_fluid_come_out_of_your_ears = request.data.get('Does_any_fluid_come_out_of_your_ears')
    Does_any_fluid_come_out_of_your_ears_Yes = request.data.get('Does_any_fluid_come_out_of_your_ears_Yes')
    if Does_any_fluid_come_out_of_your_ears == 'Yes':
        if Does_any_fluid_come_out_of_your_ears_Yes == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Does_any_fluid_come_out_of_your_ears_Yes'] = None

#Section 2
def check_Visual_inspection_Right_Ear_Pinna(request):
    Visual_inspection_Right_Ear_Pinna = request.data.get('Visual_inspection_Right_Ear_Pinna')
    Visual_inspection_Right_Ear_Pinna_Abnormal = request.data.get('Visual_inspection_Right_Ear_Pinna_Abnormal')
    if Visual_inspection_Right_Ear_Pinna == 'Abnormal':
        if Visual_inspection_Right_Ear_Pinna_Abnormal == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Visual_inspection_Right_Ear_Pinna_Abnormal'] = None

def check_Visual_inspection_Right_Ear_EarCanal(request):
    Visual_inspection_Right_Ear_EarCanal = request.data.get('Visual_inspection_Right_Ear_EarCanal')
    Visual_inspection_Right_Ear_EarCanal_Abnormal = request.data.get('Visual_inspection_Right_Ear_EarCanal_Abnormal')
    if Visual_inspection_Right_Ear_EarCanal == 'Abnormal':
        if Visual_inspection_Right_Ear_EarCanal_Abnormal == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Visual_inspection_Right_Ear_EarCanal_Abnormal'] = None

def check_Visual_inspection_Left_Ear_Pinna(request):
    Visual_inspection_Left_Ear_Pinna = request.data.get('Visual_inspection_Left_Ear_Pinna')
    Visual_inspection_Left_Ear_Pinna_Abnormal = request.data.get('Visual_inspection_Left_Ear_Pinna_Abnormal')
    if Visual_inspection_Left_Ear_Pinna == 'Abnormal':
        if Visual_inspection_Left_Ear_Pinna_Abnormal == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Visual_inspection_Left_Ear_Pinna_Abnormal'] = None

def check_Visual_inspection_Left_Ear_EarCanal(request):
    Visual_inspection_Left_Ear_EarCanal = request.data.get('Visual_inspection_Left_Ear_EarCanal')
    Visual_inspection_Left_Ear_EarCanal_Abnormal = request.data.get('Visual_inspection_Left_Ear_EarCanal_Abnormal')
    if Visual_inspection_Left_Ear_EarCanal == 'Abnormal':
        if Visual_inspection_Left_Ear_EarCanal_Abnormal == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Visual_inspection_Left_Ear_EarCanal_Abnormal'] = None

#Section 3
def check_Pure_Tone_Audiometry_Right_Ear_500Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_500Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_500Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB(request):
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB')
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer'] = None


def check_Pure_Tone_Audiometry_Left_Ear_500Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_500Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_500Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer'] = None

def check_Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB(request):
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB = request.data.get('Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB')
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer = request.data.get('Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer')
    if Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB == 'Refer':
        if Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer == None:
            raise Exception("Please provide any text that needs to be filled in.")
        
    else:
        request.data['Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer'] = None