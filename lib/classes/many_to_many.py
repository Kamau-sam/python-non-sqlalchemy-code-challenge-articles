class Article:
    all= []
    
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
       # Check if the title attribute already exists (immutable)
       if hasattr(self,"title"):AttributeError("Title cannot be changed")
       else:
            # Validate the title's length and type
            if isinstance(title,str):
                if 5<=len(title)<=50:
                    self._title=title
                else:ValueError("Title must be between 5 and 50 characheters")
            else:TypeError("Title must be a string")
  
    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, author):
        # Validate the author's type
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")
    
    @magazine.setter
    def magazine(self, magazine):
        # Validate the magazine's type
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")
     

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name

    def articles(self):
        # Get all articles written by the author
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        # Get all unique magazines the author has contributed to
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        # Add a new article for the author
        articles = Article(self, magazine, title)
        return articles
   
    def topic_areas(self):
        # Get all unique categories of magazines the author has written for
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

   

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
   
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")
    
    def articles(self):
        # Get all articles associated with the magazine
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        # Get all contributors (authors) of the magazine
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        # Get titles of all articles associated with the magazine
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None
   
    def contributing_authors(self):
      # Get authors who have written more than 2 articles for the magazine
      authors = {}
      for article in self.articles():
          if article.author in authors:
              authors[article.author] += 1
          else:
              authors[article.author] = 1
      contributing_authors = [author for author, count in authors.items() if count >= 2]
      return contributing_authors if contributing_authors else None
    
   
    @staticmethod
    def top_publisher():
        if Article.all:
            magazine_article_count = {}
            for article in Article.all:
                magazine = article.magazine
                if magazine in magazine_article_count:
                    magazine_article_count[magazine] += 1
                else:
                   magazine_article_count[magazine] = 1
            
            # Get the magazine with the most articles
            return max(magazine_article_count, key=magazine_article_count.get)
        return None

    


# Create instances of authors
author1 = Author("Kamau Samuel")
author2 = Author("Ken Walibora")
author3 = Author("Wallar Bin Wallar")

# Create instances of magazines
magazine1 = Magazine("Tech Health Today", "Health")
magazine2 = Magazine("Data Insights", "Data Science")

# Add articles to the magazines
author1.add_article(magazine1, "Advancements in Telemedicine")
author1.add_article(magazine2, "The Future of Data Analytics")
author2.add_article(magazine1, "The Power of Digital Health Records")
author3.add_article(magazine1, "Understanding Human Physiology")
author3.add_article(magazine2, "The Impact of Big Data in Healthcare")
# Add more articles to Magazine 1 by existing authors
author1.add_article(magazine1, "Innovations in Medical Imaging")
author2.add_article(magazine1, "The Role of AI in Healthcare")

article1 = Article(author1, magazine1, "Challenges in Healthcare AI Implementation")
print(article1.title)

contributing_authors = magazine1.contributing_authors()

if contributing_authors:
    print("Authors who have written more than two articles for Magazine one:")
    for author in contributing_authors:
        print(author.name)
else:
    print("No authors found who have written more than two articles for Magazine1")

top_publisher = Magazine.top_publisher()

if top_publisher:
    print(f"The Magazine with the most articles is: {top_publisher.name}")
    print(f"Category: {top_publisher.category}")
else:
    print("No articles found.")
