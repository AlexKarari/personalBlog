"""flask admin initialised.

Revision ID: 42e60097bb83
Revises: 156124c92c9f
Create Date: 2018-04-20 15:34:01.457448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e60097bb83'
down_revision = '156124c92c9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_blogger_email'), 'blogger', ['email'], unique=True)
    op.drop_constraint('blogger_email_key', 'blogger', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('blogger_email_key', 'blogger', ['email'])
    op.drop_index(op.f('ix_blogger_email'), table_name='blogger')
    # ### end Alembic commands ###