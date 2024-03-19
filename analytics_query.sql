CREATE OR REPLACE TABLE chicago-public-schools-data.cps_data_project.tbl_analytics AS (
SELECT
  
f.School_ID,f.State_School_Report_Card_URL, a.Attainment_All_Grades_School_Pct, b.Attainment_PSAT_Grade_10_School_Pct, c.Attainment_PSAT_Grade_9_School_Pct,
d.Attainment_SAT_Grade_11_School_Pct, e.Student_Attendance_Avg_Pct, e.Student_Attendance_Year_1_Pct, e.Student_Attendance_Year_2_Pct,
e.Teacher_Attendance_Avg_Pct, e.Teacher_Attendance_Year_1_Pct, e.Teacher_Attendance_Year_2_Pct, g.Blue_Ribbon_Award_Year, h.College_Enrollment_CPS_Pct_Year_1,
h.College_Enrollment_CPS_Pct_Year_2, h.College_Enrollment_School_Pct_Year_1, h.College_Enrollment_School_Pct_Year_2, h.College_Persistence_CPS_Pct_Year_1, 
h.College_Persistence_CPS_Pct_Year_2, h.College_Persistence_School_Pct_Year_1, h.College_Persistence_School_Pct_Year_2, h.Progress_Toward_Graduation_Year_1, 
h.Progress_Toward_Graduation_Year_2, i.Creative_School_Certification, i.Creative_School_Certification_Description, j.Culture_Climate_Rating, k.One_Year_Dropout_Rate_Avg_Pct, 
k.One_Year_Dropout_Rate_Year_1_Pct, 
k.One_Year_Dropout_Rate_Year_2_Pct, l.Freshmen_On_Track_CPS_Pct_Year_1, l.Freshmen_On_Track_CPS_Pct_Year_2, l.Freshmen_On_Track_School_Pct_Year_1, l.Freshmen_On_Track_School_Pct_Year_2, 
m.Graduation_4_Year_CPS_Pct_Year_1, m.Graduation_4_Year_CPS_Pct_Year_2, m.Graduation_4_Year_School_Pct_Year_1, m.Graduation_4_Year_School_Pct_Year_2, n.Graduation_5_Year_CPS_Pct_Year_1,
n.Graduation_5_Year_CPS_Pct_Year_2, n.Graduation_5_Year_School_Pct_Year_1, n.Graduation_5_Year_School_Pct_Year_2, o.Healthy_School_Certification, p.Address, p.City, p.latitude ,p.longitude, 
p.State, p.Zip, q.SAT_Grade_11_Score_CPS_Avg, q.SAT_Grade_11_Score_School_Avg, r.CPS_School_Profile, r.Fax, r.Long_Name, r.Primary_Category, r.School_Type, r.Short_Name, r.Website,
s.Parent_Survey_Results_Year, s.School_Survey_Ambitious_Instruction, s.School_Survey_Collaborative_Teachers, s.School_Survey_Effective_Leaders, s.School_Survey_Involved_Families, 
s.School_Survey_Parent_Response_Rate_Avg_Pct, s.School_Survey_Parent_Response_Rate_Pct, s.School_Survey_Safety, s.School_Survey_Student_Response_Rate_Avg_Pct, 
s.School_Survey_Student_Response_Rate_Pct, s.School_Survey_Supportive_Environment, s.School_Survey_Teacher_Response_Rate_Avg_Pct, s.School_Survey_Teacher_Response_Rate_Pct, 
t.Average_Length_Suspension_Avg_Pct, t.Average_Length_Suspension_Year_1_Pct, t.Average_Length_Suspension_Year_2_Pct, t.Behavior_Discipline_Year_1, t.Behavior_Discipline_Year_2, 
t.Misconducts_To_Suspensions_Avg_Pct, t.Misconducts_To_Suspensions_Year_1_Pct, t.Misconducts_To_Suspensions_Year_2_Pct, t.Suspensions_Per_100_Students_Avg_Pct, 
t.Suspensions_Per_100_Students_Year_1_Pct, t.Suspensions_Per_100_Students_Year_2_Pct
  
From `chicago-public-schools-data.cps_data_project.school_fact_table` f
JOIN `chicago-public-schools-data.cps_data_project.attainment_all_grades_school_lbl_dim` a   
ON f.School_ID = a.School_ID
JOIN `chicago-public-schools-data.cps_data_project.attainment_psat_grade_10_school_dim` b  
ON f.School_ID = b.School_ID
JOIN `chicago-public-schools-data.cps_data_project.attainment_psat_grade_9_school_dim` c
ON f.School_ID = c.School_ID
JOIN `chicago-public-schools-data.cps_data_project.attainment_sat_grade_11_school_dim` d 
ON f.School_ID = d.School_ID
JOIN `chicago-public-schools-data.cps_data_project.attendance_dim` e
ON f.School_ID = e.School_ID
JOIN `chicago-public-schools-data.cps_data_project.awards_recognition_dim` g
ON f.School_ID = g.School_ID
JOIN `chicago-public-schools-data.cps_data_project.college_enrollment_dim` h
ON f.School_ID = h.School_ID
JOIN `chicago-public-schools-data.cps_data_project.creative_school_certification_dim` i
ON f.School_ID = i.School_ID
JOIN `chicago-public-schools-data.cps_data_project.culture_climate_dim` j
ON f.School_ID = j.School_ID
JOIN `chicago-public-schools-data.cps_data_project.dropout_dim` k
ON f.School_ID = k.School_ID
JOIN `chicago-public-schools-data.cps_data_project.freshmen_on_track_school_dim` l
ON f.School_ID = l.School_ID
JOIN `chicago-public-schools-data.cps_data_project.graduation_4_year_school_dim` m
ON f.School_ID = m.School_ID
JOIN `chicago-public-schools-data.cps_data_project.graduation_5_year_school_dim` n
ON f.School_ID = n.School_ID
JOIN `chicago-public-schools-data.cps_data_project.healthy_school_certification_dim` o
ON f.School_ID = o.School_ID
JOIN `chicago-public-schools-data.cps_data_project.location_dim` p
ON f.School_ID = p.School_ID
JOIN `chicago-public-schools-data.cps_data_project.sat_grade_11_dim` q
ON f.School_ID = q.School_ID
JOIN `chicago-public-schools-data.cps_data_project.school_dim` r
ON f.School_ID = r.School_ID
JOIN `chicago-public-schools-data.cps_data_project.school_survey_dim` s
ON f.School_ID = s.School_ID
JOIN `chicago-public-schools-data.cps_data_project.suspension_and_discipline_dim` t
ON f.School_ID = t.School_ID);
