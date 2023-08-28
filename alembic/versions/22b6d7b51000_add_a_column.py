"""Add a column

Revision ID: 22b6d7b51000
Revises: 0956f6015d13
Create Date: 2023-08-25 21:17:21.063774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22b6d7b51000'
down_revision: Union[str, None] = '0956f6015d13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('customer', sa.Column('updated_at', sa.DateTime))


def downgrade() -> None:
    op.drop_column('customer', 'updated_at')
