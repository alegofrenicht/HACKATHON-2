"""empty message

Revision ID: 92f6cd9f3f6d
Revises: 1c276133e027
Create Date: 2023-04-11 15:34:40.480610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f6cd9f3f6d'
down_revision = '1c276133e027'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar_movie', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar_movie', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)

    # ### end Alembic commands ###