import pandas as pd
import psycopg2 as pg
from psycopg2.extras import execute_values
import time
import json
import pandas as pd



def load_data(data):
    policy_df = pd.DataFrame(data)
    policy_df['updated_date'] = policy_df['_udate'].apply(lambda x: x['$date']if isinstance(x, dict) else None)
    policy_df.drop('_udate', axis=1, inplace=True)
    policy_df['created_date'] = policy_df['_date'].apply(lambda x: x['$date']if isinstance(x, dict) else None)
    policy_df.drop('_date', axis=1, inplace=True)
    policy_df = policy_df.rename(columns={'_id': 'id', 'stage': 'stage', 'ModuleID': 'module_id','policyStatus': 'policy_status'})
    policy_df = policy_df.rename(columns={'clientid': 'client_id'})
    policy_df['insurer_name'] = policy_df['insurer'].str.split('-').str[0]
    
    return policy_df




def insert_data(conn, json_data):
    df = load_data(json_data)
    start_time = time.time() # get start time before insert
    with conn.cursor() as c:
        execute_values(
            cur=c,
            sql="""
                INSERT INTO policies
                (id,insurer,stage,client_id,product,module_id,policy_status,updated_date,created_date,insurer_name)
                VALUES %s;
                """,
            argslist=df.to_dict(orient="records"),
            template="""
                (
                    %(id)s,%(insurer)s, %(stage)s, %(client_id)s,
                    %(product)s, %(module_id)s, %(policy_status)s,
                    %(updated_date)s, %(created_date)s,
                    %(insurer_name)s
                )
                """
        )
        conn.commit()

    end_time = time.time() # get end time after insert
    total_time = end_time - start_time # calculate the time
    print(f"Insert time: {total_time} seconds")
