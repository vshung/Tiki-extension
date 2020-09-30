"""empty message

Revision ID: 633aa99b8202
Revises: 
Create Date: 2019-05-06 21:31:57.797725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '633aa99b8202'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('modified_date', sa.DateTime(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price')
    op.drop_table('product')
    # ### end Alembic commands ###