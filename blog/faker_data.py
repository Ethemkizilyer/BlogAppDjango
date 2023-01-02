# from .models import Category, Blog
# from faker import Faker
# from datetime import datetime

# def run():
#     fake = Faker(['en-US'])
#     categories = (
#         "Politics",
#         "Sports",
#         "Millitary",
#         "Travel",
#         "Showbiz"
#     )

#     for category_id in categories:
#         new_category = Category.objects.create(category_name = category_id)
#         for _ in range(30):
#             Blog.objects.create(category_id = new_category, title = fake.company(), content = fake.text(), is_published = fake.pybool())
    
#     print('Finished')

from faker import Faker
from .models import Category, Blog

def run():
    fake = Faker(["tr-TR"])
    categories = ("Life", "Science", "Politics", "Sports")

    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(20):
            Blog.objects.create(category = new_category, title = fake.name(), content=fake.text())
    print("Finished")