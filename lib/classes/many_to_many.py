class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        # Check if the title attribute already exists to prevent changes
        if hasattr(self, "title"):
            raise AttributeError("Title cannot be changed")
        else:
            # Ensure the title is a string and meets length requirements
            if isinstance(title, str):
                if 5 <= len(title) <= 50:
                    self._title = title
                else:
                    raise ValueError("Title must be between 5 and 50 characters")
            else:
                raise TypeError("Title must be a string")
    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, author):
        # Validate that the author is an instance of the Author class
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")

    @magazine.setter
    def magazine(self, magazine):
        # Validate that the magazine is an instance of the Magazine class
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")














class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name must be longer than 0 characters")

        self._name = name
        self._articles = []
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return list(self._articles)

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        # Use set to get unique categories
        areas = set(article.magazine.category for article in self._articles)
        return list(areas) if areas else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if len(category) == 0:
            raise ValueError("category must be longer than 0 characters")

        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("name must be a string")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("name must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("category must be a string")
        if len(new_category) == 0:
            raise ValueError("category must be longer than 0 characters")
        self._category = new_category

    def articles(self):
        return list(self._articles)

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        # Count each author's contributions to find top contributors
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        top_authors = [author for author, count in author_counts.items() if count > 2]
        return top_authors or None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        # Use max with a key function to find the magazine with the most articles
        return max(cls.all_magazines, key=lambda mag: len(mag._articles))