from setuptools import setup

setup(
    name = "django-eve-api",
    version = "0.0.1",
    author = "Joshua Blake",
    author_email = "joshbblake@gmail.com",
    description = ("Convenience functions for using the EvE API from Django "
                    "and storing keys in the database"),
    license = "BSD",
    packages = ['api'],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
    ],
)