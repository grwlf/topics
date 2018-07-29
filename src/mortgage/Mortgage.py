import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Tuple,List,Dict
from math import log


def mort_time(C:float=10e6, p:float=0.1, d:float=12*30e3)->Tuple[float,float]:
  """ Assume fixed mortgage payments are made every year. Part of them goes to
  debt maintanance, part to the reduce the amount of debt.

  `C` - Mortgage capital to be returned eventually
  `p` - Interest to be paid annualy
  `d` - initial payment above debt maintainence

  Return a tuple of:
   - Number of years to pay the mortgage
   - Total annual payment
  """
  return (log(C*p/d+1) / log(1+p), d+C*p)

def mort_capital(t:float, p:float, m:float)->float:
  """ Return capital refunded if use mortgage during time `t`,
  with interes rate `p` and annual payments `m` """
  S=((1+p)**t - 1)/p
  return m*S/(1+p*S)

def _mort_iter(C:float=10e6, p:float=0.1, d:float=12*30e3)->Tuple[float,float]:
  """ Same as `mort_time`, but works iteratively """
  s=0;Ci=C;di=d;i=0
  while(Ci>0):
     print(i, 'Ci', Ci, 'Ci_next',  C - d*(sum([(1+p)**ii for ii in range(0,i)])) , 'di', di, 'di_t', d*(1+p)**i, Ci*p + di)
     Ci=Ci-di
     di=di*(1+p)
     i+=1
  return i,C*p+d

def deposit(apay=100, p=0.05, t:int=10)->float:
  """ Deposit `apay` every year, for a period of `t` years.
  Return the total amount of money. """
  return apay*(p+1)*(1-(p+1)**t)/ (-p)

def hide(apay=100, t:int=10):
  """ Hide `apay` every year, for `t` years,
  Return total amount of money """
  return apay*t

def savings(apay_actual=12*30e3, pdep=0.05, **kwargs):
  """ Return savings compared with mortgage, calculated as if actual annual
  payment is `apay`, and money are kept on the deposit with annual percent `pdep` """
  years,apay_mort=mort_time(**kwargs)
  sav=(apay_mort-apay_actual)
  return deposit(apay=sav,t=years)

def rent_max(p:float, pd:float, m:float, t:float)->float:
  """ Maximum rent to keep the saved capital above-mortgage level """
  C=mort_capital(t,p,m)
  return m-(pd*C)/((pd+1)*(((pd+1)**t)-1)),C

