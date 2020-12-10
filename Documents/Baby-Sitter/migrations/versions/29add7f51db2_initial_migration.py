"""Initial Migration

Revision ID: 29add7f51db2
Revises: d25071df59d4
Create Date: 2020-12-10 17:49:07.660027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29add7f51db2'
down_revision = 'd25071df59d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('post_address', sa.String(), nullable=True))
    op.drop_column('posts', 'post_contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('post_contact', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('posts', 'post_address')
    # ### end Alembic commands ###