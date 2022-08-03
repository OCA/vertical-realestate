import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-vertical-realestate",
    description="Meta package for oca-vertical-realestate Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-realestate',
        'odoo13-addon-realestate_estate',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
