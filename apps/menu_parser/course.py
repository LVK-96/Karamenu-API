class Course(object):
    """Class used for serialization of courses."""

    def __init__(self, category, name_fi, name_en,
                 desc_fi, desc_en, tags, price):
        self.category = category
        self.name_fi = name_fi
        self.name_en = name_en
        self.desc_fi = desc_fi
        self.desc_en = desc_en
        self.tags = tags
        self.price = price

    def __eq__(self, other):
        """For testing sodexo.parse_courses."""
        return self.__dict__ == other.__dict__
