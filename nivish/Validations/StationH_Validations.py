def check_SRNDental(request):
    StationH_Dental_SR_Needed = request.data.get('StationH_Dental_SR_Needed')
    StationH_Dental_SR_Needed_Yes_Type = request.data.get('StationH_Dental_SR_Needed_Yes_Type')
    StationH_Dental_SR_Needed_Yes_Flag = request.data.get('StationH_Dental_SR_Needed_Yes_Flag')
    if StationH_Dental_SR_Needed == 'Yes':
        if StationH_Dental_SR_Needed_Yes_Type == None and StationH_Dental_SR_Needed_Yes_Flag ==  None:
            raise Exception("You have to select Type and flag")              
    else:
        request.data['StationH_Dental_SR_Needed_Yes_Type'] = None
        request.data['StationH_Dental_SR_Needed_Yes_Flag'] = None



def check_Upper_Permanent(request):
    Upper_Permanent = request.data.get("Upper_Permanent")

    # Check if Upper_Permanent is null
    if Upper_Permanent is None:
        request.data['Upper_Permanent_Decayed'] = None
        request.data['Upper_Permanent_Missing'] = None
        request.data['Upper_Permanent_Filled'] = None
        request.data['Upper_Permanent_Prosthesis'] = None
        request.data['Upper_Permanent_Restoration_done'] = None
    else:
        Upper_Permanent_Decayed = request.data.get("Upper_Permanent_Decayed")
        Upper_Permanent_Missing = request.data.get("Upper_Permanent_Missing")
        Upper_Permanent_Filled = request.data.get("Upper_Permanent_Filled")
        Upper_Permanent_Prosthesis = request.data.get("Upper_Permanent_Prosthesis")
        Upper_Permanent_Restoration_done = request.data.get("Upper_Permanent_Restoration_done")

        selected_values = Upper_Permanent.split(',')
        Decayed_value = None
        Missing_opacity_value = None
        Filled_value = None
        Prosthesis_value = None
        Restorationdone_value = None

        for i in selected_values:
            if i == "Decayed":
                Decayed_value = Upper_Permanent_Decayed
            elif i == "Missing":
                Missing_opacity_value = Upper_Permanent_Missing
            elif i == "Filled":
                Filled_value = Upper_Permanent_Filled
            elif i == "Prosthesis":
                Prosthesis_value = Upper_Permanent_Prosthesis
            elif i == "Restoration done":
                Restorationdone_value = Upper_Permanent_Restoration_done

        request.data['Upper_Permanent_Decayed'] = Decayed_value
        request.data['Upper_Permanent_Missing'] = Missing_opacity_value
        request.data['Upper_Permanent_Filled'] = Filled_value
        request.data['Upper_Permanent_Prosthesis'] = Prosthesis_value
        request.data['Upper_Permanent_Restoration_done'] = Restorationdone_value
    
def check_Upper_Deciduous(request):
    Upper_Deciduous = request.data.get("Upper_Deciduous")

    # Check if Upper_Deciduous is null
    if Upper_Deciduous is None:
        request.data['Upper_Deciduous_Decayed'] = None
        request.data['Upper_Deciduous_Missing'] = None
        request.data['Upper_Deciduous_Filled'] = None
        request.data['Upper_Deciduous_Prosthesis'] = None
        request.data['Upper_Deciduous_Restoration_done'] = None
    else:
        Upper_Deciduous_Decayed = request.data.get("Upper_Deciduous_Decayed")
        Upper_Deciduous_Missing = request.data.get("Upper_Deciduous_Missing")
        Upper_Deciduous_Filled = request.data.get("Upper_Deciduous_Filled")
        Upper_Deciduous_Prosthesis = request.data.get("Upper_Deciduous_Prosthesis")
        Upper_Deciduous_Restoration_done = request.data.get("Upper_Deciduous_Restoration_done")

        selected_values = Upper_Deciduous.split(',')
        Decayed_value = None
        Missing_opacity_value = None
        Filled_value = None
        Prosthesis_value = None
        Restorationdone_value = None

        for i in selected_values:
            if i == "Decayed":
                Decayed_value = Upper_Deciduous_Decayed
            elif i == "Missing":
                Missing_opacity_value = Upper_Deciduous_Missing
            elif i == "Filled":
                Filled_value = Upper_Deciduous_Filled
            elif i == "Prosthesis":
                Prosthesis_value = Upper_Deciduous_Prosthesis
            elif i == "Restoration done":
                Restorationdone_value = Upper_Deciduous_Restoration_done

        request.data['Upper_Deciduous_Decayed'] = Decayed_value
        request.data['Upper_Deciduous_Missing'] = Missing_opacity_value
        request.data['Upper_Deciduous_Filled'] = Filled_value
        request.data['Upper_Deciduous_Prosthesis'] = Prosthesis_value
        request.data['Upper_Deciduous_Restoration_done'] = Restorationdone_value

