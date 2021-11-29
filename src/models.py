#!/usr/bin/env python3

#DEPENDS(sqlalchemy)
import sqlalchemy as sa
from sqlalchemy import create_engine, text


engine = create_engine('sqlite+pysqlite:///../data/file.sqlite', echo=True, future=True)
metadata_obj = sa.MetaData(bind=engine)

tasks = sa.Table(
    'task', metadata_obj,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.Text, nullable=False),
    sa.Column('description', sa.Text),
    sa.Column('importance', sa.SmallInteger),
    sa.Column('due_time', sa.DateTime),
    sa.Column('urgency', sa.SmallInteger),
    sa.Column('reputation', sa.SmallInteger),
    sa.Column('amortized_cost', sa.SmallInteger),
    sa.Column('estimated_seconds', sa.Interval),
    sa.Column('unknowns', sa.Text),
    sa.Column('waiting', sa.Text, default=None),
)


with engine.connect() as conn:
    # import ipdb; ipdb.set_trace()
    print(conn.execute(tasks.select()).all())
    # query = Task.
    # result = conn.execute(text("select 'hello, world'"))
    # print(result.all())
