import tqdm
import numpy as np
import pandas as pd
from datetime import datetime
import pandas_datareader as pdr

from ta.momentum import AwesomeOscillatorIndicator, KAMAIndicator, PercentagePriceOscillator, PercentageVolumeOscillator, ROCIndicator
from ta.momentum import RSIIndicator, StochRSIIndicator, StochasticOscillator, TSIIndicator, UltimateOscillator, WilliamsRIndicator
from ta.volume import AccDistIndexIndicator, ChaikinMoneyFlowIndicator, EaseOfMovementIndicator, MFIIndicator
from ta.volume import NegativeVolumeIndexIndicator, OnBalanceVolumeIndicator, VolumePriceTrendIndicator
from ta.volatility import AverageTrueRange, BollingerBands, DonchianChannel, KeltnerChannel, UlcerIndex
from ta.trend import ADXIndicator, EMAIndicator, MACD, MassIndex, PSARIndicator, STCIndicator, TRIXIndicator, WMAIndicator, VortexIndicator
from ta.others import CumulativeReturnIndicator, DailyLogReturnIndicator, DailyReturnIndicator

class FeatureEngineer():

	# add new features
	def build_technical_indicators(df):
	    df['open_sub_close'] = df['Open'] - df['Close']
	    df['high_div_low'] = df['High'] / df['Low']
	    
	    # MA8, 21, 50, 200 - volume
	    df['ma8_vol'] = df['Volume'].rolling(8).mean()
	    df['ma21_vol'] = df['Volume'].rolling(21).mean()
	    df['ma50_vol'] = df['Volume'].rolling(50).mean()
	    df['ma200_vol'] = df['Volume'].rolling(200).mean()
	    
	    # momentum indicators
	    moment_aoi = AwesomeOscillatorIndicator(df['High'], df['Low'])
	    df['AO'] = moment_aoi.awesome_oscillator()
	    
	    moment_kama = KAMAIndicator(df['Close']) # Kaufman's Adaptive Moving Average
	    df['KAMA'] = moment_kama.kama()
	    
	    moment_ppo = PercentagePriceOscillator(df['Close'])
	    df['PPO'], df['PPO_signal'] = moment_ppo.ppo(), moment_ppo.ppo_signal()
	    
	    moment_pvo = PercentageVolumeOscillator(df['Volume'])
	    df['PVO'], df['PVO_signal'] = moment_pvo.pvo(), moment_pvo.pvo_signal()
	    
	    moment_roc = ROCIndicator(df['Close']) # Rate of Change
	    df['ROC'] = moment_roc.roc()
	    
	    moment_rsi = RSIIndicator(df['Close']) # Relative Strength Index
	    df['RSI'] = moment_rsi.rsi()
	    
	    moment_rsi_ = StochRSIIndicator(df['Close'])
	    df['RSI_stoch'] = moment_rsi_.stochrsi()
	    df['RSI_stoch_d'] = moment_rsi_.stochrsi_d()
	    df['RSI_stoch_k'] = moment_rsi_.stochrsi_k()
	    
	    moment_stoch = StochasticOscillator(df['Close'], df['High'], df['Low'])
	    df['stoch'], df['stoch_signal'] = moment_stoch.stoch(), moment_stoch.stoch_signal()
	    
	    moment_tsi = TSIIndicator(df['Close']) # True Strength Index
	    df['TSI'] = moment_tsi.tsi()
	    
	    moment_ult = UltimateOscillator(df['High'], df['Low'], df['Close'])
	    df['ult'] = moment_ult.ultimate_oscillator()
	    
	    moment_wri = WilliamsRIndicator(df['High'], df['Low'], df['Close']) # Williams %R
	    df['WRI'] = moment_wri.williams_r()
	     
	    # volume indicators
	    vol_adi = AccDistIndexIndicator(df['High'], df['Low'], df['Close'], df['Volume']) # Accumulation/Distribution Index
	    df['ADI'] = vol_adi.acc_dist_index()
	    
	    vol_cmf = ChaikinMoneyFlowIndicator(df['High'], df['Low'], df['Close'], df['Volume'])
	    df['CMF'] = vol_cmf.chaikin_money_flow()
	    
	    vol_eom = EaseOfMovementIndicator(df['High'], df['Low'], df['Volume'])
	    df['EoM'], df['EoM_signal'] = vol_eom.ease_of_movement(), vol_eom.sma_ease_of_movement()
	    
	    vol_mfi = MFIIndicator(df['High'], df['Low'], df['Close'], df['Volume']) # Money Flow Index
	    df['MFI'] = vol_mfi.money_flow_index()
	    
	    vol_nvi = NegativeVolumeIndexIndicator(df['Close'], df['Volume'])
	    df['NVI'] = vol_nvi.negative_volume_index()
	    
	    vol_obv = OnBalanceVolumeIndicator(df['Close'], df['Volume'])
	    df['OBV'] = vol_obv.on_balance_volume()
	    
	    vol_vpt = VolumePriceTrendIndicator(df['Close'], df['Volume'])
	    df['VPT'] = vol_vpt.volume_price_trend()
	    
	    # volatility indicators
	    vola_atr = AverageTrueRange(df['High'], df['Low'], df['Close'])
	    df['ATR'] = vola_atr.average_true_range()
	    
	    vola_boll = BollingerBands(df['Close'])
	    df['BOLL+'] = vola_boll.bollinger_hband()
	    df['BOLL-'] = vola_boll.bollinger_lband()
	    df['BOLL_mid'] = vola_boll.bollinger_mavg()
	    df['BOLL_percent'] = vola_boll.bollinger_pband()
	    df['BOLL_width'] = vola_boll.bollinger_wband()
	    
	    vola_dc = DonchianChannel(df['High'], df['Low'], df['Close'])
	    df['DC+'] = vola_dc.donchian_channel_hband()
	    df['DC-'] = vola_dc.donchian_channel_lband()
	    df['DC_mid'] = vola_dc.donchian_channel_mband()
	    df['DC_percent'] = vola_dc.donchian_channel_pband()
	    df['DC_width'] = vola_dc.donchian_channel_wband()
	    
	    vola_kc = KeltnerChannel(df['High'], df['Low'], df['Close'])
	    df['KC+'] = vola_kc.keltner_channel_hband()
	    df['KC-'] = vola_kc.keltner_channel_lband()
	    df['KC_mid'] = vola_kc.keltner_channel_mband()
	    df['KC_percent'] = vola_kc.keltner_channel_pband()
	    df['KC_width'] = vola_kc.keltner_channel_wband()  
	    
	    vola_ui = UlcerIndex(df['Close'])
	    df['Ulcer'] = vola_ui.ulcer_index()
	     
	    # trend indicators
	    trend_adx = ADXIndicator(df['High'], df['Low'], df['Close']) 
	    df['ADX'], df['ADX+'], df['ADX-'] = trend_adx.adx(), trend_adx.adx_pos(), trend_adx.adx_neg()
	    
	    df['ema7_price'] = EMAIndicator(df['Close'], 7).ema_indicator() # EMA7
	    df['ema21_price'] = EMAIndicator(df['Close'], 21).ema_indicator() # EMA21
	    df['ema50_price'] = EMAIndicator(df['Close'], 50).ema_indicator() # EMA50
	    df['ema200_price'] = EMAIndicator(df['Close'], 200).ema_indicator() # EMA200
	    
	    trend_macd = MACD(df['Close']) # MACD
	    df['MACD'], df['MACD_signal'] = trend_macd.macd(), trend_macd.macd_signal()
	    
	    trend_mass_index = MassIndex(df['High'], df['Low']) 
	    df['MI'] = trend_mass_index.mass_index()
	    
	    trend_psar = PSARIndicator(df['High'], df['Low'], df['Close']) # Parabolic Stop and Reverse 
	    df['PSAR'], df['PSAR+'], df['PSAR-'] = trend_psar.psar(), trend_psar.psar_up(), trend_psar.psar_down()
	    
	    trend_stc = STCIndicator(df['Close']) # Schaff Trend Cycle
	    df['STC'] = trend_stc.stc()
	    
	    trend_trix = TRIXIndicator(df['Close']) # Trix
	    df['TRIX'] = trend_trix.trix()
	    
	    trend_vi = VortexIndicator(df['High'], df['Low'], df['Close'])
	    df['VI'] = trend_vi.vortex_indicator_diff()
	    df['VI+'] = trend_vi.vortex_indicator_pos()
	    df['VI-'] = trend_vi.vortex_indicator_neg()
	    
	    trend_wma = WMAIndicator(df['Close']) # Weighted Moving Average
	    df['WMA'] = trend_wma.wma()
	    
	    # others indicators
	    other_cr = CumulativeReturnIndicator(df['Close'])
	    df['CR'] = other_cr.cumulative_return()
	    
	    other_dlr = DailyLogReturnIndicator(df['Close'])
	    df['DLR'] = other_dlr.daily_log_return()
	    
	    other_dr = DailyReturnIndicator(df['Close'])
	    df['DR'] = other_dr.daily_return()
		    
		return df



	# external data
	def import_external_data():
    	
    	data = []

	    # commodity
	    gc = pdr.get_data_yahoo('GC=F', start, end) # gold
	    sil = pdr.get_data_yahoo('SI=F', start, end) # silver
	    oil = pdr.get_data_yahoo('CL=F', start, end) # crude oil
	    
	    # dollar and bond
	    dollar = pdr.get_data_yahoo('EURUSD=X', start, end) # EUR/USD
	    bond = pdr.get_data_yahoo('^TNX', start, end) # 10-year treasury bond
	    
	    # futures 22
	    wheat = pdr.get_data_yahoo('ZWH22.CBT', start, end) # wheat
	    corn = pdr.get_data_yahoo('ZCH22.CBT', start, end) # corn
	    soy = pdr.get_data_yahoo('ZSH22.CBT', start, end) # soybean
	    oat = pdr.get_data_yahoo('ZOH22.CBT', start, end) # oat
	    usd = pdr.get_data_yahoo('DXH22.NYB', start, end) # USD
	    
	    # stock market
	    spy = pdr.get_data_yahoo('SPY', start, end) # SPY
	    dia = pdr.get_data_yahoo('DIA', start, end) # DIA
	    qqq = pdr.get_data_yahoo('QQQ', start, end) # QQQ
	    iwm = pdr.get_data_yahoo('IWM', start, end) # russell
	    vix = pdr.get_data_yahoo('^VIX', start, end) # VIX
    	bkch = pdr.get_data_yahoo('BKCH', start, end) # blockchain etf

    	return df