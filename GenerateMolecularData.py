import psi4

Mol = psi4.geometry("""
    O            0.000000000000     0.000000000000     0.000000000000
    H            0.700000000000     0.000000000000     -0.700000000000
    H            -0.700000000000     0.000000000000     -0.700000000000
  symmetry c1
""")

e,wfna = psi4.optimize('B3LYP/cc-pVDZ',return_wfn = True)

e,wfnb = psi4.driver.frequencies('B3LYP/cc-pVDZ',return_wfn = True)

M = wfnb.frequency_analysis['x'].data.T[6:]

Data = { 
         "Atoms"  : Mol.to_arrays()[3],
         "Coords" : Mol.to_arrays()[0],
         "Frequencies"  : wfnb.frequencies().to_array(),   
         "Modes"  : M.reshape(len(M),-1,3)
}

pickle.dump(Data,open("molecule_data.pkl","wb"))
