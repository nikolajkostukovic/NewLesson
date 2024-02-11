"""create_table

Revision ID: 455b9d1988e2
Revises: 
Create Date: 2024-02-07 21:45:52.972030

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

# revision identifiers, used by Alembic.
revision: str = '455b9d1988e2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('currency',
                    sa.Column('id', sa.UUID(as_uuid=True), server_default=sa.text("uuid_generate_v4()"), nullable=False),
                    sa.Column('numCode', sa.Text),
                    sa.Column('charCode', sa.Text),
                    sa.Column('nominal', sa.Integer),
                    sa.Column('name', sa.Text),  # Фунт
                    sa.Column('value', sa.Float),  # 43, 8254
                    sa.Column('vunitRate', sa.Float),  # 43, 8254
                    sa.Column('date', sa.DateTime)
                    )


def downgrade() -> None:
    op.drop_table('currency')
