"""empty message

Revision ID: 0e827423a316
Revises: 11dc3f71ef22
Create Date: 2018-12-12 20:54:37.653497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e827423a316'
down_revision = '11dc3f71ef22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.Column('image_url', sa.String(length=120), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookmark')
    # ### end Alembic commands ###
