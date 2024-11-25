class PersonalInfo:

    def __init__(self):
        self.name = "John Cosenzo"
        self.title = "Life Log New York Mets Fan"
        self.tagline = "Grew up in Queens NY and spent many summer vacation days at Shea Stadium"
        self.profile_image = "/static/images/shea.jpeg"
        self.social_links = {}
        self.skills = {
            "Frontend": ["HTML5", "CSS3", "JavaScript", "React", "Vue.js"],
            "Backend": ["Python", "Node.js", "Django", "Flask", "Express"],
            "Database": ["PostgreSQL", "MongoDB", "Redis"]
        }
        self.experience = [
            {
                "title": "First Game at Shea Stadium",
                "period": "1986",
                "description": "Attended my first Mets game at Shea Stadium during their championship season. Watched Gary Carter hit a walk-off home run against the Giants. The energy in the stadium was electric!"
            },
            {
                "title": "Season Ticket Holder",
                "period": "1990-2000",
                "description": "Became a dedicated season ticket holder, witnessing countless memorable moments including Doc Gooden's no-hitter in 1996 and Mike Piazza's legendary performances."
            },
            {
                "title": "Shea Stadium Farewell",
                "period": "2008",
                "description": "Attended the final game at Shea Stadium. An emotional day saying goodbye to a stadium that held so many memories. Watched as past Mets legends took the field one last time."
            },
            {
                "title": "Citi Field Era",
                "period": "2009-Present",
                "description": "Continuing the tradition at Citi Field, while keeping the spirit of Shea Stadium alive. Regular attendee at home games, passing down Mets traditions to the next generation."
            }
        ]
        self.projects = [
            {
                "title": "Small Website",
                "description": "A full-stack small starter website",
                "technologies": ["React", "Node.js", "MongoDB"]
            },
            {
                "title": "Task Management App",
                "description": "A simple task management application",
                "technologies": ["Vue.js", "Flask", "PostgreSQL"]
            }
        ]
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
