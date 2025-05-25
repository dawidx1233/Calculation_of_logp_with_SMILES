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

        results = []
        for idx, mol in enumerate(molecules):
            logp = mlogpc.calculate_logp(mol)
            if logp is not None:
                results.append((list_smiles[idx], logp))

        output_file = "result.csv"
        mlogpc.save_results_to_csv(results, output_file)


if __name__ == "__main__":
    main()
