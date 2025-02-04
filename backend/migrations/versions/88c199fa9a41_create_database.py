"""Create database

Revision ID: 88c199fa9a41
Revises: 
Create Date: 2025-01-19 12:59:24.405836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88c199fa9a41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('makro_calories', sa.Float(), nullable=True),
    sa.Column('makro_carbs', sa.Float(), nullable=True),
    sa.Column('makro_protein', sa.Float(), nullable=True),
    sa.Column('makro_fat', sa.Float(), nullable=True),
    sa.Column('base_unit', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipes',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('recipe_id', sa.UUID(), nullable=True),
    sa.Column('filepath', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('recipe_id', sa.UUID(), nullable=True),
    sa.Column('ingredient_id', sa.UUID(), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredients')
    op.drop_table('images')
    op.drop_table('recipes')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
