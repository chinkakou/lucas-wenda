"""empty message

Revision ID: 3689492a22d7
Revises: 9f448112c017
Create Date: 2019-02-13 18:39:59.806348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3689492a22d7'
down_revision = '9f448112c017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'create_time')
    # ### end Alembic commands ###
