# This is the script for final figure with best-fit
# run with:
# $ python solike/ymap/run_scripts/marginalized_tsz_from_TS+P18CM_analysis.py
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt





path_to_files = '/Users/boris/Work/CLASS-SZ/SO-SZ/TopoSZ/fig12 data/'



def run(args):

    D = np.loadtxt(path_to_files+'szpowespectrum_measurement_urc_snr6_p18cmb_bf_fg_from_TSZ+P18_l_clyy_sigclyy_cib_ir_rs_cn.txt')
    multipoles = D[:,0]
    marg_sz = D[:,1]
    marg_sz_yerr = D[:,2]
    Cl_cib =  D[:,3]
    Cl_ir = D[:,4]
    Cl_rs = D[:,5]
    Cl_cn =  D[:,6]



    R = np.loadtxt(path_to_files + 'szpowespectrum_measurement_urc_snr6_p18cmb_best_fit_curve_l_cl1h_cl2h_cl1h+2h.txt')
    multipoles_bf = R[:,0]
    cl_1h = R[:,1]
    cl_2h = R[:,2]

    label_size = 12
    title_size = 15
    legend_size = 13
    handle_length = 2
    y_min = 5.e-4
    y_max = 4
    fig, ax1 = plt.subplots(1,1,figsize=(7,5))

    ax = ax1
    ax.tick_params(axis = 'x',which='both',length=5,direction='in', pad=10)
    ax.tick_params(axis = 'y',which='both',length=5,direction='in', pad=5)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    plt.setp(ax.get_yticklabels(), rotation='horizontal', fontsize=label_size)
    plt.setp(ax.get_xticklabels(), fontsize=label_size)
    ax.grid( b=True, which="both", alpha=0.3, linestyle='--')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'$\ell$',size=title_size)

    ax.set_ylabel(r'$10^{12}\ell(\ell+1)\mathrm{C^{yy}_\ell/2\pi}$',size=title_size)




    ax.plot(multipoles_bf,cl_1h,color='k',ls='--',lw=2,alpha = 1.)
    ax.plot(multipoles_bf,cl_2h,color='k',ls='-.',lw=2,alpha = 1.)
    ax.plot(multipoles_bf,cl_1h+cl_2h,color='r',ls='-',lw=2,alpha = 1.)
    ax.plot(multipoles,Cl_cib,color='b',ls='--',alpha = .5)
    ir, = ax.plot(multipoles,Cl_ir,color='orange',ls='-.',alpha = .8)
    ir.set_dashes([4, 2, 1, 2, 1, 2, 1, 2])
    ax.plot(multipoles,Cl_rs,color='b',ls=':',alpha = .5)
    cn, = ax.plot(multipoles,Cl_cn,color='b',ls=':',alpha = .7)
    cn.set_dashes([4, 2, 1, 2, 1, 2])
    ax.errorbar(multipoles,marg_sz,yerr=[marg_sz_yerr,marg_sz_yerr],color='k',ls='None',alpha = 1.,label = r'Marginalized TSZ [uRC, $q_\mathrm{cut}=6$]',marker='o',markersize=3,capsize=5,elinewidth=2,markeredgewidth=2)



    ACTCellnew = 5.29/(2.67)**2
    ACTCellnewerr =	0.66/(2.67)**2

    SPTCellnew = 3.42/(2.84)**2
    SPTCellnewerr = 0.54/(2.84)**2

    ax.errorbar([3000],[SPTCellnew],
                yerr=[SPTCellnewerr],capthick=1,capsize=3,elinewidth=1,\
                 fmt='>',mfc='k',markersize=8,color = 'r')

    ax.errorbar([3000],[ACTCellnew],
                yerr=[ACTCellnewerr],capthick=1,capsize=3,elinewidth=2,\
                 fmt='<',mfc='k',markersize=8,color = 'r',zorder=100)
    ax.text(3.9e3, 4.2e-1, 'SPT (2020)', fontsize=9,rotation = 0,
    verticalalignment='center',horizontalalignment='left')
    ax.text(3.9e3, 7e-1, 'ACT (2020)', fontsize=9,rotation = 0,
    verticalalignment='center',horizontalalignment='left')



    P = np.loadtxt(path_to_files+'planck_sz_1712_00788v1.txt')
    ax.errorbar(P[:,0][0:18],P[:,1][0:18],yerr = P[:,2][0:18],color='green',linestyle="None",alpha = .2,label = 'B18',marker='o',markersize=3,capsize=5,elinewidth=2,markeredgewidth=2)
    ax.fill_between(P[:,0][0:18],P[:,1][0:18]-P[:,2][0:18],P[:,1][0:18]+P[:,2][0:18],
    color='green',alpha=0.1,label=r'1-$\sigma$ interval from Bolliet et al. (2018)')
    ax.set_ylim(y_min,y_max)
    ax.legend(loc=2,ncol=1,fontsize=10,frameon=False)

    plt.xlim(8,1.1e4)



    ax.text(1.1e2, 2.4e-2, '1-halo', fontsize=11,rotation = 45,
    verticalalignment='bottom',horizontalalignment='left')
    ax.text(2e3, 6.5e-3, '2-halo', fontsize=11,rotation = -30,
    verticalalignment='bottom',horizontalalignment='left')
    ax.text(1.e3, 1.2, 'BEST-FIT TSZ', fontsize=9,rotation = 18,
    verticalalignment='bottom',horizontalalignment='left')
    fig.tight_layout()

    ax.text(3.e2, 7e-2, 'IR Res.', fontsize=9,rotation = 58,
    verticalalignment='center',horizontalalignment='left')

    ax.text(4.7e2, 5e-3, 'Noise Res.', fontsize=9,rotation = 58,
    verticalalignment='center',horizontalalignment='left')

    ax.text(1e3, 4e-2, 'Radio Res.', fontsize=9,rotation = 0,
    verticalalignment='center',horizontalalignment='left')
    ax.text(1e3, 3.5e-3, 'CIB Res.', fontsize=9,rotation = 0,
    verticalalignment='center',horizontalalignment='left')
    fig.tight_layout()

    plt.savefig(path_to_files+'my_marginalized_tsz_fig.pdf')
    plt.show(block=True)


def main():
    parser=argparse.ArgumentParser(description="plotting results")
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()
