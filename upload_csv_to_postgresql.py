import uuid

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID

db_url = "postgresql://postgres:mac123@localhost:5432/postgres"

csv_file_path = "/Users/sanjanabalachandran/Downloads/hospitals_staging_data.csv"

engine = create_engine(db_url)

df = pd.read_csv(csv_file_path)


def convert_to_uuid(value):
    return uuid.UUID(value) if pd.notnull(value) else None


df['id'] = df['id'].apply(convert_to_uuid)
df['deleted_by_id'] = df['deleted_by_id'].apply(convert_to_uuid)

df.to_sql('hospitals', engine, if_exists='append', index=False, dtype={
    "id": UUID(as_uuid=True),
    "deleted_by_id": UUID(as_uuid=True)
})

print("Data uploaded")
