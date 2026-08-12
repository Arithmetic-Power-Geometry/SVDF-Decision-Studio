import sys,pathlib,pandas as pd
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'python'))
from svdf_engine import analyze,score_projects,specification_robustness

def load(name):return pd.read_csv(ROOT/'samples'/name)

def test_general_sample_runs():
    out=analyze(load('university_energy.csv'),n_draws=100,seed=2026,budget=10000000)
    assert out['n_projects']==5 and out['n_frontier']>=1
    assert all(0<=r['shared_value_gain']<=1 and 0<=r['implementation_complexity']<=1 for r in out['scored'])

def test_frontier_definition():
    df=pd.DataFrame([
      {'project_id':'A','project_name':'A','economic_value':10,'environmental_value':10,'stakeholder_reach':10,'implementation_burden':1,'scale':1,'volatility':1},
      {'project_id':'B','project_name':'B','economic_value':1,'environmental_value':1,'stakeholder_reach':1,'implementation_burden':10,'scale':10,'volatility':10},
      {'project_id':'C','project_name':'C','economic_value':8,'environmental_value':8,'stakeholder_reach':8,'implementation_burden':5,'scale':5,'volatility':5},])
    r=score_projects(df)
    assert bool(r.loc[r.project_id=='A','frontier'].iloc[0]) is True
    assert bool(r.loc[r.project_id=='B','frontier'].iloc[0]) is False

def test_paper_reproduction_frontier():
    out=analyze(load('paper_reproduction.csv'),n_draws=2000,seed=2026)
    assert out['frontier_ids']==['U06','U05','U04']
    by={r['project_id']:r for r in out['scored']}
    assert round(by['U06']['shared_value_gain'],3)==0.048
    assert round(by['U06']['implementation_complexity'],3)==0.233
    assert round(by['U06']['frontier_frequency']*100,1)==100.0
    assert abs(by['U04']['frontier_frequency']-0.8455)<1e-12
    assert abs(by['U05']['frontier_frequency']-0.7535)<1e-12
