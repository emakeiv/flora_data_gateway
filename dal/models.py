from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    JSON
)

Base = declarative_base()


class Config(Base):

    __tablename__ = "configs"

    id = Column(Integer, primary_key=True, index=True)
    config_samples_per_packet = Column(Integer)
    class_map = Column(JSON)
    model_json = Column(JSON)
    loop = Column(Boolean)
    data_type = Column(String, default="int16")
    sml_library_path = Column(String)
    run_sml_model = Column(Boolean, default=False)
    convert_to_int16 = Column(Boolean, default=False)
    scaling_factor = Column(Float, default=1.0)
    device_id = Column(String, unique=True, index=True)
    sample_rate = Column(Float)
    config_columns = Column(JSON)
