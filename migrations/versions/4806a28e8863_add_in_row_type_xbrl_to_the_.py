"""add in row_type_xbrl to the depreciation_amortization_summary_ferc1 table

Revision ID: 4806a28e8863
Revises: cc04ea89a4c8
Create Date: 2023-06-06 13:27:32.834458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4806a28e8863'
down_revision = 'cc04ea89a4c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('row_type_xbrl', sa.Enum('calculated_value', 'reported_value', 'correction'), nullable=True, comment='Indicates whether the value reported in the row is calculated, or uniquely reported within the table.'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.drop_column('row_type_xbrl')

    # ### end Alembic commands ###
