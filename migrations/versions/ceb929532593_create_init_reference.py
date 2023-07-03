"""create init reference

Revision ID: ceb929532593
Revises: 015adb87f2a8
Create Date: 2023-07-02 20:33:29.346824

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.orm import Session

from models import Currency, TransactionType, User, Account, Category

# revision identifiers, used by Alembic.
revision = 'ceb929532593'
down_revision = '015adb87f2a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.add_all([

        Currency(id='2103a409-ff56-46d3-98ef-4220036bfec4', created_by='alembic_adm', version=1,
                 code='RUB', name='Российский рубль'),
        Currency(id='1545b316-ff4b-4558-8f42-58042f6f381e', created_by='alembic_adm', version=1,
                 code='USD', name='Доллар'),
        Currency(id='9fce08b0-89c9-4303-b5b3-e950314ea114', created_by='alembic_adm', version=1,
                 code='IDR', name='Индонезийская рупия'),

        Account(id='5b50a0d5-5009-4001-b7a4-dc2d2650cb58', created_by='alembic_adm', version=1,
                code="RUB", name='Наличные рубли', currency_id='2103a409-ff56-46d3-98ef-4220036bfec4'),

        Category(id='c92aed39-5c66-4241-bd5f-39d93ebc6383', created_by='alembic_adm', version=1,
                 code="food", name='Еда'),

        TransactionType(id='e103a303-00e7-412b-8f03-d94a7648534f', created_by='alembic_adm', version=1,
                        code='expense', name='Доход'),
        TransactionType(id='69decf95-ad00-45de-bb79-0df6becd65fe', created_by='alembic_adm', version=1,
                        code='income ', name='Расход'),
        TransactionType(id='826ea6c4-a819-488d-85b4-79e3565b7353', created_by='alembic_adm', version=1,
                        code='transfer', name='Перевод'),

        User(id='da99ed40-a394-4b8b-9db4-52dd81814c7c',
             created_by='alembic_adm',
             version=1,
             login='admin',
             username='admin',
             email='admin@gmail.com',
             hash_password="admin_password")
    ])
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    delete_currency_sql = delete(Currency).where(Currency.id.in_([
        '2103a409-ff56-46d3-98ef-4220036bfec4',
        '1545b316-ff4b-4558-8f42-58042f6f381e',
        '9fce08b0-89c9-4303-b5b3-e950314ea114'
    ]))
    session.execute(delete_currency_sql)

    delete_transaction_type_sql = delete(TransactionType).where(TransactionType.id.in_([
        'e103a303-00e7-412b-8f03-d94a7648534f',
        '69decf95-ad00-45de-bb79-0df6becd65fe',
        '826ea6c4-a819-488d-85b4-79e3565b7353'
    ]))
    session.execute(delete_transaction_type_sql)

    delete_user_sql = delete(User).where(User.id.in_([
        'da99ed40-a394-4b8b-9db4-52dd81814c7c'
    ]))
    session.execute(delete_user_sql)

    session.commit()

