"""config table inclusion

Revision ID: 234f9c1deef3
Revises: 
Create Date: 2023-09-13 15:19:22.299003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '234f9c1deef3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('config_samples_per_packet', sa.Integer(), nullable=True),
    sa.Column('class_map', sa.JSON(), nullable=True),
    sa.Column('model_json', sa.JSON(), nullable=True),
    sa.Column('loop', sa.Boolean(), nullable=True),
    sa.Column('data_type', sa.String(), nullable=True),
    sa.Column('sml_library_path', sa.String(), nullable=True),
    sa.Column('run_sml_model', sa.Boolean(), nullable=True),
    sa.Column('convert_to_int16', sa.Boolean(), nullable=True),
    sa.Column('scaling_factor', sa.Float(), nullable=True),
    sa.Column('device_id', sa.String(), nullable=True),
    sa.Column('sample_rate', sa.Float(), nullable=True),
    sa.Column('config_columns', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_configs_device_id'), 'configs', ['device_id'], unique=True)
    op.create_index(op.f('ix_configs_id'), 'configs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_configs_id'), table_name='configs')
    op.drop_index(op.f('ix_configs_device_id'), table_name='configs')
    op.drop_table('configs')
    # ### end Alembic commands ###
