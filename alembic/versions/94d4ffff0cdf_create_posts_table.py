"""create posts table

Revision ID: 94d4ffff0cdf
Revises: 
Create Date: 2022-05-24 20:02:47.058875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94d4ffff0cdf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():    
    op.drop_table('posts')
    pass
