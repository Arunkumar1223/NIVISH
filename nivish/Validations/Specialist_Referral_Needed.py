def check_SRN(request):
    Specialist_Referral_Needed = request.data.get('Specialist_Referral_Needed')
    Specialist_Referral_Needed_Type = request.data.get('Specialist_Referral_Needed_Type')
    Specialist_Referral_Needed_Flag = request.data.get('Specialist_Referral_Needed_Flag')
    Other = request.data.get('Other')

    if Specialist_Referral_Needed == 'Yes':
        if Specialist_Referral_Needed_Type == None or Specialist_Referral_Needed_Flag ==  None:
            raise Exception("You have to select Type and flag")      
        selected_values = request.data.get('Specialist_Referral_Needed_Type', '').split(',')  
        Other_value = None
        for i in selected_values:
            if i == "Other":
                Other_value = Other
        request.data['Other'] = Other_value
        
                
    else:
        request.data['Specialist_Referral_Needed_Type'] = None
        request.data['Specialist_Referral_Needed_Flag'] = None
        request.data['Other'] = None


