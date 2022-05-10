"""Sixtysix_test Migration 

Revision ID: 99a95aa7ffb3
Revises: fefdae9ee0b9
Create Date: 2022-05-10 06:45:17.441178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a95aa7ffb3'
down_revision = 'fefdae9ee0b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    op.drop_column('users', 'email')
    op.drop_table('comments')
    # ### end Alembic commands ###
