"""create users

Revision ID: bc4036ff5409
Revises: 
Create Date: 2021-08-05 10:56:11.838797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc4036ff5409'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False)
    )


def downgrade():
    op.drop_table('users')
