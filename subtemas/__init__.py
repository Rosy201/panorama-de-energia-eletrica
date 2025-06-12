from .consumo_temporal import layout as layout_consumo_temporal, register_callbacks as register_consumo_temporal
from .consumo_por_setor import layout as layout_setor, register_callbacks as register_setor

__all__ = [
    "layout_consumo_temporal",
    "register_consumo_temporal",
    "layout_setor",
    "register_setor",
]
