from .consumo_temporal import layout as layout_consumo_temporal, register_callbacks as register_consumo_temporal
from .consumo_por_setor import layout as layout_setor, register_callbacks as register_setor
from .geracao_por_fonte import layout as layout_geracao, register_callbacks as register_geracao

__all__ = [
    "layout_consumo_temporal", "register_consumo_temporal",
    "layout_setor", "register_setor",
    "layout_geracao", "register_geracao"
]

