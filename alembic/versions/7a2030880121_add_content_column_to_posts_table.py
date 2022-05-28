"""add content column to posts table

Revision ID: 7a2030880121
Revises: 94d4ffff0cdf
Create Date: 2022-05-24 20:32:02.667272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a2030880121'
down_revision = '94d4ffff0cdf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass  
