

StationGYorN = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Partially', 'Partially')
)

CNS_Speech_Abnormal_ENUM = (
    ('Lisping', 'Lisping'),
    ('Stammering', 'Stammering'),
    ('Other', 'Other')
)


CNS_History_of_Headache_yes_Frequency_ENUM = (
    ('Sporadic', 'Sporadic'),
    ('Continuous', 'Continuous')
   
)




CNS_History_of_Headache_yes_Frequency_Continuous_ENUM =  (

    ('Since 1 week', 'Since 1 week'),
    ('Since 1 Month', 'Since 1 Month'),
    ('Since 3 Month', 'Since 3 Month'),
    ('Since 6 Month', 'Since 6 Month'),
    ('Since 1 Year', 'Since 1 Year'),
    ('More than 1 Year', 'More than 1 Year'),
)


# CNS_History_of_Headache_yes_Associated_With_Others_ENUM =  (
#     ('Waking up with headache', 'Waking up with headache'),
#     ('Morning', 'Morning'),
#     ('Afternoon', 'Afternoon'),
#     ('Evening', 'Evening'),
#     ('Night', 'Night'),
# )


CNS_History_of_Headache_yes_From_ENUM = (
     ('< 1 Month', '< 1 Month'),
    ('< 1 Year', '< 1 Year'),
    ('> 1 Year', '> 1 Year'),
    ('> 2 Year', '> 2 Year'),
    ('> 5 Year', '> 5 Year'),
)



CNS_History_of_Headache_yes_Duration_ENUM =  (
    ('Less than 1 hour', 'Less than 1 hour'),
    ('1 to 3 hours', '1 to 3 hours'),
    ('1 day', '1 day'),
    ('2 to 3 days', '2 to 3 days'),
    ('More than 3 days', 'More than 3 days'),
)




CNS_History_of_Dizziness_yes_Frequency_ENUM = (
    ('Sporadic', 'Sporadic'),
    ('Continuous', 'Continuous')
   
)


CNS_History_of_Dizziness_yes_Frequency_Continuous_ENUM =  (

    ('Since 1 week', 'Since 1 week'),
    ('Since 1 Month', 'Since 1 Month'),
    ('Since 3 Month', 'Since 3 Month'),
    ('Since 6 Month', 'Since 6 Month'),
    ('Since 1 Year', 'Since 1 Year'),
    ('More than 1 Year', 'More than 1 Year'),
)







# CNS_History_of_Dizziness_yes_Associated_With_Part_of_day_ENUM =  (

#     ('Waking up with headache', 'Waking up with headache'),
#     ('Morning', 'Morning'),
#     ('Afternoon', 'Afternoon'),
#     ('Evening', 'Evening'),
#     ('Night', 'Night'),
# )




RS_Shape_of_Chest_Abnormal_ENUM =  (

    ('Concave', 'Concave'),
    ('Pigeon', 'Pigeon'),
    ('Barrel', 'Barrel'),
    ('Retracted intercostal spaces', 'Retracted intercostal spaces'),
    ('Other', 'Other'),

)

RS_Type_of_Respiration_ENUM =  (

    ('Abdominal', 'Abdominal'),
    ('Thoracic', 'Thoracic'),
    ('Abdomino-Thoracic', 'Abdomino-Thoracic'),
    
    )


RS_Type_of_Respiration_Label_ENUM =  (

    ('Indrawing of intercostal spaces', 'Indrawing of intercostal spaces'),
    ('Indrawing of chest', 'Indrawing of chest'),
    ('Other', 'Other'),
    
)



RS_Trachea_ENUM =  (

    ('Central', 'Central'),
    ('Displaced to Left', 'Displaced to Left'),
    ('Displaced to Right', 'Displaced to Right'),
    
)

RS_Evidence_of_Tracheostomy_ENUM =  (

    ('Absent', 'Absent'),
    ('Tracheostomy opening', 'Tracheostomy opening'),
    ('Tracheostomy scar', 'Tracheostomy scar'),
    
)




RBE_ENUM = (
    ('Reduced', 'Reduced'),
    ('Absent', 'Absent'),
    ('Exaggerated', 'Exaggerated'),
)

Tenderness_ENUM = (
    ('Absent', 'Absent'),
    ('Present', 'Present'),
    ('Present Rebound', 'Present Rebound'),
)


