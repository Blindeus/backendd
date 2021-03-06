"""empty message

Revision ID: 1f482c20ad80
Revises: 
Create Date: 2021-07-06 01:08:12.773983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f482c20ad80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('rut', sa.String(), nullable=False),
    sa.Column('numeroDocumento', sa.String(), nullable=False),
    sa.Column('fechaNacimiento', sa.String(), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
