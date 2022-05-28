"""add foreign-key to posts table

Revision ID: 42ccfe27b644
Revises: f379898be74b
Create Date: 2022-05-24 20:43:30.299976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42ccfe27b644'
down_revision = 'f379898be74b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
