import numpy as np
import pandas as pd
import pytest
from mllab.delivery_j56 import validate_rows,align_submission

CONTRACT={'columns':['amount','foreign','device'],'numeric':['amount'],'boolean':['foreign']}

def test_valid_null_and_boolean():
 frame=validate_rows([{'amount':None,'foreign':True,'device':'mobile'}],CONTRACT)
 assert frame.shape==(1,3) and pd.isna(frame.amount.iloc[0])

@pytest.mark.parametrize('row',[
 {'amount':1,'foreign':True},
 {'amount':1,'foreign':True,'device':'mobile','extra':2},
 {'amount':'beaucoup','foreign':True,'device':'mobile'},
 {'amount':float('inf'),'foreign':True,'device':'mobile'},
 {'amount':1,'foreign':'True','device':'mobile'},
])
def test_reject_invalid_contract(row):
 with pytest.raises(ValueError):validate_rows([row],CONTRACT)

def test_realign_by_id_instead_of_row_order():
 sample=pd.DataFrame({'id':[18,12,27],'is_fraud':[0,0,0]})
 predictions=pd.DataFrame({'id':[12,18,27],'is_fraud':[.9,.1,.3]})
 result=align_submission(sample,predictions)
 assert result.id.tolist()==[18,12,27] and np.allclose(result.is_fraud,[.1,.9,.3])

@pytest.mark.parametrize('ids,probas',[([18,18,27],[.1,.2,.3]),([18,12],[.1,.2]),([18,12,28],[.1,.2,.3]),([18,12,27],[.1,np.nan,.3])])
def test_reject_invalid_submission(ids,probas):
 sample=pd.DataFrame({'id':[18,12,27],'is_fraud':[0,0,0]})
 with pytest.raises(ValueError):align_submission(sample,pd.DataFrame({'id':ids,'is_fraud':probas}))
