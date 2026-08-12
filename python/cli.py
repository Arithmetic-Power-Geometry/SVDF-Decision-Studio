import argparse,pandas as pd,json,pathlib
from svdf_engine import analyze

def main():
    ap=argparse.ArgumentParser(description='SVDF Decision Studio CLI')
    ap.add_argument('csv');ap.add_argument('--draws',type=int,default=2000);ap.add_argument('--seed',type=int,default=2026);ap.add_argument('--budget',type=float);ap.add_argument('--out',default='outputs/analysis.json')
    a=ap.parse_args();df=pd.read_csv(a.csv);r=analyze(df,a.draws,a.seed,a.budget);o=pathlib.Path(a.out);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(r,indent=2,default=str))
    print(f"Projects: {r['n_projects']} | Frontier: {r['n_frontier']} | IDs: {', '.join(map(str,r['frontier_ids']))}")
if __name__=='__main__':main()
