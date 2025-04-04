import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ai-content-generator",
    version="0.1.0",
    author="Chukwukaodinaka Bryan Obieyisi",
    author_email="ckobieyisi@gmail.com",
    description="An autonomous AI Social Media content generator built with OpenAI Responses SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-content-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "openai-agents==0.0.5",
        "openai>=0.27.0",
        "PyYAML>=6.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-social-media-manager = scripts.run_agent:main",
        ],
    },
)
