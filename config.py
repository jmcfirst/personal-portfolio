class PersonalInfo:

    def __init__(self):
        self.name = "John Cosenzo"
        self.title = "Life Long New York Mets Fan"
        self.tagline = "Grew up in Queens NY and spent many summer vacation days at Good Old Shea Stadium- Just 7 stops on the 7 train and I was there!"
        self.profile_image = "/static/images/shea.jpeg"
        self.social_links = {}
        self.skills = {
            "Frontend": ["HTML5", "CSS3", "JavaScript"],
            "Backend": ["Python", "Node.js", "Django", "Flask", "Express"],
            "Database": ["MySQL", "MongoDB"]
        }
        self.experience = [{
            "title":
            "My Shea Stadium History",
            "period":
            "1970",
            "description":
            "Attended my first Mets game at Shea Stadium in The Summer of 1970"
        }, {
            "title":
            "Attend Many Games At Shea",
            "period":
            "1970-1980",
            "description":
            "Watched Tom Seaver Pitch Many Games that he should of won, but the Mets were a weak hitting team those days"
        }, {
            "title":
            "Shea Stadium Farewell",
            "period":
            "2008",
            "description":
            "Watched on TV the final game at Shea Stadium. An emotional day saying goodbye to a stadium that held so many memories. Watched as past Mets legends took the field one last time."
        }, {
            "title":
            "Citi Field Era",
            "period":
            "2009-Present",
            "description":
            "Continuing the tradition at Citi Field, while keeping the spirit of Shea Stadium alive. Regular attendee at home games, passing down Mets traditions to the next generation."
        }]
        self.projects = [{
            "title": "Personal Website Development",
            "description": "Custom website design and development tailored to your needs",
            "technologies": ["HTML5", "CSS3", "JavaScript"]
        }, {
            "title": "Web Application Development",
            "description": "Full-stack web application development with modern technologies",
            "technologies": ["Python", "Flask", "MongoDB"]
        }]
        self.copyright_year = "2024"

    def get_data(self):
        return {
            "name": self.name,
            "title": self.title,
            "tagline": self.tagline,
            "profile_image": self.profile_image,
            "social_links": self.social_links,
            "skills": self.skills,
            "experience": self.experience,
            "projects": self.projects,
            "copyright_year": self.copyright_year
        }
