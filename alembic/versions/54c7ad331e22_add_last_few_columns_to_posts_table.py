"""add last few columns to posts table

Revision ID: 54c7ad331e22
Revises: 42ccfe27b644
Create Date: 2022-05-24 20:49:19.244766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54c7ad331e22'
down_revision = '42ccfe27b644'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
