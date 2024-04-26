from setuptools import setup, find_packages


setup(
    name="env",
    version="0.0.1",
    description="RT-Thread Env",
    url="https://github.com/RT-Thread/env.git",
    author="RT-Thread Development Team",
    author_email="rt-thread@rt-thread.org",
    keywords="rt-thread",
    license="Apache License 2.0",
    project_urls={
        "Github repository": "https:/github.com/rt-thread/env.git",
        "User guide": "https:/github.com/rt-thread/env.git",
    },
    python_requires=">=3.6",
    install_requires=[
        "SCons>=4.0.0",
        "requests",
        "psutil",
        "kconfiglib",
        "windows-curses; platform_system=='Windows'",
    ],
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
    ),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "env=env.env:main",
            "menuconfig=env.env:menuconfig",
            "pkgs=env.env:pkgs",
            "sdk=env.env:sdk",
            "system=env.env:system",
        ]
    },
)
