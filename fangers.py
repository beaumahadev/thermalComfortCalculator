import math

#Fanger's Predicted Mean Vote model

#Input:
    #ta- air temperature (degrees C)
    #rh- relative humidity (%)
    #met- metabolic rate 
    #clo- clothing index 
#Output:
    #pmv: predicted mean vote
    #ppd: percent predicted dissatisfied 

def calculate(ta, rh, met, clo):

    #assume the air is still
    vel=0.1

    #assume no external work
    wme=0

    #assume radiant temp same as ambient temp
    tr=ta

    pa = rh * 10 * math.exp(16.6536 - 4030.183 / (ta + 235))
    icl = 0.155 * clo #thermal insulation of the clothing in M2K/W
    m = met * 58.15 #metabolic rate in W/M2
    w = wme * 58.15 #external work in W/M2
    mw = m - w #internal heat production in the human body
    if icl <= 0.078:
        fcl = 1 + (1.29 * icl)
    else:
        fcl = 1.05 + (0.645 * icl)

    #heat transf. coeff. by forced convection
    hcf = 12.1 * math.sqrt(vel)
    taa = ta + 273
    tra = tr + 273
    tcla = taa + (35.5 - ta) / (3.5 * icl + 0.1)


    p1 = icl * fcl
    p2 = p1 * 3.96
    p3 = p1 * 100
    p4 = p1 * taa
    p5 = 308.7 - 0.028 * mw + p2 * pow(tra / 100, 4)
    xn = tcla / 100
    xf = tcla / 50
    eps = 0.00015

    n = 0

    while (abs(xn - xf) > eps):
        xf = (xf + xn) / 2
        hcn = 2.38 * pow(abs(100.0 * xf - taa), 0.25)
        if hcf > hcn:
             hc = hcf
        else:
            hc = hcn
        xn = (p5 + p4 * hc - p2 * pow(xf, 4)) / (100 + p3 * hc)
        n+=n
        if n > 150:
            print('Max iterations exceeded')
            return(1)

    tcl = 100 * xn - 273

    #heat loss diff. through skin
    hl1 = 3.05 * 0.001 * (5733 - (6.99 * mw) - pa)
    #heat loss by sweating
    if mw > 58.15:
        hl2 = 0.42 * (mw - 58.15)
    else:
        hl2 = 0
    #latent respiration heat loss
    hl3 = 1.7 * 0.00001 * m * (5867 - pa)
    #dry respiration heat loss
    hl4 = 0.0014 * m * (34 - ta)
    #heat loss by radiation
    hl5 = 3.96 * fcl * (pow(xn, 4) - pow(tra / 100, 4))
    #heat loss by convection
    hl6 = fcl * hc * (tcl - ta)

    ts = 0.303 * math.exp(-0.036 * m) + 0.028
    pmv = ts * (mw - hl1 - hl2 - hl3 - hl4 - hl5 - hl6)
    ppd = 100.0 - 95.0 * math.exp(-0.03353 * pow(pmv, 4.0) - 0.2179 * pow(pmv, 2.0))

    if pmv > -.2 and pmv < .2:
        comfort="neutral"
    elif pmv > .2 and pmv < .5:
        comfort="warm"
    elif pmv < -.2 and pmv > -.5:
        comfort="cool"
    elif pmv > .5:
        comfort="hot"
    elif pmv < -.5:
        comfort="cold"

    r = {"pmv":pmv,"ppd":ppd,"comfort":comfort}
    return(r)


