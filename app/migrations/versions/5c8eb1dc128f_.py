"""empty message

Revision ID: 5c8eb1dc128f
Revises: ca2e9b9fd45e
Create Date: 2019-07-01 19:37:48.619445

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5c8eb1dc128f'
down_revision = 'ca2e9b9fd45e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movement_status')
    op.add_column('movement', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movement', 'status')
    op.create_table('movement_status',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('movement_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movement_id'], ['movement.id'], name='movement_status_movement_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='movement_status_pkey')
    )
    # ### end Alembic commands ###
