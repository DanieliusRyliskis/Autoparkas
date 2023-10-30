import pandas
import os

not_complete = True

while not_complete:
    try:
        # __________Exercise 1__________
        duplicates = []
        auto_data = pandas.read_csv("new_data.csv")
        gamintojai = auto_data["Gamintojas:"].to_list()
        gamintojai_nodpl = list(set(gamintojai))
        for g in gamintojai_nodpl:
            amount = gamintojai.count(g)
            if amount > 1:
                duplicates.append(f"{g}: {amount} vnt.")
            else:
                pass
        print(duplicates)
        # __________Exercise 2__________
        def main():
            auto_data = pandas.read_csv("new_data.csv")
            gamintojo_pav = input("Įveskite gamintojo pavadinimą: ").title()
            gamintojo_masinos = auto_data[auto_data["Gamintojas:"] == gamintojo_pav]
            if not gamintojo_masinos.empty:
                print(f"Štai jūsų mašinos {gamintojo_pav}:")
                for index, row in gamintojo_masinos.iterrows():
                    print(
                        f"Valstybinis numeris: {row['Valstybinis numeris:']}, Modelis: {row['Modelis:']}, Pagaminimo metai: {row['Pagaminimo metai:']}")
            else:
                print(f"Nerasta mašinų, kurių gamintojas yra {gamintojo_pav}.")


        if __name__ == "__main__":
            main()
        # __________Exercise 3__________
        file_path = 'senesni_automobiliai.csv'
        if os.path.exists(file_path):
            pass
        else:
            metai = auto_data["Pagaminimo metai:"].to_list()
            senesni = [i for i in metai if 2023-i > 10]
            senesni_nodpl = list(set(senesni))
            for m in senesni_nodpl:
                atitikmuo = (auto_data[auto_data['Pagaminimo metai:'] == m])
                atitikmuo_index = atitikmuo.index.to_list()
                try:
                    senesni_automobiliai = pandas.read_csv('senesni_automobiliai.csv')
                    new_data = auto_data.iloc[atitikmuo_index]
                    new_data.to_csv('senesni_automobiliai.csv', mode='a', header=False, index=False)

                except FileNotFoundError:
                    senesni_automobiliai = auto_data.iloc[atitikmuo_index]
                    senesni_automobiliai.to_csv('senesni_automobiliai.csv', mode='w', index=False)
            removed_column = pandas.read_csv('senesni_automobiliai.csv')
            removed_column = removed_column.drop('Unnamed: 0', axis=1)
            removed_column = removed_column.reset_index()
            removed_column.columns = [''] + list(removed_column.columns[1:])
            removed_column.to_csv('senesni_automobiliai.csv', index=False)
        not_complete = False

    except FileNotFoundError:
        Autoparkas = {
            'Valstybinis numeris:': ["ABC 784", "LKA 451", "OTY 751", "LFD 787", "PTS 454", "RTS 653", "TBV 762",
                                     "LRE 741", "TKL 745", "LFF 132", "BBN 769", "PNM 656", "LER 345", "BNL 326",
                                     "OPT 189", "TKL 778", "PPO 854", "PKG 617", "PLT 465", "PFL 456", "POT 688",
                                     "TRP 665", "PLT 456", "TRL 545", "PFL 564", "PTL 564", "LLP 887", "LLF 554",
                                     "OPR 778", "DSL 665", "YTL 878", "RLT 659", "LDK 878", "LFK 564", "ATR 587",
                                     "OPT 646", "SST 887", "NPT 998", "PZD 453", "OTP 663", "TTP 654", "HTL 998",
                                     "PDZ 659", "TDI 323", "POP 666", "OOP 662", "LLY 444", "TTD 888", "OPY 787",
                                     "CBD 551", "LOP 633", "LDP 635", "RTX 592", "OPN 347", "LEM 829", "PPP 103"],
            'Gamintojas:': ["Hyundai ", "Audi", "Volkswagen", "Toyota", "Toyota", "Skoda", "Hyundai", "Fiat", "Fiat",
                            "Toyota", "Audi", "Volkswagen", "Volkswagen", "Toyota", "Lexus", "Mercedes-Benz", "Dacia",
                            "Toyota", "Subaru", "Dacia", "Dacia", "Skoda", "Kia", "Audi", "Nissan", "Volkswagen",
                            "Citroen", "Opel", "Porsche", "Toyota", "Audi", "Skoda", "Volkswagen", "Volkswagen",
                            "Volkswagen", "Toyota", "Skoda", "Range Rover", "Skoda", "Ford", "Chrysler", "Volkswagen",
                            "Volkswagen", "Renault", "Toyota", "Skoda", "Range Rover", "Citroen", "Ford", "BMW",
                            "Suzuki", "Suzuki", "Suzuki", "Skoda", "Range Rover", "Opel"],
            'Modelis:': ["i20", "Q7", "Passat", "Proace City", "Land Cruiser", "Octavia TSI", "i20 Active",
                         "Ducato Maxi", "Ducato", "Land Cruiser", "SQ7 Quattro", "Passat", "Passat CC TSI",
                         "C-HR Hybrid", "RX 450h", "Vito N1", "Logan", "Proace Verso Long", "Outback", "Logan MCV",
                         "Logan", "Superb AT", "Sportage", "A5 SPORTBACK 2.0 Quattro", "Navara", "Touran", "Jumper",
                         "Ampera", "Macan", "RAV4 Hybrid", "RS3 Sportback", "Fabia", "Crafter 4Motion",
                         "Touareg V6 Bluemotion", "Passat Highline BiTDI 4Motion", "Land Cruiser", "Kodiaq",
                         "Velar R-Dynamic", "Octavia Scout 4x4", "Galaxy AT", "Pacifica 3.6 AT",
                         "Jetta 2.0 TDI BlueMotion", "Amarok Hunter Edition", "Kangoo", "Corolla Hybrid",
                         "Octavia Scout", "Sport", "Jumper", "S-MAX AT", "550 i xDrive", "Grand Vitara", "Grand Vitara",
                         "Grand Vitara", "Octavia TSI", "Sport HSE", "Astra"],
            'Pagaminimo metai:': ["2017", "2014", "2020", "2021", "2021", "2016", "2017", "2021", "2018", "2015",
                                  "2018", "2017", "2016", "2019", "2015", "2022", "2017", "2019", "2019", "2017",
                                  "2017", "2016", "2020", "2009", "2018", "2017", "2016", "2012", "2020", "2016",
                                  "2017", "2018", "2019", "2012", "2017", "2019", "2019", "2018", "2016", "2016",
                                  "2017", "2017", "2020", "2019", "2019", "2017", "2015", "2016", "2015", "2010",
                                  "2011", "2012", "2012", "2018", "2015", "2011"],
        }
        data = pandas.DataFrame(Autoparkas)
        data.to_csv("new_data.csv")
