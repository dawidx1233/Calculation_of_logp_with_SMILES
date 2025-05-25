from rdkit import Chem
from rdkit.Chem import Descriptors
import logging
import csv
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MolecularFormulaCalculator")


class MolecularLogPCalculator:

    @staticmethod
    def read_smiles_from_file(file_path: str) -> list:
        try:
            smiles_list = []
            with open(file_path, "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line:
                        smiles_list.append(stripped_line)
            logger.info(f"Odczytane {len(smiles_list)} SMILES z pliku {file_path}")
            return smiles_list
        except FileNotFoundError:
            logger.error(f"Plik nie został znaleziony: {file_path}")
            return []
        except Exception as e:
            logger.error(f"Błąd podczas odczytu pliku {e}")
            return []

    @staticmethod
    def smiles_to_mol(smiles_list: list) -> list:
        molecules = []
        for idx, smiles in enumerate(smiles_list):
            try:
                mol = Chem.MolFromSmiles(smiles)
                if mol is None:
                    logger.warning(f"Nieprawidłowy SMILES (indesk: {idx}): {smiles}")
                else:
                    molecules.append(mol)
            except Exception as e:
                logger.error(f"Błąd konwersji SMILES (indeks {idx}): {e}")
        logger.info(f"Konwersja zakończona. Liczba poprawnych cząsteczek: {len(molecules)}")
        return molecules

    @staticmethod
    def calculate_logp(mol: str) -> float | None:
        try:
            return Descriptors.MolLogP(mol)
        except Exception as e:
            logger.error(f"Błąd podczas obliczania logP: {e}")
            return None

    @staticmethod
    def save_results_to_csv(result:list, output_file:str):
        try:
            print()
        except Exception as e:
            logger.error(f"Błąd podczas zapisu do pliku CSV: {e}")



