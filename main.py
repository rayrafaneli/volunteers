class Volunteer:
    def __init__(self, name, skills, availability, contact_info):
        self.name = name
        self.skills = skills
        self.availability = availability
        self.contact_info = contact_info

    def display_info(self):
        return f"{self.name} - Habilidades: {self.skills}, Disponibilidade: {self.availability}, Contato: {self.contact_info}"


class Organization:
    def __init__(self, name, needs, contact_info):
        self.name = name
        self.needs = needs
        self.contact_info = contact_info

    def display_info(self):
        return f"{self.name} - Necessidades: {self.needs}, Contato: {self.contact_info}"


class VolunteerMatchingPlatform:
    def __init__(self):
        self.volunteers = []
        self.organizations = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def add_organization(self, organization):
        self.organizations.append(organization)

    def display_volunteers(self):
        for volunteer in self.volunteers:
            print(volunteer.display_info())

    def display_organizations(self):
        for organization in self.organizations:
            print(organization.display_info())

    def match_volunteers(self):
        matches = []
        for organization in self.organizations:
            for volunteer in self.volunteers:
                if any(skill in organization.needs for skill in volunteer.skills):
                    matches.append((organization, volunteer))
        return matches


def main():
    platform = VolunteerMatchingPlatform()

    while True:
        print("\n1. Adicionar voluntário")
        print("2. Adicionar organização")
        print("3. Mostrar voluntários")
        print("4. Mostrar organizações")
        print("5. Encontrar correspondências")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do voluntário: ")
            skills = input("Habilidades (separadas por vírgulas): ").split(",")
            availability = input("Disponibilidade: ")
            contact_info = input("Informações de contato: ")
            volunteer = Volunteer(name, skills, availability, contact_info)
            platform.add_volunteer(volunteer)
        elif choice == "2":
            name = input("Nome da organização: ")
            needs = input("Necessidades (separadas por vírgulas): ").split(",")
            contact_info = input("Informações de contato: ")
            organization = Organization(name, needs, contact_info)
            platform.add_organization(organization)
        elif choice == "3":
            platform.display_volunteers()
        elif choice == "4":
            platform.display_organizations()
        elif choice == "5":
            matches = platform.match_volunteers()
            for org, vol in matches:
                print(f"Organização: {org.name} - Voluntário: {vol.name}")
        elif choice == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
