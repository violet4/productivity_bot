"""empty message

Revision ID: 7daad4519c97
Revises: 
Create Date: 2021-11-28 19:55:54.895960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7daad4519c97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """
    importance
    due date
    urgency
    affects reputation
    amortized cost (e.g. test environment)
    estimated seconds
    unknowns
    waiting (follow-up?)
    """
    op.create_table(
        'task',
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


def downgrade():
    op.drop_table('task')
