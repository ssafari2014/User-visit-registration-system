"""Add user_agent to page_visits

Revision ID: 067f9f5df02b
Revises: 85e0152e82f6
Create Date: 2025-05-24 18:47:54.930379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '067f9f5df02b'
down_revision: Union[str, None] = '85e0152e82f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # حذف کامل یا کامنت کردن این خط برای SQLite:
    # op.alter_column('page_visits', 'timestamp',
    #                 existing_type=sa.DateTime(),
    #                 nullable=False)
    pass

def downgrade() -> None:
    """Downgrade schema."""
    # حذف کامل یا کامنت کردن این خط برای SQLite:
    # op.alter_column('page_visits', 'timestamp',
    #                 existing_type=sa.DateTime(),
    #                 nullable=True)
    pass

