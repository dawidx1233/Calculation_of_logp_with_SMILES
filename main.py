from calculator import MolecularLogPCalculator as mlogpc


def main():
    print("Podaj nazwę pliku z SMILES lub 'q' aby zakończyć")
    while True:
        user_input = input("Podaj nazwę pliku z SMILES: ").strip()
        if user_input == 'q':
            print("Zakończenie działania programu")
            break
        list_smiles = mlogpc.read_smiles_from_file(user_input)
        if not list_smiles:
            continue

        molecules = mlogpc.smiles_to_mol(list_smiles)
        print(molecules)


if __name__ == "__main__":
    main()
