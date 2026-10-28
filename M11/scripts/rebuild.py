"""Recalculate Case 31 metrics and figures from the supplied SPSS file."""
from pathlib import Path
import json
import pyreadstat
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root = Path(__file__).resolve().parents[1]
x, meta = pyreadstat.read_sav(str(root / 'data/Case 31 Data_efcu_Prepped.sav'))
assert ((x[['q3','q4','q5','q6']].mean(axis=1) - x.at_emp).abs() < 1e-9).all()
x.to_csv(root / 'data/case31.csv', index=False)
valid = x.q37.isin([1,2,3,4,5])
metrics = {'n':len(x), 'employee_mean':float(x.at_emp.mean()), 'overall_valid':int(valid.sum()), 'overall_missing':int((~valid).sum()), 'positive_count':int(x.q37.isin([1,2]).sum()), 'positive_percent':float(x.q37.isin([1,2]).sum()/valid.sum()*100), 'service_means':{c:float(x[c].mean()) for c in ['q3','q4','q5','q6']}, 'headquarters_employee_mean':{str(k):float(v) for k,v in x.groupby('q38').at_emp.mean().items()}}
(root/'data/metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#dae2e6','text.color':'#17333b','axes.labelcolor':'#17333b','xtick.color':'#4d646b','ytick.color':'#4d646b','figure.facecolor':'white','axes.facecolor':'white'})
def chart(name,labels,vals,maxv,xlabel):
    fig,ax=plt.subplots(figsize=(8,3.5))
    bars=ax.barh(labels,vals,color='#167d8d',height=.55)
    ax.invert_yaxis(); ax.set_xlim(0,maxv); ax.set_xlabel(xlabel)
    ax.grid(axis='x',alpha=.14); ax.set_axisbelow(True); ax.tick_params(axis='y',length=0)
    for b,v in zip(bars,vals):
        ax.text(v+maxv*.015,b.get_y()+b.get_height()/2,f'{v:.2f}' if maxv==5 else str(int(v)),va='center')
    fig.tight_layout(); fig.savefig(root/f'assets/{name}.svg'); plt.close(fig)
chart('service',['Courtesy','Helpfulness','Professionalism','Availability'],[x[c].mean() for c in ['q3','q4','q5','q6']],5,'Mean agreement (1 = strongly disagree; 5 = strongly agree)')
chart('overall',['Excellent','Good','Average','Poor','Very poor'],[int((x.q37==i).sum()) for i in range(1,6)],85,'Number of respondents (121 valid ratings)')
chart('groups',['Headquarters: yes (n = 57)','Headquarters: no (n = 71)'],[x.loc[x.q38==i,'at_emp'].mean() for i in [1,2]],5,'Mean employee service composite (1–5)')
print(json.dumps(metrics,indent=2))
