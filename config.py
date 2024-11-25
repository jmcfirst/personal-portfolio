class PersonalInfo:

    def __init__(self):
        self.name = "John Cosenzo"
        self.title = "Life Log New York Mets Fan"
        self.tagline = "Grew up in Queens NY and spent many summer vacation days at Shea Stadium"
        self.profile_image = "/static/images/shea.jpeg"
        self.social_links = {
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "twitter": "https://twitter.com"
        }
        self.skills = {
            "Frontend": ["HTML5", "CSS3", "JavaScript", "React", "Vue.js"],
            "Backend": ["Python", "Node.js", "Django", "Flask", "Express"],
            "Database": ["PostgreSQL", "MongoDB", "Redis"]
        }
        self.experience = [{
            "title":
            "Senior Developer @ Tech Corp",
            "period":
            "2020 - Present",
            "description":
            "Led development of enterprise applications and mentored junior developers."
        }, {
            "title":
            "Full Stack Developer @ StartUp Inc",
            "period":
            "2018 - 2020",
            "description":
            "Developed and maintained multiple client projects using modern web technologies."
        }]
        self.projects = [{
            "title": "E-commerce Platform",
            "description":
            "A full-stack e-commerce solution with real-time inventory management.",
            "technologies": ["React", "Node.js", "MongoDB"]
        }, {
            "title": "Task Management App",
            "description":
            "A collaborative task management tool with real-time updates.",
            "technologies": ["Vue.js", "Flask", "PostgreSQL"]
        }]
        self.copyright_year = "2023"

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