def check_Lower_Deciduous(request):
    Lower_Deciduous = request.data.get("Lower_Deciduous")

    # Check if Lower_Deciduous is null
    if Lower_Deciduous is None:
        request.data['Lower_Deciduous_Decayed'] = None
        request.data['Lower_Deciduous_Missing'] = None
        request.data['Lower_Deciduous_Filled'] = None
        request.data['Lower_Deciduous_Prosthesis'] = None
        request.data['Lower_Deciduous_Restoration_done'] = None
    else:
        Lower_Deciduous_Decayed = request.data.get("Lower_Deciduous_Decayed")
        Lower_Deciduous_Missing = request.data.get("Lower_Deciduous_Missing")
        Lower_Deciduous_Filled = request.data.get("Lower_Deciduous_Filled")
        Lower_Deciduous_Prosthesis = request.data.get("Lower_Deciduous_Prosthesis")
        Lower_Deciduous_Restoration_done = request.data.get("Lower_Deciduous_Restoration_done")

        selected_values = Lower_Deciduous.split(',')
        Decayed_value = None
        Missing_opacity_value = None
        Filled_value = None
        Prosthesis_value = None
        Restorationdone_value = None

        for i in selected_values:
            if i == "Decayed":
                Decayed_value = Lower_Deciduous_Decayed
            elif i == "Missing":
                Missing_opacity_value = Lower_Deciduous_Missing
            elif i == "Filled":
                Filled_value = Lower_Deciduous_Filled
            elif i == "Prosthesis":
                Prosthesis_value = Lower_Deciduous_Prosthesis
            elif i == "Restoration done":
                Restorationdone_value = Lower_Deciduous_Restoration_done

        request.data['Lower_Deciduous_Decayed'] = Decayed_value
        request.data['Lower_Deciduous_Missing'] = Missing_opacity_value
        request.data['Lower_Deciduous_Filled'] = Filled_value
        request.data['Lower_Deciduous_Prosthesis'] = Prosthesis_value
        request.data['Lower_Deciduous_Restoration_done'] = Restorationdone_value

