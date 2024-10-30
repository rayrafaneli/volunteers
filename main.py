import tkinter as tk
from tkinter import messagebox

class Volunteer:
    def __init__(self, name, skills, availability, contact_info):
        self.name = name
        self.skills = skills
        self.availability = availability
        self.contact_info = contact_info

    def display_info(self):
        return f"{self.name} - Habilidades: {', '.join(self.skills)}, Disponibilidade: {self.availability}, Contato: {self.contact_info}"


class Organization:
    def __init__(self, name, needs, contact_info):
        self.name = name
        self.needs = needs
        self.contact_info = contact_info

    def display_info(self):
        return f"{self.name} - Necessidades: {', '.join(self.needs)}, Contato: {self.contact_info}"


class VolunteerMatchingPlatform:
    def __init__(self):
        self.volunteers = []
        self.organizations = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def add_organization(self, organization):
        self.organizations.append(organization)

    def display_volunteers(self):
        return "\n".join(volunteer.display_info() for volunteer in self.volunteers)

    def display_organizations(self):
        return "\n".join(organization.display_info() for organization in self.organizations)

    def match_volunteers(self):
        matches = []
        for organization in self.organizations:
            for volunteer in self.volunteers:
                if any(skill in organization.needs for skill in volunteer.skills):
                    matches.append((organization, volunteer))
        return matches

class VolunteerMatchingApp:
    def __init__(self, root):
        self.platform = VolunteerMatchingPlatform()
        self.root = root
        self.root.title("Plataforma de Correspondência de Voluntários")

        # Labels and entries for Volunteers
        self.volunteer_name_label = tk.Label(root, text="Nome do Voluntário")
        self.volunteer_name_label.pack()
        self.volunteer_name_entry = tk.Entry(root)
        self.volunteer_name_entry.pack()

        self.volunteer_skills_label = tk.Label(root, text="Habilidades (separadas por vírgulas)")
        self.volunteer_skills_label.pack()
        self.volunteer_skills_entry = tk.Entry(root)
        self.volunteer_skills_entry.pack()

        self.volunteer_availability_label = tk.Label(root, text="Disponibilidade")
        self.volunteer_availability_label.pack()
        self.volunteer_availability_entry = tk.Entry(root)
        self.volunteer_availability_entry.pack()

        self.volunteer_contact_label = tk.Label(root, text="Informações de Contato")
        self.volunteer_contact_label.pack()
        self.volunteer_contact_entry = tk.Entry(root)
        self.volunteer_contact_entry.pack()

        self.add_volunteer_button = tk.Button(root, text="Adicionar Voluntário", command=self.add_volunteer)
        self.add_volunteer_button.pack()

        # Labels and entries for Organizations
        self.organization_name_label = tk.Label(root, text="Nome da Organização")
        self.organization_name_label.pack()
        self.organization_name_entry = tk.Entry(root)
        self.organization_name_entry.pack()

        self.organization_needs_label = tk.Label(root, text="Necessidades (separadas por vírgulas)")
        self.organization_needs_label.pack()
        self.organization_needs_entry = tk.Entry(root)
        self.organization_needs_entry.pack()

        self.organization_contact_label = tk.Label(root, text="Informações de Contato")
        self.organization_contact_label.pack()
        self.organization_contact_entry = tk.Entry(root)
        self.add_organization_button = tk.Button(root, text="Adicionar Organização", command=self.add_organization)
        self.add_organization_button.pack()

        self.organization_contact_entry.pack()

        # Buttons to display information and match volunteers
        self.show_volunteers_button = tk.Button(root, text="Mostrar Voluntários", command=self.show_volunteers)
        self.show_volunteers_button.pack()

        self.show_organizations_button = tk.Button(root, text="Mostrar Organizações", command=self.show_organizations)
        self.show_organizations_button.pack()

        self.match_button = tk.Button(root, text="Encontrar Correspondências", command=self.match_volunteers)
        self.match_button.pack()

    def add_volunteer(self):
        name = self.volunteer_name_entry.get()
        skills = self.volunteer_skills_entry.get().split(',')
        availability = self.volunteer_availability_entry.get()
        contact_info = self.volunteer_contact_entry.get()
        volunteer = Volunteer(name, skills, availability, contact_info)
        self.platform.add_volunteer(volunteer)
        messagebox.showinfo("Sucesso", "Voluntário adicionado!")

    def add_organization(self):
        name = self.organization_name_entry.get()
        needs = self.organization_needs_entry.get().split(',')
        contact_info = self.organization_contact_entry.get()
        organization = Organization(name, needs, contact_info)
        self.platform.add_organization(organization)
        messagebox.showinfo("Sucesso", "Organização adicionada!")

    def show_volunteers(self):
        volunteers = self.platform.display_volunteers()
        messagebox.showinfo("Voluntários", volunteers)

    def show_organizations(self):
        organizations = self.platform.display_organizations()
        messagebox.showinfo("Organizações", organizations)

    def match_volunteers(self):
        matches = self.platform.match_volunteers()
        match_info = "\n".join(f"Organização: {org.name} - Voluntário: {vol.name}" for org, vol in matches)
        messagebox.showinfo("Correspondências", match_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = VolunteerMatchingApp(root)
    root.mainloop()
