### Enem database analysis 


Extraction transformation and loading process to access the Enem database information. Here, there are some cleaning flow to get insights about Enem exam. The visualizations were obtained by using Microsoft Power BI service. The aim of this project is to show some patterns and the distribution of students scores by Brazilian states.



## ENEM (Exame Nacional do Ensino Médio) ℹ️ 
- Enem is a Brazilian exam and it is the key way to enroll in higher education in Brazil.

The MICRODADOS_ENEM_2017 dataset contains the information about the quiz answered by students, the location where the tests were performed, school data and their scores in 2017. The data can be found in Inep Data. 

### Dictionary of Variables: 

- NU_INSCRICAO: Student registration number
- NU_IDADE: Age 
- TP_ESTADO_CIVIL: Marital Status
- TP_NACIONALIDADE: Nationality
- TP_ST_CONCLUSAO: High School Conclusion Time
- TP_ANO_CONCLUIU: The Year of High School Conclusion 
- IN_TREINEIRO: Exam Trainer?
- COMPUTADOR 'Sim' if the participant has a computer at home/ 'Não' if the participant does not have a computer at home
- INTERNET
- NO_MUNICIPIO_ESC: City
- SG_UF_ESC: Acronym of the Federative Unit in which the school is located
- TP_LOCALIZACAO_ESC: School localization
- TP_DEPENDENCIA_ADM_ESC: School Administrative Dependency
- NO_MUNICIPIO_RESIDENCIA: City where the participant lives 
- SG_UF_RESIDENCIA: Acronym of the Federative Unit that the participant lives
- NU_NOTA_CN: Natural Science Score
- NU_NOTA_CH: Human Science Score 
- NOTA_LC: Languages and codes Score
- NOTA_MT: Math Score 
- NU_NOTA_REDACAO: Writing Score 
- NOTA_FINAL: Final Score 


### Main libraries:

- Data cleaning steps was processed by using pandas library (Anaconda Python distribution)
- The boto3 was used to connect with Amazon Web Services (AWS) Software Development Kit (SDK) with Python. Boto3 allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2


### Business Intelligence insights

- The visualizations obtained allow us to understand: 
    - How was students' grades distributed across the Brazilian territory
    - The interaction between grade and other variables



