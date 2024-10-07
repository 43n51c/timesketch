"""Linking Analysis and InvestigativeQuestion models.

Revision ID: 87d24c7252fc
Revises: c5560d97a2c8
Create Date: 2024-10-02 16:17:42.576745

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "87d24c7252fc"
down_revision = "c5560d97a2c8"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("analysis", schema=None) as batch_op:
        batch_op.add_column(sa.Column("approach_id", sa.Integer(), nullable=True))
        batch_op.add_column(
            sa.Column("question_conclusion_id", sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            None, "investigativequestionconclusion", ["question_conclusion_id"], ["id"]
        )
        batch_op.create_foreign_key(
            None, "investigativequestionapproach", ["approach_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("analysis", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("question_conclusion_id")
        batch_op.drop_column("approach_id")

    # ### end Alembic commands ###
