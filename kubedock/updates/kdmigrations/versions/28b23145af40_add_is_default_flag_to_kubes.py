"""Add 'is_default' flag to kube types model

Revision ID: 28b23145af40
Revises: 56f9182bf415
Create Date: 2015-11-04 15:15:29.561256

"""

# revision identifiers, used by Alembic.
revision = '28b23145af40'
down_revision = '56f9182bf415'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session = sessionmaker()
Base = declarative_base()

class Kube(Base):
    __tablename__ = 'kubes'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    is_default = sa.Column(sa.Boolean, default=None, nullable=True, unique=True)


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kubes', sa.Column('is_default', sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, 'kubes', ['is_default'])
    ### end Alembic commands ###
    kube = session.query(Kube).filter(Kube.id >= 0).order_by(Kube.id).first()
    if kube is not None:
        kube.is_default = True
        session.commit()


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('kubes_is_default_key', 'kubes', type_='unique')
    op.drop_column('kubes', 'is_default')
    ### end Alembic commands ###
