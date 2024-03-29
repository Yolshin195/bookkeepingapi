"""init baseData

Revision ID: dbcbe4e8d328
Revises: 
Create Date: 2023-08-30 23:56:49.454585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbcbe4e8d328'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookkeeping_api_category',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookkeeping_api_currency',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookkeeping_api_telegram_user',
    sa.Column('telegram_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bookkeeping_api_telegram_user_telegram_id'), 'bookkeeping_api_telegram_user', ['telegram_id'], unique=True)
    op.create_table('bookkeeping_api_transaction_type',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookkeeping_api_user_password',
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bookkeeping_api_user_password_email'), 'bookkeeping_api_user_password', ['email'], unique=True)
    op.create_table('bookkeeping_api_account',
    sa.Column('currency_id', sa.Uuid(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['currency_id'], ['bookkeeping_api_currency.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookkeeping_api_user',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('user_password_id', sa.Uuid(), nullable=True),
    sa.Column('telegram_user_id', sa.Uuid(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['telegram_user_id'], ['bookkeeping_api_telegram_user.id'], ),
    sa.ForeignKeyConstraint(['user_password_id'], ['bookkeeping_api_user_password.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookkeeping_api_transaction',
    sa.Column('owner_id', sa.Uuid(), nullable=False),
    sa.Column('type_id', sa.Uuid(), nullable=False),
    sa.Column('expense_account_id', sa.Uuid(), nullable=True),
    sa.Column('expense', sa.Numeric(), nullable=True),
    sa.Column('income_account_id', sa.Uuid(), nullable=True),
    sa.Column('income', sa.Numeric(), nullable=True),
    sa.Column('category_id', sa.Uuid(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['bookkeeping_api_category.id'], ),
    sa.ForeignKeyConstraint(['expense_account_id'], ['bookkeeping_api_account.id'], ),
    sa.ForeignKeyConstraint(['income_account_id'], ['bookkeeping_api_account.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['bookkeeping_api_user.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['bookkeeping_api_transaction_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookkeeping_api_transaction')
    op.drop_table('bookkeeping_api_user')
    op.drop_table('bookkeeping_api_account')
    op.drop_index(op.f('ix_bookkeeping_api_user_password_email'), table_name='bookkeeping_api_user_password')
    op.drop_table('bookkeeping_api_user_password')
    op.drop_table('bookkeeping_api_transaction_type')
    op.drop_index(op.f('ix_bookkeeping_api_telegram_user_telegram_id'), table_name='bookkeeping_api_telegram_user')
    op.drop_table('bookkeeping_api_telegram_user')
    op.drop_table('bookkeeping_api_currency')
    op.drop_table('bookkeeping_api_category')
    # ### end Alembic commands ###
