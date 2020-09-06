from setuptools import find_packages, setup

setup(
    name="slack-wh-hpc",
    version="1.0.0",
    description="Slack incoming-webhook client tool for people doing high performance computing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="nayu.T.S",
    url="https://github.com/tasotasoso/slack-wh-hpc",
    keywords="slack webhook python",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7.4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: MIT License",
    ],
)
