"""empty message

Revision ID: d0a22cc5b56f
Revises: 0eb20b86aacf
Create Date: 2019-08-28 04:35:31.614403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a22cc5b56f'
down_revision = '0eb20b86aacf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'airplanes',
        sa.Column('id', sa.String(length=60), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('created_by', sa.String(), nullable=True),
        sa.Column('updated_by', sa.String(), nullable=True),
        sa.Column('model', sa.String(length=60), nullable=False),
        sa.Column('type', sa.String(length=60), nullable=False),
        sa.Column('capacity', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_airplanes'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('airplanes')
    # ### end Alembic commands ###
