from pathlib import Path
from zensols.pybuild import SetupUtil

su = SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="zensols.cnndmdb",
    package_names=['zensols', 'resources'],
    package_data={'': ['*.conf', '*.json', '*.yml', '*.sql']},
    description='Creates a SQLite database if the CNN and DailyMail summarization dataset.',
    user='plandes',
    project='cnndmdb',
    keywords=['tooling'],
).setup()
