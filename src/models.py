#!/usr/bin/env python3

#DEPENDS(sqlalchemy)
import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine('sqlite+pysqlite:///file.sqlite', echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello, world'"))
    print(result.all())


