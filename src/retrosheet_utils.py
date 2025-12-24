import numpy as np
import pandas as pd

#source - https://github.com/beanumber/abdwr3edata/blob/main/R/retrosheet.R

def retrosheet_add_states(df):
    # Create bases code: 3-digit string indicating which bases are occupied
    df['bases'] = (
        np.where(df['base1_run_id'].notna() & (df['base1_run_id'] != ''), '1', '0') +
        np.where(df['base2_run_id'].notna() & (df['base2_run_id'] != ''), '1', '0') +
        np.where(df['base3_run_id'].notna() & (df['base3_run_id'] != ''), '1', '0')
    )
    
    # Combine bases and outs to create game state
    df['state'] = df['bases'] + ' ' + df['outs_ct'].astype(str)
    
    # Determine which bases are occupied after each play
    df['is_runner1'] = (
        (df['run1_dest_id'] == 1) | (df['bat_dest_id'] == 1)
    ).astype(int)
    
    df['is_runner2'] = (
        (df['run1_dest_id'] == 2) | 
        (df['run2_dest_id'] == 2) | 
        (df['bat_dest_id'] == 2)
    ).astype(int)
    
    df['is_runner3'] = (
        (df['run1_dest_id'] == 3) | 
        (df['run2_dest_id'] == 3) |
        (df['run3_dest_id'] == 3) | 
        (df['bat_dest_id'] == 3)
    ).astype(int)
    
    # Calculate outs and bases after the play
    df['new_outs'] = df['outs_ct'] + df['event_outs_ct']
    
    # Create new bases code and state after the play
    df['new_bases'] = (
        df['is_runner1'].astype(str) +
        df['is_runner2'].astype(str) +
        df['is_runner3'].astype(str)
    )
    
    df['new_state'] = df['new_bases'] + ' ' + df['new_outs'].astype(str)
    
    # Calculate runs scored on each play
    df['runs_scored'] = (
        (df['bat_dest_id'] > 3).astype(int) + 
        (df['run1_dest_id'] > 3).astype(int) + 
        (df['run2_dest_id'] > 3).astype(int) + 
        (df['run3_dest_id'] > 3).astype(int)
    )
    
    return df

def retrosheet_add_counts(df):
    b = "[BIPV]"  # Ball patterns
    s = "[CFKLMOQRST]"  # Strike patterns
    
    df['c00'] = True  # All PAs start at 0-0
    df['c10'] = df['pseq'].str.contains(f'^{b}')
    df['c01'] = df['pseq'].str.contains(f'^{s}')
    df['c20'] = df['pseq'].str.contains(f'^{b}{{2}}')
    df['c30'] = df['pseq'].str.contains(f'^{b}{{3}}')
    df['c02'] = df['pseq'].str.contains(f'^{s}{{2}}')
    df['c11'] = df['pseq'].str.contains(f'^{s}{b}|^{b}{s}')
    df['c21'] = df['pseq'].str.contains(f'^{s}{b}{b}|^{b}{s}{b}|^{b}{b}{s}')
    df['c31'] = df['pseq'].str.contains(f'^{s}{b}{b}{b}|^{b}{s}{b}{b}|^{b}{b}{s}{b}|^{b}{b}{b}{s}')
    df['c12'] = df['pseq'].str.contains(f'^{b}{s}{s}|^{s}{b}{s}|^{s}{s}[FR]*{b}')
    df['c22'] = df['pseq'].str.contains(f'^{b}{b}{s}{s}|^{b}{s}{b}{s}|^{b}{s}{s}[FR]*{b}|^{s}{b}{b}{s}|^{s}{b}{s}[FR]*{b}|^{s}{s}[FR]*{b}[FR]*{b}')
    df['c32'] = df['pseq'].str.contains(f'^{s}*{b}{s}*{b}{s}*{b}') & df['pseq'].str.contains(f'^{b}*{s}{b}*{s}')
    
    return df

