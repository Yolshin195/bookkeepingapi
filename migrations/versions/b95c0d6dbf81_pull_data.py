"""pull data

Revision ID: b95c0d6dbf81
Revises: dbcbe4e8d328
Create Date: 2023-08-30 23:57:42.903617

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.orm import Session

from models import Currency, TransactionType, User, Account, Category
from models.user import UserPassword


# revision identifiers, used by Alembic.
revision = 'b95c0d6dbf81'
down_revision = 'dbcbe4e8d328'
branch_labels = None
depends_on = None


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.add_all([

        Currency(id='2103a409-ff56-46d3-98ef-4220036bfec4', created_by='alembic_adm',
                 code='RUB', name='Российский рубль'),
        Currency(id='1545b316-ff4b-4558-8f42-58042f6f381e', created_by='alembic_adm',
                 code='USD', name='Доллар'),
        Currency(id='9fce08b0-89c9-4303-b5b3-e950314ea114', created_by='alembic_adm',
                 code='IDR', name='Индонезийская рупия'),
        Currency(id='f07b9566-cd7c-4f80-b207-870bd7491946', created_by='alembic_adm',
                 code='THB', name='Тайский бат'),

        Account(id='5b50a0d5-5009-4001-b7a4-dc2d2650cb58', created_by='alembic_adm',
                code="RUB", name='Наличные рубли', currency_id='2103a409-ff56-46d3-98ef-4220036bfec4'),
        Account(id='17a6cb11-1cc9-4c12-934a-75a6320220d7', created_by='alembic_adm',
                code="THB", name='Наличные баты', currency_id='f07b9566-cd7c-4f80-b207-870bd7491946'),

        Category(id='c92aed39-5c66-4241-bd5f-39d93ebc6383', created_by='alembic_adm',
                 code="food", name='Еда'),

        TransactionType(id='e103a303-00e7-412b-8f03-d94a7648534f', created_by='alembic_adm',
                        code='expense', name='Доход'),
        TransactionType(id='69decf95-ad00-45de-bb79-0df6becd65fe', created_by='alembic_adm',
                        code='income ', name='Расход'),
        TransactionType(id='826ea6c4-a819-488d-85b4-79e3565b7353', created_by='alembic_adm',
                        code='transfer', name='Перевод'),

        UserPassword(id='dbd7031d-29ee-4bdd-9042-dccab3c25604', created_by='alembic_adm',
                     email='admin@gmail.com',
                     hashed_password="$2b$12$KH7uMs/WZYGWuVzyVCEii.tsPQbJCLqHDRuv6.FK9bIg72xg7lnua"),

        User(id='da99ed40-a394-4b8b-9db4-52dd81814c7c', created_by='alembic_adm',
             username='admin',
             user_password_id='dbd7031d-29ee-4bdd-9042-dccab3c25604',
             is_superuser=True,
             is_verified=True)
    ])
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())

    delete_account_sql = delete(Account).where(Account.id.in_([
        '5b50a0d5-5009-4001-b7a4-dc2d2650cb58',
        '17a6cb11-1cc9-4c12-934a-75a6320220d7',
    ]))
    session.execute(delete_account_sql)

    delete_currency_sql = delete(Currency).where(Currency.id.in_([
        '2103a409-ff56-46d3-98ef-4220036bfec4',
        '1545b316-ff4b-4558-8f42-58042f6f381e',
        '9fce08b0-89c9-4303-b5b3-e950314ea114',
        'f07b9566-cd7c-4f80-b207-870bd7491946',
    ]))
    session.execute(delete_currency_sql)

    delete_transaction_type_sql = delete(TransactionType).where(TransactionType.id.in_([
        'e103a303-00e7-412b-8f03-d94a7648534f',
        '69decf95-ad00-45de-bb79-0df6becd65fe',
        '826ea6c4-a819-488d-85b4-79e3565b7353',
    ]))
    session.execute(delete_transaction_type_sql)

    delete_user_sql = delete(User).where(User.id.in_([
        'da99ed40-a394-4b8b-9db4-52dd81814c7c',
    ]))
    session.execute(delete_user_sql)

    delete_user_password_sql = delete(UserPassword).where(UserPassword.id.in_([
        'dbd7031d-29ee-4bdd-9042-dccab3c25604',
    ]))
    session.execute(delete_user_password_sql)

    session.commit()
