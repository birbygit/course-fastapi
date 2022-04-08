"""add users table

Revision ID: 785f2d0d4f06
Revises: 0e91399e239a
Create Date: 2022-04-08 10:07:19.846794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '785f2d0d4f06'
down_revision = '0e91399e239a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
