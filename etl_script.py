import pandas as pd
import boto3
import io

# Credentials IAM
client = boto3.client('s3',
            aws_access_key_id='############',
            aws_secret_access_key='############################'
        )

bucket_name = 'enemdata'
file_key = 'raw/df_particionado_300000.csv'

response = client.get_object(Bucket=bucket_name, Key=file_key)

# Reading a sample of enem data from S3
initial_df = pd.read_csv((io.BytesIO(response['Body'].read())), encoding= 'utf-8', sep = ',') # 'Body' is a key word

#score_table
notas = pd.DataFrame(initial_df, columns = ['NU_INSCRICAO','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO'])
notas['NOTA_FINAL'] = (notas['NU_NOTA_CN'] + notas['NU_NOTA_CH'] + notas['NU_NOTA_LC'] + notas['NU_NOTA_MT'] + notas['NU_NOTA_REDACAO'])/5

#students_table
alunos = pd.DataFrame(initial_df, columns = ['NU_INSCRICAO','NU_IDADE','TP_ESTADO_CIVIL','TP_NACIONALIDADE','TP_ST_CONCLUSAO','TP_ANO_CONCLUIU', 'IN_TREINEIRO', 'Q025', 'Q024', 'Q006', 'SG_UF_RESIDENCIA', 'NO_MUNICIPIO_RESIDENCIA'])

# replace column values in students_table
dicionario_estado_civil ={0:'Solteiro(a)', 1:'Casado(a)/Mora com companheiro(a)',2:'Divorciado(a)/Desquitado(a)/Separado(a)', 3:'Viúvo(a)'}
alunos['TP_ESTADO_CIVIL'] = alunos['TP_ESTADO_CIVIL'].map(dicionario_estado_civil)

dicionario_tp_nacionali ={0:'Não informado',1:'Brasileiro(a)', 2:'Brasileiro(a) Naturalizado(a)',3:'Estrangeiro(a)', 4:'Brasileiro(a) Nato(a), nascido(a) no exterior'}
alunos['TP_NACIONALIDADE'] = alunos['TP_NACIONALIDADE'].map(dicionario_tp_nacionali)

dicionario_tp_st_conclusao = {1:'Já concluí o Ensino Médio', 2:'Estou cursando e concluirei o Ensino Médio em 2017', 3:'Estou cursando e concluirei o Ensino Médio após 2017', 4:'Não concluí e não estou cursando o Ensino Médio'}
alunos['TP_ST_CONCLUSAO'] = alunos['TP_ST_CONCLUSAO'].map(dicionario_tp_st_conclusao)

dicionario_tp_ano_concluiu = {0:'Não informado',1:'2016',2:'2015',3:'2014',4:'2013',5:'2012',6:'2011',7:'2010',8:'2009',9:'2008',10:'2007',11:'Antes de 2007'}
alunos['TP_ANO_CONCLUIU'] = alunos['TP_ANO_CONCLUIU'].map(dicionario_tp_ano_concluiu)

alunos['IN_TREINEIRO'] = alunos['IN_TREINEIRO'].replace({1:'Sim', 0:'Não'})

alunos['NOTA_FINAL'] = notas['NOTA_FINAL']



# rename columns
alunos.rename(columns={'Q025':'INTERNET_EM_CASA', 'Q024':'COMPUTADOR_EM_CASA', 'Q006':'RENDA_MENSAL'}, inplace = True)

dicionario_internet = {'A':'Não', 'B':'Sim'}
alunos['INTERNET_EM_CASA'] = alunos['INTERNET_EM_CASA'].map(dicionario_internet)

dicionario_computador = {'A':'Não', 'B':'Sim, um ou mais', 'C':'Sim, um ou mais', 'D':'Sim, um ou mais', 'E':'Sim, um ou mais'}
alunos['COMPUTADOR_EM_CASA'] = alunos['COMPUTADOR_EM_CASA'].map(dicionario_computador)

dicionario_renda_mensal = {'A':'Nenhuma renda','B':'Até R$ 937,00', 'C':'De R$ 937,01 até R$ 1.405,50', 'D':'De R$ 1.405,51 até R$ 1.874,00', 'E':'De R$ 1.874,01 até R$ 2.342,50','F':'De R$ 2.342,51 até R$ 2.811,00','G':'De R$ 2.811,01 até R$ 3.748,00', 'H':'De R$ 3.748,01 até R$ 4.685,00', 'I':'De R$ 4.685,01 até R$ 5.622,00', 'J':'De R$ 5.622,01 até R$ 6.559,00', 'K':'De R$ 6.559,01 até R$ 7.496,00', 'L':'De R$ 7.496,01 até R$ 8.433,00', 'M':'De R$ 8.433,01 até R$ 9.370,00', 'N':'De R$ 9.370,01 até R$ 11.244,00', 'O':'De R$ 11.244,01 até R$ 14.055,00', 'P':'De R$ 14.055,01 até R$ 18.740,00', 'Q':'Mais de R$ 18.740,00'}
alunos['RENDA_MENSAL'] = alunos['RENDA_MENSAL'].map(dicionario_renda_mensal)

#school_table
escola = pd.DataFrame(initial_df, columns = ['NU_INSCRICAO','NO_MUNICIPIO_ESC','SG_UF_ESC','TP_LOCALIZACAO_ESC', 'TP_DEPENDENCIA_ADM_ESC'])

