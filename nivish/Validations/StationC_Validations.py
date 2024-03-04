def check_VisionCorrected(request):
    VisionCorrected = request.data.get('Vision_Corrected')
    Vision_Corrected_Yes = request.data.get('Vision_Corrected_Yes') 
    
    if VisionCorrected == 'Yes':
            if Vision_Corrected_Yes == None:
                    raise Exception("You have to select atleast one field")
    else:
        request.data['Vision_Corrected_Yes'] = None


def check_Visually_Challenged(request):
    Visually_Challenged_Right_Eye = request.data.get("Visually_Challenged_Right_Eye")
    Visually_Challenged_Right_Eye_Enucleation = request.data.get("Visually_Challenged_Right_Eye_Enucleation")
    Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other = request.data.get("Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other")
    Visually_Challenged_Right_Eye_Enucleation_Cataract = request.data.get("Visually_Challenged_Right_Eye_Enucleation_Cataract")
    Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = request.data.get("Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity")
    Visually_Challenged_Right_Eye_Enucleation_Glaucoma = request.data.get("Visually_Challenged_Right_Eye_Enucleation_Glaucoma")
    Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = request.data.get("Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi")
    Visually_Challenged_Left_Eye = request.data.get("Visually_Challenged_Left_Eye")
    Visually_Challenged_Left_Eye_Enucleation = request.data.get("Visually_Challenged_Left_Eye_Enucleation")
    Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other = request.data.get("Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other")  
    Visually_Challenged_Left_Eye_Enucleation_Cataract =request.data.get("Visually_Challenged_Left_Eye_Enucleation_Cataract")
    Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = request.data.get("Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity")
    Visually_Challenged_Left_Eye_Enucleation_Glaucoma = request.data.get("Visually_Challenged_Left_Eye_Enucleation_Glaucoma")
    Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = request.data.get("Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi")


    if Visually_Challenged_Right_Eye == 'Yes':
        if Visually_Challenged_Right_Eye_Enucleation == None:
            raise Exception("You have to select Yes")
        elif Visually_Challenged_Right_Eye_Enucleation == 'Yes': 
                selected_values = request.data.get('Visually_Challenged_Right_Eye_Enucleation_Why_removed', '').split(',')
                Other_value = None
                for i in selected_values:
                    if i == "Other":
                        Other_value = Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other        
                request.data['Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other'] = Other_value
                request.data['Visually_Challenged_Right_Eye_Enucleation_No']=None
                request.data['Visually_Challenged_Right_Eye_Enucleation_Cataract']=None
                request.data ['Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity']=None
                request.data['Visually_Challenged_Right_Eye_Enucleation_Glaucoma']=None
                request.data['Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi']=None  
        elif Visually_Challenged_Right_Eye_Enucleation == 'No':   
            selected_values = request.data.get('Visually_Challenged_Right_Eye_Enucleation_No', '').split(',')
            cataract_value = None
            corneal_opacity_value = None
            glaucoma_value = None
            phthisis_bulbi_value = None
            for i in selected_values:
                if i == "Cataract":
                    cataract_value = Visually_Challenged_Right_Eye_Enucleation_Cataract
                elif i == "Corneal opacity":
                    corneal_opacity_value = Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity
                elif i == "Glaucoma":
                    glaucoma_value = Visually_Challenged_Right_Eye_Enucleation_Glaucoma
                elif i == "Phthisis bulbi":
                    phthisis_bulbi_value = Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi

            request.data['Visually_Challenged_Right_Eye_Enucleation_Cataract'] = cataract_value
            request.data['Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity'] = corneal_opacity_value
            request.data['Visually_Challenged_Right_Eye_Enucleation_Glaucoma'] = glaucoma_value
            request.data['Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi'] = phthisis_bulbi_value
            request.data['Visually_Challenged_Right_Eye_Enucleation_When_removed'] = None
            request.data['Visually_Challenged_Right_Eye_Enucleation_Why_removed'] = None
            request.data['VC_Right_Eye_Enucleation_Artificial_Eye_Used'] = None  
            request.data['Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other'] = None  
                         
          
    else:
        request.data['Visually_Challenged_Right_Eye_Enucleation'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_When_removed'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Why_removed'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other'] = None
        request.data['VC_Right_Eye_Enucleation_Artificial_Eye_Used'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_No'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Cataract'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Glaucoma'] = None
        request.data['Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi'] = None
    
    if Visually_Challenged_Left_Eye == 'Yes':
        if Visually_Challenged_Left_Eye_Enucleation is None:
            raise Exception("You have to select Yes")
        elif Visually_Challenged_Left_Eye_Enucleation == 'Yes':
            selected_values = request.data.get('Visually_Challenged_Left_Eye_Enucleation_Why_removed', '').split(',')
            Other_value = None
            for i in selected_values:
                if i == "Other":
                    Other_value = Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other        
            request.data['Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other'] = Other_value
            request.data['Visually_Challenged_Left_Eye_Enucleation_No'] = None
            request.data['Visually_Challenged_Left_Eye_Enucleation_Cataract'] = None
            request.data['Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity'] = None
            request.data['Visually_Challenged_Left_Eye_Enucleation_Glaucoma'] = None
            request.data['Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi'] = None

        elif Visually_Challenged_Left_Eye_Enucleation == 'No':   
            selected_values = request.data.get('Visually_Challenged_Left_Eye_Enucleation_No', '').split(',')
            
            cataract_value = None
            corneal_opacity_value = None
            glaucoma_value = None
            phthisis_bulbi_value = None

            for i in selected_values:
                if i == "Cataract":
                    cataract_value = Visually_Challenged_Left_Eye_Enucleation_Cataract
                elif i == "Corneal opacity":
                    corneal_opacity_value = Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity
                elif i == "Glaucoma":
                    glaucoma_value = Visually_Challenged_Left_Eye_Enucleation_Glaucoma
                elif i == "Phthisis bulbi":
                    phthisis_bulbi_value = Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi

            request.data['Visually_Challenged_Left_Eye_Enucleation_Cataract'] = cataract_value
            request.data['Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity'] = corneal_opacity_value
            request.data['Visually_Challenged_Left_Eye_Enucleation_Glaucoma'] = glaucoma_value
            request.data['Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi'] = phthisis_bulbi_value
            
            request.data['Visually_Challenged_Left_Eye_Enucleation_When_removed']=None
            request.data['Visually_Challenged_Left_Eye_Enucleation_Why_removed']=None
            request.data['VC_Left_Eye_Enucleation_Artificial_Eye_Used']=None   
            request.data['Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other'] = None       
        
    else:
        request.data['Visually_Challenged_Left_Eye_Enucleation'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_When_removed'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Why_removed'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other'] = None
        request.data['VC_Left_Eye_Enucleation_Artificial_Eye_Used'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_No'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Cataract'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Glaucoma'] = None
        request.data['Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi'] = None

def check_Visual_Acuity_Color_Blindness(request):
    Visual_Acuity_Color_Blindness = request.data.get('Visual_Acuity_Color_Blindness')
    Visual_Acuity_Color_Blindness_Yes = request.data.get('Visual_Acuity_Color_Blindness_Yes') 
    
    if Visual_Acuity_Color_Blindness == 'Yes':
            if Visual_Acuity_Color_Blindness_Yes == None:
                    raise Exception("You have to select atleast one field")
    else:
        request.data['Visual_Acuity_Color_Blindness_Yes'] = None

