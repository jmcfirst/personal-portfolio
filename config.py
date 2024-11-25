class PersonalInfo:
    def __init__(self):
        self.name = "John Doe"
        self.title = "Senior Software Developer"
        self.tagline = "Crafting elegant solutions to complex problems"
        self.profile_image = "https://images.unsplash.com/photo-1576558656222-ba66febe3dec"
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
        self.experience = [
            {
                "title": "Senior Developer @ Tech Corp",
                "period": "2020 - Present",
                "description": "Led development of enterprise applications and mentored junior developers."
            },
            {
                "title": "Full Stack Developer @ StartUp Inc",
                "period": "2018 - 2020",
                "description": "Developed and maintained multiple client projects using modern web technologies."
            }
        ]
        self.projects = [
            {
                "title": "E-commerce Platform",
                "description": "A full-stack e-commerce solution with real-time inventory management.",
                "technologies": ["React", "Node.js", "MongoDB"]
            },
            {
                "title": "Task Management App",
                "description": "A collaborative task management tool with real-time updates.",
                "technologies": ["Vue.js", "Flask", "PostgreSQL"]
            }
        ]
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
