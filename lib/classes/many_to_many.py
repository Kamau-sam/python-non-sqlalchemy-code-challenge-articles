class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("title must be between 5 and 50 characters")








#class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass