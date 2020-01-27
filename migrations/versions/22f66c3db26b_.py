"""empty message

Revision ID: 22f66c3db26b
Revises: 
Create Date: 2020-01-27 00:52:39.430745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f66c3db26b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('usage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usage_id'], ['usage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_receipt_timestamp'), 'receipt', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_receipt_timestamp'), table_name='receipt')
    op.drop_table('receipt')
    op.drop_table('usage')
    # ### end Alembic commands ###