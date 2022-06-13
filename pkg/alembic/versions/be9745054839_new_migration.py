"""New Migration

Revision ID: be9745054839
Revises: 
Create Date: 2022-06-12 03:46:26.779482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "be9745054839"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("login", sa.String(), nullable=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column(
            "time_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("time_last_activity", sa.DateTime(timezone=True), nullable=True),
        sa.Column("time_last_login", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("header", sa.String(), nullable=True),
        sa.Column("content", sa.String(), nullable=True),
        sa.Column(
            "time_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_post_id"), "post", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_post_id"), table_name="post")
    op.drop_table("post")
    op.drop_table("user")
    # ### end Alembic commands ###
