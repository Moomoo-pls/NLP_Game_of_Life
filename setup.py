import setuptools

setuptools.setup(
    name="Moo_NLP_Game_of_Life",
    version="1.0.0",
    author="Stephen Moo-Young",
    author_email="mooyoung12@gmail.com",
    description="Game of Life for the take home coding challenge",
    url="https://github.com/Moomoo-pls/NLP_Game_of_Life",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'game-of-life=Game_of_Life.main:main',
        ]
    },
)