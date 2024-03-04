"""
Module containing enum-like structures for different status types.
"""

SRNYesorNo = (('No', 'No'),
              ('Yes', 'Yes'),)

Referral_Needed_Flag = (('Non-Urgent', 'Non-Urgent'),
                        ('Urgent', 'Urgent'),
                        ('Emergency', 'Emergency'),)

NormalandAbnormal = (('Normal', 'Normal'),
                     ('Abnormal', 'Abnormal'),)

AbsentandPresent = (('Absent', 'Absent'),
                    ('Present', 'Present'),)

Review_Status_Enum = (('Not Reviewed', 'Not Reviewed'),
                      ('Review Completed', 'Review Completed'),
                      ('On Hold', 'On Hold'),)
