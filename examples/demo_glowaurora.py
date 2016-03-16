#!/usr/bin/env python3
"""
default parameter values like those of Stan's fortran examples--yield rather similar output

Note, this simulation uses a specific input differential number flux spectrum
"""
from dateutil.parser import parse
from matplotlib.pyplot import show
#
from glowaurora.runglow import runglowaurora,plotaurora

def E0aurora(t0,glatlon,flux,e0,f107a,f107,f107p,ap,makeplot):

    (glat,glon) = glatlon

    ver,photIon,isr,phitop,zceta,sza,prate,lrate,tez,sion = runglowaurora(flux,e0,
                                                                 t0,glat,glon,
                                                                 f107a,f107,f107p,ap)

    plotaurora(phitop,ver,zceta,photIon,isr,sion,t0,glat,glon,prate,lrate,makeplot=makeplot)

    return ver,photIon,isr,phitop,zceta,sza

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description="Stan Solomon's GLOW auroral model")
    p.add_argument('simtime',help='yyyy-mm-ddTHH:MM:SSZ time of sim',nargs='?',default='1999-12-21T00:00:00Z')
    p.add_argument('-c','--latlon',help='geodetic latitude/longitude (deg)',type=float,nargs=2,default=(70,0))
#    p.add_argument('-n','--nbins',help='number of energy bins in incident diff num flux',type=int,default=190) #hard-coded in cglow.h
    p.add_argument('--flux',help='overall incident flux [erg ...]',type=float,default=1.)
    p.add_argument('--e0',help='characteristic energy [eV]',type=float,default=1e3)
    p.add_argument('--f107a',help='AVERAGE OF F10.7 FLUX',type=float,default=100)
    p.add_argument('--f107p',help='DAILY F10.7 FLUX FOR PREVIOUS DAY',type=float,default=100)
    p.add_argument('--f107',help='F10.7 for sim. day',type=float,default=100)
    p.add_argument('--ap',help='daily ap',type=float,default=4)
    p.add_argument('-m','--makeplot',help='show to show plots, png to save pngs of plots',nargs='+',default=['show'])
    p = p.parse_args()

    t0 = parse(p.simtime)

    ver,photIon,isr,phitop,zceta,sza = E0aurora(t0,p.latlon,p.flux,p.e0,p.f107a,p.f107,p.f107p,p.ap,p.makeplot)

    show()
