from pathlib import Path

import yfinance as yf
from yfinance import cache


def configure_yfinance_cache():
    cache_dir = Path(__file__).resolve().parents[2] / ".yfinance-cache"
    cache_dir.mkdir(exist_ok=True)
    cache.set_cache_location(str(cache_dir))
    yf.set_tz_cache_location(str(cache_dir))
