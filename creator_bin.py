# Imports
import pandas as pd
import random
from datetime import datetime
from DataBaseConnector.dbconnector import DataBaseConnector
import time

if __name__ =='__main__':
    #read source files
    last_names_df = pd.read_csv('last_names.txt')
    male_names =  pd.read_csv('male_names.txt')
    female_names =  pd.read_csv('female_names.txt')
    domains_df  =  pd.read_csv('domain.txt')
    area_code_df =  pd.read_csv('area_code.csv',delimiter='\t')

    # change to Capital on last names dataframe
    last_names_df.last_name=last_names_df.last_name.str.capitalize()

    #create database connector object
    conn = DataBaseConnector('ODOO')

    sql = '''insert into res_partner (name,
                                email,
                                phone,
                                active,
                                is_company,
                                partner_share,
                                email_normalized,
                                phone_sanitized,
                                create_date,
                                write_date)
                                values(
                                %(name)s,
                                %(email)s,
                                
                                %(phone)s,
                                %(active)s,
                                %(is_company)s,
                                %(partner_share)s,
                                %(email_normalized)s,
                                %(phone_sanitized)s,
                                %(create_date)s,
                                %(write_date)s
                                )'''
    #Create a customers :
    execute=True
    while execute:
        for i in range(random.randrange(4,10)):
                name = male_names.loc[random.randrange(0,len(male_names.index)),['name']].values[0]
                last_name = last_names_df.loc[random.randrange(0,len(last_names_df.index)),['last_name']].values[0]
                domain =  domains_df.loc[random.randrange(0,len(domains_df.index)),['domain']].values[0]
                e_mail = name+'.'+last_name+'@'+domain
                code = area_code_df.loc[random.randrange(0,len(area_code_df.index)),['code']].values[0]
                phone = '('+str(code)+')'+str(random.randrange(970,980))+'-'+str(random.randrange(4387,7893))
                params={'name':name+' '+last_name,
                        'email':e_mail if random.random()>0.36 else '',
                        'phone': phone if random.random() > 0.26 else '',
                        'is_company':False,
                        'partner_share':False,
                        'email_normalized':  e_mail if random.random()>0.7 else '',
                        'phone_sanitized':phone,
                        'active':'True',
                        'create_date':datetime.now(),
                        'write_date':datetime.now()
                        }
                conn.execute_insert(sqlquery=sql,sqlparams=params)
                params
        time.sleep(60)    