Crepts_ENUM = (
    ('Absent', 'Absent'),
    ('Present', 'Present'),
    ('Exaggerated', 'Exaggerated'),
)

FC_ENUM = (
    ('Fine', 'Fine'),
    ('Coarse', 'Coarse'),
)



WD_ENUM = (
    ('Wet', 'Wet'),
    ('Dry', 'Dry'),
)

OTW_ENUM = (
    ('1+', '1+'),
    ('2+', '2+'),
    ('3+', '3+'),
    )


CVS_Jugular_Pulsations_ENUM = (
    ('Not visible', 'Not visible'),
    ('Visible', 'Visible'),
    )




CVS_Apex_Beat_ENUM = (
    ('Normal', 'Normal'),
    ('Displaced', 'Displaced'),
   
    )



AUS_Cleft_Lip_Present_ENUM = (
    ('Repaired', 'Repaired'),
    ('Unrepaired', 'Unrepaired'),
   
    )

MDS_ENUM = (

    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe'),
)


SFH_ENUM = (

    ('Soft', 'Soft'),
    ('Firm', 'Firm'),
    ('Hard', 'Hard'),
)



NP_ENUM = (

    ('Not Palpable', 'Not Palpable'),
    ('Palpable', 'Palpable'),
)





AUS_LH_Liver_Palpable_ENUM = (

    ('1F', '1F'),
    ('2F', '2F'),
    ('3F', '3F'),
    ('Greater than 3F', 'Greater than 3F'),
)

NT_ENUM = (

     ('Not Tender', 'Not Tender'),
    ('Tender', 'Tender'),
)


AUS_Urinary_Bladder_Palpable_ENUM = (

    ('1F', '1F'),
    ('2F', '2F'),
    ('3F', '3F'),
)



ML_ENUM = (

    ('More', 'More'),
    ('Less', 'Less'),
)



IN_ENUM = (

    ('Indicated', 'Indicated'),
    ('Not Indicated', 'Not Indicated'),
)


Score_ENUM = (

    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


G_ENUM = (

    ('Girls', 'Girls'),
    ('Boys', 'Boys'),
    ('Both', 'Both'),
    ('Neither', 'Neither'),
)


# PAG_MA_Yes_Age_of_Menarche_ENUM = (

#     ('0', '0'),
#     ('1', '1'),
#     ('2', '2'),
#     ('3', '3'),
#     ('4', '4'),
#     ('5', '5'),
#     ('6', '6'),
#     ('7', '7'),

# )



PAG_MA_Yes_Character_Regularity_ENUM = (

    ('Regular', 'Regular'),
    ('Irregular', 'Irregular')
    
)

PAG_MA_Yes_Character_Frequency_in_Days_ENUM = (

    ('<16', '<16'),
    ('16-20', '16-20'),
    ('21-25', '21-25'),
    ('26-28', '26-28'),
    ('29-30', '29-30'),
    ('31-35', '31-35'),
    ('36-40', '36-40'),
    ('41-50', '41-50'),
    ('51-60', '51-60'),
    ('>60', '>60'),
    
)



PAG_MA_Yes_Duration_in_days_ENUM = (

    ('<1', '<1'),
    ('1-2', '1-2'),
    ('2-3', '2-3'),
    ('3-4', '3-4'),
    ('4-5', '4-5'),
    ('5-6', '5-6'),
    ('6-7', '6-7'),
    ('7-8', '7-8'),
    ('8-9', '8-9'),
    ('9-10', '9-10'),
    ('>10', '>10'),
    
)


PAG_MA_Yes_Flow_ENUM = (

    ('Scanty', 'Scanty'),
    ('Moderate', 'Moderate'),
    ('Heavy', 'Heavy'),
)



PAG_MA_Yes_Comfort_ENUM = (

    ('Painless', 'Painless'),
    ('Painful', 'Painful'),
    ('Mild Discomfort', 'Mild Discomfort'),
    ('Exceedingly Painful', 'Exceedingly Painful'),
    ('Moderate Discomfort', 'Moderate Discomfort'),
)

History_of_Medication_Yes_ENUM = (

    ('Less than 7 days', 'Less than 7 days'),
    ('1 month - 1 year', '1 month - 1 year'),
    ('7 days - 1 month', '7 days - 1 month'),
    ('greater than 1 year', 'greater than 1 year'),
)