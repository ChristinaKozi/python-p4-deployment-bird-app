"""empty message

Revision ID: e1f055bffad0
Revises: 40ce37b01971
Create Date: 2024-04-05 11:09:06.037013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1f055bffad0'
down_revision = '40ce37b01971'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('birds', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('birds', 'image')
    # ### end Alembic commands ###
