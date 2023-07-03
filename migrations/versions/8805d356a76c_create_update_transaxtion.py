"""create update transaxtion

Revision ID: 8805d356a76c
Revises: ceb929532593
Create Date: 2023-07-03 20:17:43.267244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8805d356a76c'
down_revision = 'ceb929532593'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookkeeping_api_transaction', 'expense_account_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('bookkeeping_api_transaction', 'expense',
               existing_type=sa.NUMERIC(),
               nullable=True)
    op.alter_column('bookkeeping_api_transaction', 'income_account_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('bookkeeping_api_transaction', 'income',
               existing_type=sa.NUMERIC(),
               nullable=True)
    op.alter_column('bookkeeping_api_transaction', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookkeeping_api_transaction', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('bookkeeping_api_transaction', 'income',
               existing_type=sa.NUMERIC(),
               nullable=False)
    op.alter_column('bookkeeping_api_transaction', 'income_account_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('bookkeeping_api_transaction', 'expense',
               existing_type=sa.NUMERIC(),
               nullable=False)
    op.alter_column('bookkeeping_api_transaction', 'expense_account_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###