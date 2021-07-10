"""Create log_post table

Revision ID: 179c22e19a6f
Revises:
Create Date: 2021-07-05 10:23:52.720900

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '179c22e19a6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_post',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('last_updated', sa.DateTime(), nullable=False),
                    sa.Column('title', sa.Text(), nullable=False),
                    sa.Column('content', sa.Text(), nullable=True),
                    sa.Column('is_markdown', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log_post')
    # ### end Alembic commands ###
