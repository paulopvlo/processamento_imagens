from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_de_imagens_desafio",
    version="0.0.1",
    author="paulopvlo",
    author_email="paulo.pv@gmail.com",
    description="Criando pacote processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulopvlo/processamento_de_imagens.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)