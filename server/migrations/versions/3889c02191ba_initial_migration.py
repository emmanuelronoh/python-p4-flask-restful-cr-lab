"""Initial migration

Revision ID: 3889c02191ba
Revises: 
Create Date: 2024-10-12 12:33:11.863472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3889c02191ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
