"""Add o campo currency em person

Revision ID: 0f77ef3aba06
Revises: 7e3679be81ba
Create Date: 2023-02-10 13:17:53.407233

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '0f77ef3aba06'
down_revision = '7e3679be81ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('currency', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'currency')
    # ### end Alembic commands ###