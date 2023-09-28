from pydantic import BaseModel


class ConfigSchema(BaseModel):
    config_samples_per_packet: int
    class_map: dict
    model_json: dict
    loop: bool
    data_type: str = "int16"
    sml_library_path: str = None
    run_sml_model: bool = False
    convert_to_int16: bool = False
    scaling_factor: float = 1.0
    device_id: str
    sample_rate: float
    config_columns: dict

    class Config:
        from_attributes = True  # Allows using this Pydantic model with ORMs like SQLAlchemy
