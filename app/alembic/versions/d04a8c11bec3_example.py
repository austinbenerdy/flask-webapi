"""example

Revision ID: d04a8c11bec3
Revises: 72534dacc9da
Create Date: 2021-04-02 21:26:32.753544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd04a8c11bec3'
down_revision = '72534dacc9da'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'example',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=True),
        sa.Column('description', sa.Unicode(200))
    )
    op.execute('INSERT INTO example (name, description) values (\'Austin\', \'A person who does things\')')
    op.execute('INSERT INTO example (name, description) values (\'Rochelle\', \'An awesome software engineer.\')')
    pass


def downgrade():
    op.drop_table('example')
    pass
