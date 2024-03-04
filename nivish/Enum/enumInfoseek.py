"""
Module containing enum-like structures for student information.
"""

Basic_Information_ENUM = (
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Guardian', 'Guardian'),
    ('Other', 'Other'),
)

Gender_ENUM = (
    ('Female', 'Female'),
    ('Male', 'Male'),
)

BloodGroup_ENUM = (
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O'),
    ('Not Known', 'Not Known'),
)

Rh_Factor_ENUM = (
    ('Rh Positive', 'Rh Positive'),
    ('Rh Negative', 'Rh Negative'),
    ('Not Known', 'Not Known'),
)

Ethnicity_ENUM = (
    ('Asian/Indian', 'Asian/Indian'),
    ('Black African', 'Black African'),
    ('Arabs', 'Arabs'),
    ('Other', 'Other'),
)

Basic_Lifestyle_ENUM = (
    ('Outdoor', 'Outdoor'),
    ('Indoor', 'Indoor'),
    ('Both', 'Both'),
    ('Neither', 'Neither'),
)

Type_of_meal_ENUM = (
    ('Vegetarian', 'Vegetarian'),
    ('Non Vegetarian', 'Non Vegetarian'),
    ('Vegetarian with Eggs', 'Vegetarian with Eggs'),
    ('Vegetarian with Fish', 'Vegetarian with Fish'),
    ('Vegan', 'Vegan'),
    ('Organic', 'Organic'),
    ('Other', 'Other'),
)

StudentMeal_If_Yes_ENUM = (
    ('Home', 'Home'),
    ('School', 'School'),
    ('Stalls/Hawkers', 'Stalls/Hawkers'),
    ('Tuck Shop', 'Tuck Shop'),
    ('Other', 'Other'),
)

Students_average_sleep_ENUM = (
    ('Less than 8 hours', 'Less than 8 hours'),
    ('More than 8 hours', 'More than 8 hours'),
)

Social_personality_student_ENUM = (
    ('Aggressive', 'Aggressive'),
    ('Attention Seeking', 'Attention Seeking'),
    ('Calm', 'Calm'),
    ('Gregarious/Outgoing', 'Gregarious/Outgoing'),
    ('Happy', 'Happy'),
    ('Nervous', 'Nervous'),
    ('Sad/Morose', 'Sad/Morose'),
    ('Sulky/Cranky', 'Sulky/Cranky'),
    ('Withdrawn', 'Withdrawn'),
    ('Other', 'Other'),
)

Students_self_image_ENUM = (
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Average', 'Average'),
    ('Poor', 'Poor'),
)

Student_reactions_change_ENUM = (
    ('Adjusting', 'Adjusting'),
    ('Cheerful', 'Cheerful'),
    ('Fearful', 'Fearful'),
    ('Nervous', 'Nervous'),
    ('Non-Adjusting', 'Non-Adjusting'),
    ('Resistant', 'Resistant'),
    ('Obstructive', 'Obstructive'),
    ('Nothing specific', 'Nothing specific'),
    ('Other', 'Other'),
)

Student_reaction_change_others_ENUM = (
    ('Aggressive', 'Aggressive'),
    ('Dependent', 'Dependent'),
    ('Dominating', 'Dominating'),
    ('Friendly', 'Friendly'),
    ('Submissive', 'Submissive'),
    ('Clingy', 'Clingy'),
    ('Nothing specific', 'Nothing specific'),
    ('Other', 'Other'),
)

Student_general_opinion_ENUM = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
    ('Neutral', 'Neutral'),
)

Belongs_To_ENUM = (
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Guardian', 'Guardian'),
)
