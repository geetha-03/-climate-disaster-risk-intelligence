from typing import TypedDict, Optional
import pandas as pd

class ClimateState(TypedDict):
    query: str
    region: str
    disaster_type: str
    
    raw_data: Optional[pd.DataFrame]
    yearly_counts: Optional[pd.DataFrame]
    
    trend_slope: Optional[float]
    p_value: Optional[float]

    mk_trend: Optional[str]
    mk_p_value: Optional[float]
    
    risk_level: Optional[str]
    interpretation: Optional[str]
    reflection_notes: Optional[str]

    plot_figure: Optional[object]

    t_stat: Optional[float]
    t_p_value: Optional[float]
    confidence_level: Optional[str]

    