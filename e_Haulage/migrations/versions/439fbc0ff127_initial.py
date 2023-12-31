"""Initial

Revision ID: 439fbc0ff127
Revises: 
Create Date: 2023-09-08 21:46:39.498631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '439fbc0ff127'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user2_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('f_user2', 'user2', ['user2_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=120),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=60),
               nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=50),
               nullable=False)

    with op.batch_alter_table('user2', schema=None) as batch_op:
        batch_op.drop_column('house_address')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user2', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('house_address', sa.VARCHAR(length=150), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=150),
               nullable=True)

    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.drop_constraint('f_user2', type_='foreignkey')
        batch_op.drop_column('user2_id')

    # ### end Alembic commands ###
