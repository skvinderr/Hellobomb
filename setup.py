from distutils.core import setup
setup(
  name = 'Hellobomb',         # How you named your package folder (MyLib)
  packages = ['Hellobomb'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='afl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is a SMS And CALL and MAIL bomber , by ADI',   # Give a short description about your library
  author = 'ADITYA',                   # Type in your name
  author_email = 'skvinderr@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/skvinderr/Hellobomb',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/skvinderr/Hellobomb/archive/refs/heads/master.zip',    # I explain this later on
  keywords = ['Bomber', 'SMS bomber', 'Call bomber', 'Free bomber'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Academic Free License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