def check_Lower_Permanent(request):
    Lower_Permanent = request.data.get("Lower_Permanent")

    # Check if Lower_Permanent is null
    if Lower_Permanent is None:
        request.data['Lower_Permanent_Decayed'] = None
        request.data['Lower_Permanent_Missing'] = None
        request.data['Lower_Permanent_Filled'] = None
        request.data['Lower_Permanent_Prosthesis'] = None
        request.data['Lower_Permanent_Restoration_done'] = None
    else:
        Lower_Permanent_Decayed = request.data.get("Lower_Permanent_Decayed")
        Lower_Permanent_Missing = request.data.get("Lower_Permanent_Missing")
        Lower_Permanent_Filled = request.data.get("Lower_Permanent_Filled")
        Lower_Permanent_Prosthesis = request.data.get("Lower_Permanent_Prosthesis")
        Lower_Permanent_Restoration_done = request.data.get("Lower_Permanent_Restoration_done")

        selected_values = Lower_Permanent.split(',')
        Decayed_value = None
        Missing_opacity_value = None
        Filled_value = None
        Prosthesis_value = None
        Restorationdone_value = None

        for i in selected_values:
            if i == "Decayed":
                Decayed_value = Lower_Permanent_Decayed
            elif i == "Missing":
                Missing_opacity_value = Lower_Permanent_Missing
            elif i == "Filled":
                Filled_value = Lower_Permanent_Filled
            elif i == "Prosthesis":
                Prosthesis_value = Lower_Permanent_Prosthesis
            elif i == "Restoration done":
                Restorationdone_value = Lower_Permanent_Restoration_done

        request.data['Lower_Permanent_Decayed'] = Decayed_value
        request.data['Lower_Permanent_Missing'] = Missing_opacity_value
        request.data['Lower_Permanent_Filled'] = Filled_value
        request.data['Lower_Permanent_Prosthesis'] = Prosthesis_value
        request.data['Lower_Permanent_Restoration_done'] = Restorationdone_value



    
def check_Braces(request):
    Braces = request.data.get("Braces")
    Braces_Yes = request.data.get("Braces_Yes")   

    if Braces is None:
        request.data['Braces_Yes'] = None
    elif Braces == 'Yes':
            if Braces_Yes == None:                  
                    raise Exception("You have to select atleast one field")             
    else:
        request.data['Braces_Yes'] = None
        
def check_Bridges(request):
    Bridges = request.data.get("Bridges")
    Bridges_Yes = request.data.get("Bridges_Yes")

    if Bridges is None:
        request.data['Bridges_Yes'] = None
    elif Bridges == 'Yes':
         if Bridges_Yes == None:
              raise Exception("You have to select atleast one field")       
    else:
         request.data['Bridges_Yes'] = None

def check_Dentures(request):
    Dentures = request.data.get("Dentures")
    Dentures_Yes = request.data.get("Dentures_Yes")

    if Dentures is None:
        request.data['Dentures_Yes'] = None
    elif Dentures == 'Yes':
          if Dentures_Yes == None:
               raise Exception("You have to select atleast one field")        
    else:
          request.data['Dentures_Yes'] = None


def check_Soft_Tissue_Pathology(request):
     Soft_Tissue_Pathology = request.data.get("Soft_Tissue_Pathology")
     Soft_Tissue_Pathology_Yes = request.data.get("Soft_Tissue_Pathology_Yes")
     Soft_Tissue_Pathology_Yes_Other = request.data.get("Soft_Tissue_Pathology_Yes_Other")
     if Soft_Tissue_Pathology == 'Yes':        
          if Soft_Tissue_Pathology_Yes == None:
               raise Exception("You have to select atleast one field")                  
          selected_values = request.data.get('Soft_Tissue_Pathology_Yes', '').split(',')
          Others_value = None
          for i in selected_values:
            if i == "Other":
                Others_value = Soft_Tissue_Pathology_Yes_Other
            request.data['Soft_Tissue_Pathology_Yes_Other'] = Others_value  
     else:
          request.data['Soft_Tissue_Pathology_Yes'] = None
          request.data['Soft_Tissue_Pathology_Yes_Other'] = None

def check_Treatment_Needed(request):
     Treatment_Needed = request.data.get("Treatment_Needed")
     Treatment_Needed_Yes = request.data.get("Treatment_Needed_Yes")
     Treatment_Needed_Yes_Other = request.data.get("Treatment_Needed_Yes_Other")
     if Treatment_Needed == 'Yes':
          if Treatment_Needed_Yes is None:
               raise Exception("You have to select to Yes")
          selected_values = request.data.get('Treatment_Needed_Yes', '').split(',')
          Others_value = None
          for i in selected_values:
            if i == "Other":
                Others_value = Treatment_Needed_Yes_Other
            request.data['Treatment_Needed_Yes_Other'] = Others_value          
     else:
          request.data['Treatment_Needed_Yes'] = None
          request.data['Treatment_Needed_Yes_Other'] = None
