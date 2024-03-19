import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Create the school_dim and location_dim DataFrame etc...
    school_dim = df[['Short_Name', 'Long_Name', 'School_Type', 'Primary_Category', 'Fax', 'CPS_School_Profile', 'Website']].copy()
    school_dim['School_ID'] = df['School_ID'].values

    location_dim = df[['longitude', 'latitude', 'Address', 'City', 'State', 'Zip']].copy()
    location_dim['School_ID'] = df['School_ID'].values

    awards_recognition_dim = df[['Blue_Ribbon_Award_Year', 
                                'Excelerate_Award_Gold_Year', 
                                'Spot_Light_Award_Year', 
                                'Improvement_Award_Year', 
                                'Excellence_Award_Year',
                                'Supportive_School_Award',
                                'Supportive_School_Award_Desc',
                                'Progress_Report_Year']].copy()
    awards_recognition_dim['School_ID'] = df['School_ID'].values

    culture_climate_dim = df[['Culture_Climate_Rating', 'Culture_Climate_Description']].copy()
    culture_climate_dim['School_ID'] = df['School_ID'].values

    school_survey_dim = df[['School_Survey_Rating_Description', 
                            'School_Survey_Student_Response_Rate_Pct', 
                            'School_Survey_Student_Response_Rate_Avg_Pct', 
                            'School_Survey_Teacher_Response_Rate_Pct',
                            'School_Survey_Teacher_Response_Rate_Avg_Pct', 
                            'School_Survey_Parent_Response_Rate_Pct',
                            'School_Survey_Parent_Response_Rate_Avg_Pct',
                            'School_Survey_Involved_Families',
                            'School_Survey_Supportive_Environment',
                            'School_Survey_Ambitious_Instruction',
                            'School_Survey_Effective_Leaders',
                            'School_Survey_Collaborative_Teachers', 
                            'School_Survey_Safety',
                            'Parent_Survey_Results_Year']].copy()
    school_survey_dim['School_ID'] = df['School_ID'].values

    attendance_dim = df[['Student_Attendance_Year_1_Pct', 
                        'Student_Attendance_Year_2_Pct', 
                        'Student_Attendance_Avg_Pct',
                        'Teacher_Attendance_Year_1_Pct',
                        'Teacher_Attendance_Year_2_Pct',
                        'Teacher_Attendance_Avg_Pct']].copy()
    attendance_dim['School_ID'] = df['School_ID'].values

    creative_school_certification_dim = df[['Creative_School_Certification', 'Creative_School_Certification_Description']].copy()
    creative_school_certification_dim['School_ID'] = df['School_ID'].values

    healthy_school_certification_dim = df[['Healthy_School_Certification', 'Healthy_School_Certification_Description']].copy()
    healthy_school_certification_dim['School_ID'] = df['School_ID'].values

    attainment_all_grades_school_lbl_dim = df[['Attainment_All_Grades_School_Pct', 'Attainment_All_Grades_School_Lbl']].copy()
    attainment_all_grades_school_lbl_dim['School_ID'] = df['School_ID'].values

    student_attainment_dim = df[['Student_Attainment_Rating', 'Student_Attainment_Description', 'Attainment_Reading_Pct_ES',
                                'Attainment_Reading_Lbl_ES', 'Attainment_Math_Pct_ES', 'Attainment_Math_Lbl_ES']].copy()
    student_attainment_dim['School_ID'] = df['School_ID'].values
    

    attainment_all_grades_school_lbl_dim = df[['Attainment_All_Grades_School_Pct', 'Attainment_All_Grades_School_Lbl']].copy()
    attainment_all_grades_school_lbl_dim['School_ID'] = df['School_ID'].values
    attainment_all_grades_school_lbl_dim

    suspension_and_discipline_dim = df[['Suspensions_Per_100_Students_Year_1_Pct', 'Suspensions_Per_100_Students_Year_2_Pct',
                                        'Suspensions_Per_100_Students_Avg_Pct', 'Misconducts_To_Suspensions_Year_1_Pct', 'Misconducts_To_Suspensions_Year_2_Pct',
                                        'Misconducts_To_Suspensions_Avg_Pct', 'Average_Length_Suspension_Year_1_Pct', 'Average_Length_Suspension_Year_2_Pct',
                                        'Average_Length_Suspension_Avg_Pct', 'Behavior_Discipline_Year_1', 'Behavior_Discipline_Year_2' ]].copy()
    suspension_and_discipline_dim['School_ID'] = df['School_ID'].values
    

    attainment_psat_grade_9_school_dim = df[['Attainment_PSAT_Grade_9_School_Pct', 'Attainment_PSAT_Grade_9_School_Lbl']].copy()
    attainment_psat_grade_9_school_dim['School_ID'] = df['School_ID'].values

    attainment_psat_grade_10_school_dim = df[['Attainment_PSAT_Grade_10_School_Pct', 'Attainment_PSAT_Grade_10_School_Lbl']].copy()
    attainment_psat_grade_10_school_dim['School_ID'] = df['School_ID'].values

    attainment_sat_grade_11_school_dim = df[['Attainment_SAT_Grade_11_School_Pct', 'Attainment_SAT_Grade_11_School_Lbl']].copy()
    attainment_sat_grade_11_school_dim['School_ID'] = df['School_ID'].values

    graduation_4_year_school_dim = df[['Graduation_4_Year_School_Pct_Year_2', 'Graduation_4_Year_CPS_Pct_Year_2', 'Graduation_4_Year_School_Pct_Year_1',
                                    'Graduation_4_Year_CPS_Pct_Year_1']].copy()
    graduation_4_year_school_dim['School_ID'] = df['School_ID'].values

    graduation_5_year_school_dim = df[['Graduation_5_Year_School_Pct_Year_2', 'Graduation_5_Year_CPS_Pct_Year_2', 'Graduation_5_Year_School_Pct_Year_1',
                                    'Graduation_5_Year_CPS_Pct_Year_1']].copy()
    graduation_5_year_school_dim['School_ID'] = df['School_ID'].values

    sat_grade_11_dim = df[['SAT_Grade_11_Score_School_Avg', 'SAT_Grade_11_Score_CPS_Avg']].copy()
    sat_grade_11_dim['School_ID'] = df['School_ID'].values

    college_enrollment_dim = df[['College_Enrollment_School_Pct_Year_2', 'College_Enrollment_CPS_Pct_Year_2',
                                'College_Enrollment_School_Pct_Year_1', 'College_Enrollment_CPS_Pct_Year_1',
                                'College_Persistence_School_Pct_Year_2', 'College_Persistence_CPS_Pct_Year_2',
                                'College_Persistence_School_Pct_Year_1', 'College_Persistence_CPS_Pct_Year_1', 'Progress_Toward_Graduation_Year_1',
                                'Progress_Toward_Graduation_Year_2']].copy()
    college_enrollment_dim['School_ID'] = df['School_ID'].values

    freshmen_on_track_school_dim = df[['Freshmen_On_Track_School_Pct_Year_2', 'Freshmen_On_Track_CPS_Pct_Year_2',
                                    'Freshmen_On_Track_School_Pct_Year_1', 'Freshmen_On_Track_CPS_Pct_Year_1']].copy()
    freshmen_on_track_school_dim['School_ID'] = df['School_ID'].values

    dropout_dim = df[['One_Year_Dropout_Rate_Year_1_Pct', 'One_Year_Dropout_Rate_Year_2_Pct', 'One_Year_Dropout_Rate_Avg_Pct']].copy()
    dropout_dim['School_ID'] = df['School_ID'].values

    # create the fact table

    school_fact_table = df.merge(school_dim, on='School_ID', how='left')\
                        .merge(location_dim, on='School_ID', how='left')\
                        .merge(awards_recognition_dim, on='School_ID', how='left')\
                        .merge(culture_climate_dim, on='School_ID', how='left')\
                        .merge(school_survey_dim, on='School_ID', how='left')\
                        .merge(attendance_dim, on='School_ID', how='left')\
                        .merge(creative_school_certification_dim, on='School_ID', how='left')\
                        .merge(healthy_school_certification_dim, on='School_ID', how='left')\
                        .merge(attainment_all_grades_school_lbl_dim, on='School_ID', how='left')\
                        .merge(student_attainment_dim, on='School_ID', how='left')\
                        .merge(suspension_and_discipline_dim, on='School_ID', how='left')\
                        .merge(attainment_psat_grade_9_school_dim, on='School_ID', how='left')\
                        .merge(attainment_psat_grade_10_school_dim, on='School_ID', how='left')\
                        .merge(attainment_sat_grade_11_school_dim, on='School_ID', how='left')\
                        .merge(graduation_4_year_school_dim, on='School_ID', how='left')\
                        .merge(graduation_5_year_school_dim, on='School_ID', how='left')\
                        .merge(sat_grade_11_dim, on='School_ID', how='left')\
                        .merge(college_enrollment_dim, on='School_ID', how='left')\
                        .merge(freshmen_on_track_school_dim, on='School_ID', how='left')\
                        .merge(dropout_dim, on='School_ID', how='left')\
                        [['School_ID', 'State_School_Report_Card_URL', 'Mobility_Rate_Pct', 'Chronic_Truancy_Pct',
                        'Other_Metrics_Year_1', 'Other_Metrics_Year_2']].copy()
                        
    return {'school_dim': school_dim.to_dict(orient='dict'),
    'location_dim': location_dim.to_dict(orient='dict'),
    'awards_recognition_dim': awards_recognition_dim.to_dict(orient='dict'),
    'culture_climate_dim': culture_climate_dim.to_dict(orient='dict'),
    'school_survey_dim': school_survey_dim.to_dict(orient='dict'),
    'attendance_dim': attendance_dim.to_dict(orient='dict'),
    'creative_school_certification_dim': creative_school_certification_dim.to_dict(orient='dict'),
    'healthy_school_certification_dim': healthy_school_certification_dim.to_dict(orient='dict'),
    'attainment_all_grades_school_lbl_dim': attainment_all_grades_school_lbl_dim.to_dict(orient='dict'),
    'suspension_and_discipline_dim': suspension_and_discipline_dim.to_dict(orient='dict'),
    'attainment_psat_grade_9_school_dim': attainment_psat_grade_9_school_dim.to_dict(orient='dict'),
    'attainment_psat_grade_10_school_dim': attainment_psat_grade_10_school_dim.to_dict(orient='dict'),
    'attainment_sat_grade_11_school_dim': attainment_sat_grade_11_school_dim.to_dict(orient='dict'),
    'graduation_4_year_school_dim': graduation_4_year_school_dim.to_dict(orient='dict'),
    'graduation_5_year_school_dim': graduation_5_year_school_dim.to_dict(orient='dict'),
    'sat_grade_11_dim': sat_grade_11_dim.to_dict(orient='dict'),
    'college_enrollment_dim': college_enrollment_dim.to_dict(orient='dict'),
    'freshmen_on_track_school_dim': freshmen_on_track_school_dim.to_dict(orient='dict'),
    'dropout_dim': dropout_dim.to_dict(orient='dict'),
    'school_fact_table': school_fact_table.to_dict(orient='dict')}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
