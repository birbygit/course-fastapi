"""Add content column to posts table

Revision ID: 0e91399e239a
Revises: ef2e14f18817
Create Date: 2022-04-08 09:57:24.538638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e91399e239a'
down_revision = 'ef2e14f18817'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
