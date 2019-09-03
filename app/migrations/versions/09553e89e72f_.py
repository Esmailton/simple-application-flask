"""empty message

Revision ID: 09553e89e72f
Revises: 33fc9077c801
Create Date: 2019-09-02 20:00:10.960455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09553e89e72f'
down_revision = '33fc9077c801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'employee', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'employee_id')
    # ### end Alembic commands ###
