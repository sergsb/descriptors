import rdkit
from e3fp.pipeline import fprints_from_smiles
from mordred import Calculator, descriptors
from rdkit import Chem
import numpy as np
from rdkit.Chem.rdMolDescriptors import GetMorganFingerprintAsBitVect
from rdkit.DataStructs.cDataStructs import ConvertToNumpyArray

morded_calculator = Calculator(descriptors, ignore_3D=False)

fprint_params = {'bits': 4096, 'radius_multiplier': 1.5, 'rdkit_invariants': True}
confgen_params = {'max_energy_diff': 20.0, 'first': 10}

def ecfp( mol, r=3, nBits=4096, errors_as_zeros=True):
    mol = Chem.MolFromSmiles(mol) if not isinstance(mol, rdkit.Chem.rdchem.Mol) else mol
    try:
        arr = np.zeros((1,))
        ConvertToNumpyArray(GetMorganFingerprintAsBitVect(mol, r, nBits), arr)
        return arr.astype(np.float32)
    except:
        return np.NaN if not errors_as_zeros else np.zeros((nBits,), dtype=np.float32)

def e3fp(smiles): return np.vstack([fp.to_vector(sparse=False).astype(np.float32) for fp in fprints_from_smiles(smiles,smiles,confgen_params,fprint_params)])
def mordred(smiles): return np.array([list(morded_calculator(Chem.MolFromSmiles(smiles))
                                      .fill_missing(value=0.)
                                      .values())])\
    .astype(np.float32)

def get_avaliable_descriptors(): return {'morded':mordred,'ecfp':ecfp,'e3fp':e3fp}
