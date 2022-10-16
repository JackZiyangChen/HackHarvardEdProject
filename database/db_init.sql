CREATE DATABASE IF NOT EXISTS userCollege;
USE userCollege;

CREATE TABLE Users(
 user_id INTEGER AUTO_INCREMENT,
 username VARCHAR(100),
 password VARCHAR(100) NOT NULL,
 first_name VARCHAR(100),
 last_name VARCHAR(100),
 email VARCHAR(100),
 zip_code VARCHAR(5),
 major VARCHAR(100),
 
 PRIMARY KEY (user_id)
);
 
CREATE TABLE UserGrades(
 user_id INTEGER,
 gpa FLOAT,
 sat_score INTEGER,
 act_score INTEGER ,
 
 PRIMARY KEY (user_id),
 FOREIGN KEY (user_id)
 REFERENCES Users(user_id)
);

CREATE TABLE UserExtracurricular(
 user_id INTEGER,
 area VARCHAR(100),
 
 PRIMARY KEY (user_id),
 FOREIGN KEY (user_id)
 REFERENCES Users(user_id)
);

CREATE TABLE CollegeProgress(
 user_id INTEGER,
 college_id INTEGER,
 college_name VARCHAR(100),
 sent_transcript VARCHAR(100), 
 main_essay VARCHAR(100),
 supplement_essay VARCHAR(100),
 recommendation_letters VARCHAR(100),
 payment VARCHAR(100),
 deadline DATE,
 admission_type VARCHAR(100),
 
 PRIMARY KEY (user_id, college_id),
 FOREIGN KEY (user_id)
 REFERENCES Users(user_id),
 FOREIGN KEY (college_id)
 REFERENCES CollegeInfo(college_id)
);

CREATE TABLE CollegeInfo(
 college_id INTEGER AUTO_INCREMENT,
 college_name VARCHAR(100),
 tuition_in_state INTEGER,
 tuition_out_of_state INTEGER,
 avg_gpa INTEGER,
 location VARCHAR(100),
 admission_rate FLOAT,
 campus_size INTEGER,
 most_popular_disciplines VARCHAR(100),
 
 PRIMARY KEY (college_id)
);

CREATE TABLE CollegeRequirement(
 college_id INTEGER,
 college_name VARCHAR(100),
 main_essay BOOLEAN,
 supplement_essay BOOLEAN,
 recommendation_letters BOOLEAN,
 
 PRIMARY KEY (college_id),
 FOREIGN KEY (college_id)
 REFERENCES CollegeInfo(college_id)
);

CREATE TABLE college_data(
 name VARCHAR(100),
 cost_of_attendance_in_state INTEGER,
 tuition_in_state INTEGER,
 cost_of_attendance_out_of_state INTEGER,
 tuition_out_of_state INTEGER,
 students_offered_wait_list	INTEGER,
 average_gpa FLOAT,
 overall_admission_rate	INTEGER,
 overall_admission_rate_men	INTEGER,
 overall_admission_rate_women INTEGER,
 received_financial_aid	INTEGER,
 need_fully_met	INTEGER,
 average_percent_of_need_met FLOAT,
 average_award FLOAT,
 average_indebtedness_of_2018_graduates	FLOAT,
 academic_calendar_system VARCHAR(100),
 most_popular_disciplines VARCHAR(100),
 location VARCHAR(100),
 city_size INTEGER,
 campus_size INTEGER,
 avg_low_in_jan	FLOAT,
 avg_high_in_sep FLOAT,
 college_housing INTEGER,
 sororities	INTEGER,
 fraternities INTEGER,
 coeducational INTEGER,
 all_undergraduates	INTEGER,
 all_undergraduates_women FLOAT,	
 all_undergraduates_men	FLOAT,
 international_students	INTEGER,
 first_year_students_returning	INTEGER,
 students_graduating_within_4_years	INTEGER,
 students_graduating_within_6_years	INTEGER,
 average_starting_salary INTEGER,
 graduates_pursuing_advanced_study_directly FLOAT
 
);

LOAD DATA LOCAL INFILE '/Users/iris/Downloads/BU/Fall 2022/HackHarvard/HackHarvardEdProject/database/college_data.csv'
INTO TABLE college_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

INSERT INTO CollegeInfo (
 college_name,
 tuition_in_state,
 tuition_out_of_state,
 avg_gpa,
 location,
 admission_rate,
 campus_size,
 most_popular_disciplines)
SELECT name,
 tuition_in_state,
 tuition_out_of_state,
 average_gpa,
 location,
 overall_admission_rate,
 campus_size,
 most_popular_disciplines
FROM college_data;

CREATE TABLE us_news_data (
 id INTEGER,
 rankingType VARCHAR(100),
 name VARCHAR(100),
 urlName VARCHAR(100),
 region VARCHAR(100),
 fundingType VARCHAR(100),
 ranks INTEGER,
 location VARCHAR(100),
 tuition INTEGER,
 totalUndergraduate INTEGER,
 costAfterAid INTEGER,
 percentReceivingAid FLOAT,
 acceptanceRate FLOAT,
 hsGpa FLOAT,
 engineeringRepScore FLOAT,
 businessRepScore FLOAT,
 computerScienceRepScore FlOAT,
 nursingRepScore FLOAT,
 sat25 INTEGER,
 sat75 INTEGER,
 act25 INTEGER,
 act75 INTEGER
);

LOAD DATA LOCAL INFILE '/Users/iris/Downloads/BU/Fall 2022/HackHarvard/us_news_2023.csv'
INTO TABLE us_news_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;